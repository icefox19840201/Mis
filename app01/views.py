#encoding:utf-8
import json
import uuid
import hashlib
from django.contrib.messages.storage import session
from django.http import cookie
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.core import serializers
# Create your views here.
from django.template.context_processors import csrf
from common.utils import check_isLogin
from models import user, userRole, Right
from common import urlconfig
from common import actionconfig

content={}
@check_isLogin
def index(request):
   global content
   return render_to_response(urlconfig.index,content)

@check_isLogin
def project(request):
    return render_to_response(urlconfig.project,content)

def login(request):

    content.update(csrf(request))
    if request.method=="GET":
         return render_to_response(urlconfig.login,content)
    elif request.method=="POST":

        username=request.POST.get("username",None)
        pwd=request.POST.get("password",None)
        pwd=gethashCode(request,pwd)
        try:

            userobj= user.objects.get(loginName=username,pwd=pwd)
            if userobj:
               request.session["user"]=userobj.username
              # request.session["currentUserInfo"]=json.dumps(userobj)
               content["user"]= request.session["user"]
               return  render_to_response(urlconfig.index,content)
        except Exception as e:
            raise e
               #return render_to_response(urlconfig.login,content)
    return render_to_response(urlconfig.login,content)

@check_isLogin
def logout(request):
     content=None
     del request.session["user"]
     return render_to_response(urlconfig.login)
def tasks(request):
    return render_to_response(urlconfig.tasks,content)
def active(request):
    return render_to_response("app01/activity.htm",content)
def message(request):
    return render_to_response("app01/messages.htm",content)
def files(request):
    return render_to_response("app01/files.htm",content)
def profile(request):
    return render_to_response("app01/profile.htm",content)
def setting(request):
    return render_to_response("app01/settings.htm",content)
def blank(request):
    return render_to_response("app01/blank.htm",content)
def help(request):
    return render_to_response("app01/help.htm",content)
def gallery(request):
    return render_to_response("app01/gallery.htm")

@check_isLogin
def usermanage(request):
     global content
     if "saveuser" in request.session:
          del request.session["saveuser"]
          content.update(csrf(request))
          if "data" in content:
              del content["data"]

          return render_to_response(urlconfig.usermanage,content)
     if request.method=="GET" and request.GET.get("action")=="mainview":
          uinfo=getAllUserInfo(request)
          for user in uinfo:
              roleinfo=  userRole.objects.get(id=user.usrRole_id)
              user.roleName=roleinfo.role_desc
          content["data"]=uinfo
          return render_to_response(urlconfig.usermanage,content)
     elif request.method=="GET" and request.GET.get("action")=="adduser":
         content["role"]=getRole(request)
         return  render_to_response(urlconfig.useradd,content)
     elif request.method=="GET" and request.GET.get("action")=="deletealluser":
         pass
     elif  request.method=="GET" and request.GET.get("action")=="view":
         pass
     elif  request.method=="GET" and request.GET.get("action")=="edit":
         pass
     elif  request.method=="GET" and request.GET.get("action")=="delete":
         pass

     if request.method=="POST":
         try:
            from models import user
            userinfo=user()
            userinfo.id=uuid.uuid4()
            userinfo.loginName=request.POST.get("loginname",None)
            userinfo.usercode=request.POST.get("usercode",None)
            userinfo.username=request.POST.get("username",None)
            id= uuid.UUID(request.POST.get("roleid",None))
            userinfo.usrRole=userRole.objects.get(id=id)
            m=hashlib.md5()
            userinfo.pwd=request.POST.get("pwd",None)
            if userinfo.pwd is not None:
                m.update(userinfo.pwd)
                userinfo.pwd=m.hexdigest()
            userinfo.save()
            request.session["saveuser"]=True
            return HttpResponseRedirect(actionconfig.usermanage)
         except Exception as err:
             raise err.message

