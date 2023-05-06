import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from match.models import Match
from matchuser.models import Matchuser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=Match.objects.filter().all()
    resList=[]
    for p in res:
        college = {}
        college['createTime'] =p.create_time
        college['id'] =p.id
        resuser=Matchuser.objects.filter(matchid=p.id).all()
        userlist=[]
        for user in resuser:
            usr={}
            usr['name']=user.name
            usr['status']=user.status
            userlist.append(usr)        
        college['users'] =userlist
        college['name'] =p.name
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
    re=Match.objects.get(id=id)
    newre={}
    newre['createTime'] =re.create_time
    newre['id'] =re.id
    newre['name'] =re.name
    newre['reserve1'] =re.reserve1
    newre['reserve2'] =re.reserve2
    newre['reserve3'] =re.reserve3
    newre['reserve4'] =re.reserve4
    newre['reserve5'] =re.reserve5
    newre['status'] =re.status
    users=Matchuser.objects.filter(matchid=id).all()
    resList=[]
    for p in users:
        college = {}
        college['name'] =p.name
        college['status'] =p.status        
        resList.append(college)   
    newre['users'] =resList
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
    Matchuser.objects.filter(matchid=id).delete()
    re=Match.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    match=Match.objects.create(create_time=now,name=jsonData['name'],reserve1=jsonData['reserve1'],reserve2=jsonData['reserve2'],reserve3=jsonData['reserve3'],reserve4=jsonData['reserve4'],reserve5=jsonData['reserve5'],status=jsonData['status'])#括号里面是表字段=值
    # for mu in jsonData['users']:
    #     Matchuser.objects.create(create_time=now,name=mu['name'],matchid=match.id,status=mu['status'])    
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = Match.objects.get(id=jsonData['id'])
    # Matchuser.objects.filter(matchid=jsonData['id']).delete()
    # now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # for mu in jsonData['users']:
    #     Matchuser.objects.create(create_time=now,name=mu['name'],matchid=jsonData['id'],status=mu['status'])
    try:
        if  jsonData['name']:
            re.name=jsonData['name']
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
        res1=Match.objects.filter(name=search)
    else:
        res1=Match.objects.filter()
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