import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from images.models import Images
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import time
import os
def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=Images.objects.filter().all()
    resList=[]
    for p in res:
        college = {}
        college['createTime'] =p.create_time
        college['id'] =p.id
        college['name'] =p.name
        college['path'] =p.path
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['status'] =p.status
        resList.append(college)   
    content = {
                'success': True,
                'message': '查询成功',
                'data':resList
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def info(request):  # request是必须带的实例。类似class下方法必须带self一样  
    query_dict = request.GET
    id = query_dict.get('id')  
    re=Images.objects.get(id=id)
    newre={}
    newre['createTime'] =re.create_time
    newre['id'] =re.id
    newre['name'] =re.name
    newre['path'] =re.path
    newre['reserve1'] =re.reserve1
    newre['reserve2'] =re.reserve2
    newre['reserve3'] =re.reserve3
    newre['reserve4'] =re.reserve4
    newre['reserve5'] =re.reserve5
    newre['status'] =re.status
    content = {
                'success': True,
                'message': '查询成功',
                'data':newre
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def delete(request):  # request是必须带的实例。类似class下方法必须带self一样  
    query_dict = request.GET
    id = query_dict.get('id')  
    re=Images.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Images.objects.create(create_time=now,name=jsonData['name'],path=jsonData['path'],reserve1=jsonData['reserve1'],reserve2=jsonData['reserve2'],reserve3=jsonData['reserve3'],reserve4=jsonData['reserve4'],reserve5=jsonData['reserve5'],status=jsonData['status'])#括号里面是表字段=值
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = Images.objects.get(id=jsonData['id'])
    try:
        if  jsonData['name']:
            re.name=jsonData['name']
        if  jsonData['path']:
            re.path=jsonData['path']
        if  jsonData['reserve1']:
            re.reserve1=jsonData['reserve1']
        if  jsonData['reserve2']:
            re.reserve2=jsonData['reserve2']
        if  jsonData['reserve3']:
            re.reserve3=jsonData['reserve3']
        if  jsonData['reserve4']:
            re.reserve4=jsonData['reserve4']
        if  jsonData['reserve5']:
            re.reserve5=jsonData['reserve5']
        if  jsonData['status']:
            re.status=jsonData['status']
    except Exception:
        print()
    re.save()
    content = {
                    'success': True,
                    'message': '修改成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def page(request):  # request是必须带的实例。类似class下方法必须带self一样   
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pagesize = data['pageSize']
    search = data['search']
    res1=[]
    if search:
        res1=Images.objects.filter(name=search)
    else:
        res1=Images.objects.filter()
        #Pagination
    total = res1.count()
    p = Paginator(res1, pagesize) # Show 10 contacts per page.
    page=[]
    try:
        page = p.page(pageNum)
    except PageNotAnInteger:
        page = p.page(pageNum)
    except EmptyPage:
        page = p.page(pageNum)
    resList=[]
    for p in page:
        college = {} 
        college['createTime'] =p.create_time
        college['id'] =p.id
        college['name'] =p.name
        college['path'] =p.path
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['status'] =p.status
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def upload(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("file", None)
        timestamp = time.time()        
        tuple_time = time.localtime(timestamp)
        newfile=time.strftime("%Y%m%d%H%M%S", tuple_time)
        filet=File.name
        index = filet.find(".")
        filetype=filet[index:len(filet)]
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            # 打开特定的文件进行二进制的写操作;
            with open("./static/%s" % newfile+filetype, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            content = {
                    'success': True,
                    'message': '上传成功',
                    'data':"http://localhost:8000/static/%s" % newfile+filetype               
                }
            return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
    else:
        content = {
                    'success': True,
                    'message': '上传失败'                
                }
        return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
