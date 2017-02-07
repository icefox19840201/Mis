#encoding:utf-8
from django.http import JsonResponse
from django.shortcuts import render,render_to_response
from common.Asset import urlconfig
from DataAccess.Asset import assetDac
from common import utils
# Create your views here.
from common.Asset import pagging

def index(request):
    '''
    资产首页
    :param request:
    :return:
    '''
    viewModel=assetDac.getAll()
    start,end,link,total=pagging.assetPagging(request)
    return render_to_response(
                                urlconfig.index,
                                {
                                    "data":viewModel[start:end],
                                    "link":link
                                }
                              )
def search(request):
    '''
    资产搜索
    :param request:
    :return:
    '''
    searchEey=str(utils.GetData(request,"search").encode('utf-8')).lstrip()
    viewModel=assetDac.queryData(searchEey)

    return render_to_response(
                                urlconfig.index,
                                {
                                    "data":viewModel
                                }
                              )
def showDetails(request):
    '''
    获取资产详细情况
    :param request:
    :return:
    '''
    id=int(utils.GetData(request,'id'))
    data=assetDac.showDetails(id)
    return JsonResponse(data)
