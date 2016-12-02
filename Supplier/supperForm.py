#encoding:utf-8
from django import forms
from django.forms import ModelForm
from models import Supplier, sysType, SupplierBusinessInfo


class SupplierForm(forms.ModelForm):
    #ModelForm生成downlist下拉框
    def __init__(self,*args,**kwargs):
        super(SupplierForm,self).__init__(*args,**kwargs)
        self.fields['systemType'].widget.choices = sysType.objects.all().values_list('id','sysDesc')
        self.fields['Supplier_name'].widget.choices=SupplierBusinessInfo.objects.all().values_list('id','name')
    class Meta:
        model=Supplier
        exclude={'id',}
        #fields = ('serial_number','person_id','position','system_os','pc_score','pc_cpu','pc_memory','use_time','pc_description')

