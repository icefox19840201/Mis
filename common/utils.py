#encoding:utf-8
from django.shortcuts import render_to_response
from common import urlconfig


def check_isLogin(main_func):
    '''
    登录验证
    :param main_func:
    :return:
    '''
    def wrapper(request,*args,**kwargs):

        if "user" not in request.session:
            return render_to_response(urlconfig.login)
        return main_func(request,*args,**kwargs)
    return wrapper

def str2int(str,default=-1):
    pass

def page404(request):
    return  render_to_response(urlconfig.page404)

def GetData(request,key):
    '''
    获取GET与Post提交参数的值
    :param request:
    :param key:
    :return:
    '''
    if request.method=="GET":
        return request.GET.get(key,None)
    return request.POST.get(key,None)

def Is_GET(request):
    if request.method=="GET":
        return True
    return False

def Is_POST(request):
    if request.method=="POST":
        return True
    return False



