from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from common.utils import check_isLogin


@check_isLogin
def index(request):
   return render_to_response("app01/index.html")