@check_isLogin
def rolerightmanage(request):
    '''
    列表中查看，编辑，删除的处理
    :param request:
    :return:
    '''
    try:
        if request.method=="GET" and request.GET.get("action")=="view":
            id=request.GET.get("id")
            content["editable"]=False
            content["data"]=userRole.objects.get(id=id)
            userrole= userRole.objects.get(id=id )
            uright=userrole.role_right.all()
            return  render_to_response(urlconfig.roleright,content)
        elif  request.method=="GET" and request.GET.get("action")=="edit":

            pass
        elif  request.method=="GET" and request.GET.get("action")=="delete":

             pass
        else:
             content["role"]=getRole(request)
             return render_to_response(urlconfig.rolerightmanage, content)
    except Exception as err:

         return render_to_response(urlconfig.rolemanage,content)

@check_isLogin
def roleright(request):
    '''
    角色权限对应的多表查询（难点）
    :param request:
    :return:
    '''
    if request.method=="POST":
                try:
                    if request.POST.get("url"):
                        role_right=Right()
                        role_right.id=uuid.uuid4()
                        role_right.url=request.POST.get("url")
                        roleid=str(request.POST.get("roleid"))
                        role_right.queryRight=1 if request.POST.get("queryright",None)==u"on" else 0
                        role_right.updateRight=1 if request.POST.get("updateright",None)==u"on" else 0
                        role_right.editRight=1 if request.POST.get("addright",None)==u"on" else 0
                        role_right.deleteRight=1 if request.POST.get("deleteright",None)==u"on" else 0
                        if roleid !="-1" and roleid is  not None:
                            #多对多表的处理添加数据
                            role=userRole.objects.get(id=roleid)
                            role_right.save()
                            role.role_right.add(role_right)
                            return render_to_response(urlconfig.rolerightmanage,content)
                        else:
                            role_right.save()
                            return render_to_response(urlconfig.rolerightmanage,content)
                except Exception as err:
                    raise ValueError("获取url错误{0}",err.message)
                content["role"]=getRole(request)
                return  render_to_response(urlconfig.right,content)
    else:

        if request.method=="GET" and request.GET.get("type")=="assignroleright":
           uinfo=getAllUserInfo(request)
           contentdata=[]
           data={}
           for item in uinfo:
               urinfo=getRightByRoleId(request,item.id,item.usrRole_id)
               contentdata.append(urinfo)
           data["datacontent"]=contentdata
           return render_to_response(urlconfig.assignroleRight,data)
    return  render_to_response(urlconfig.right,content)


@check_isLogin
def getRole(request):

    content["role"]=userRole.objects.all().values("id","role_desc","role_code")
    return content["role"]

@check_isLogin
def rolemanage(request):

    if request.method=="GET":
         if request.GET.get("type")=="addrole":
            return render_to_response(urlconfig.rolemanage)

    else:
        try:
                    rolecode=request.POST.get("rolecode")
                    rolename=request.POST.get("rolename")
                    if rolecode and rolename:
                        role=userRole()
                        role.id=uuid.uuid4()
                        role.role_desc=rolename
                        role.role_code=rolecode
                        role.save()
        except:
            raise ValueError("出错了")
    return rolerightmanage(request)

def gethashCode(request,pwd):
    '''
    md5加密
    :param request:当前上下文请法度对象
    :param pwd:需要加蜜的密码明文
    :return:返回加密后的密文
    '''
    m=hashlib.md5()
    m.update(pwd)
    return m.hexdigest()

@check_isLogin
def getAllUserInfo(request):
     userinfo=user.objects.all()
     return userinfo


@check_isLogin
def getRightByRoleId(request,uid,rid):
    '''
    根据角色获取相对应的权限
    :param request: 当前上下文请求
    :param uid: userid
    :param rid: roleid
    :return:
    '''
    Result={}
    role=userRole.objects.get(id=rid)
    r_right=role.role_right.all()
    userobj=user.objects.get(id=uid)
    Result=dict(user=userobj,role=role,r_right=r_right)
    return Result
@check_isLogin
def editroleRight(request):
    '''
    角色权限调整
    :param request:
    :param request:
    :return:
    '''
    uinfo=user(request.session["currentUserInfo"])
    uroleInfo=getRightByRoleId(request,uinfo.id,uinfo.usrRole_id)
    return  HttpResponse(json.dumps(uroleInfo), content_type='application/json')






