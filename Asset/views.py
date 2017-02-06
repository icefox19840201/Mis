from django.shortcuts import render,render_to_response
from common.Asset import urlconfig
from DataAccess.Asset import assetDac
# Create your views here.
def index(request):
    viewModel=assetDac.getAll()
    return render_to_response(
                                urlconfig.index,
                                {
                                    "data":viewModel
                                }
                              )
