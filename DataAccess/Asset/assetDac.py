#encoding:utf-8
from Asset.models import AssetType,AssetList
from ViewModel.Asset import assetViewModel


def getAll():
    '''
    获取所有资产
    :return:
    '''
    model=AssetList.objects.all()
    viewmodelList=[]

    for item in model:
        viewmodel=assetViewModel.assetViewModel()
        viewmodel.AssetName=item.assetName
        viewmodel.assetType= AssetType.objects.get(id=item.id)
        viewmodel.assetType=item.assetType
        viewmodel.Local=item.local
        viewmodel.Factory=item.Factory
        viewmodel.UserOrDep=item.UserOrDep
        viewmodelList.append(viewmodel)

    return viewmodelList