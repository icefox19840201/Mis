#encoding:utf-8
from django.shortcuts import render_to_response
from common import urlconfig


def check_isLogin(main_func):
    def wrapper(request,*args,**kwargs):

        if "user" not in request.session:
            return render_to_response(urlconfig.login)
        return main_func(request,*args,**kwargs)
    return wrapper

def str2int(str,default=-1):
    pass

def page404(request):
    return  render_to_response(urlconfig.page404)
