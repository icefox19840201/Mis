from django.shortcuts import render,render_to_response
from common import utils
from common.Supplier import urlconfig
from Supplier.supperForm import SupplierForm
# Create your views here.
def index(request):
    if utils.Is_GET(request):
       return render_to_response(urlconfig.index,{'form':SupplierForm()})
