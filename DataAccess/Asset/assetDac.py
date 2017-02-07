#encoding:utf-8
from Asset.models import AssetType,AssetList
from ViewModel.Asset import assetViewModel
from . import sqlhelper

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
        type= AssetType.objects.get(id=item.id)
        viewmodel.assetType=type.name
        viewmodel.Local=item.local
        viewmodel.Factory=item.Factory
        viewmodel.UserOrDep=item.UserOrDep
        viewmodelList.append(viewmodel)

    return viewmodelList
def queryData(key):
    sql= '''
                        SELECT * FROM(	select
                        list.assetName,
                        list.`local`,
                        list.Factory,
                        list.UserOrDep,
                        type.`name`
                    from asset_assetlist list
                    LEFT JOIN
                    asset_assettype type
                    on
                    list.assetType_id=type.id
                ) a
                where
                a.assetName  LIKE '%{0}%'
                 or
                  a.`local` LIKE '%{1}%'
                  OR
                a.Factory LIKE '%{2}%'
                OR
                a.UserOrDep LIKE '%{3}%'
                OR
                a.name LIKE  '%{4}%'

        '''.format(key,key,key,key,key)
    queryData=sqlhelper.execquerySql(sql)
    listData=[]
    for item in queryData:
        viewmodel=assetViewModel.assetViewModel()
        viewmodel.AssetName=item[0]
        viewmodel.assetType=item[4]
        viewmodel.Local=item[1]
        viewmodel.Factory=item[2]
        viewmodel.UserOrDep=item[3]
        listData.append(viewmodel)
    return listData