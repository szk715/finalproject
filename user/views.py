import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from user.models import UserInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=UserInfo.objects.filter().all()
    resList=[]
    for p in res:
        college = {}  
        college['username'] =p.username
        college['password']=p.password
        college['type']=p.type
        college['id']=p.id
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
    re=UserInfo.objects.get(id=id)
    newre={}   
    newre['username'] =re.username
    newre['password']=re.password
    newre['type']=re.type
    newre['id']=re.id
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
    re=UserInfo.objects.get(id=id).delete()
   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def login(request):  # request是必须带的实例。类似class下方法必须带self一样    
    jsonData = json.loads(request.body.decode())
    res1=UserInfo.objects.filter(username=jsonData['username']).all()
    content={}
    if  len(res1)>0:
        res2=UserInfo.objects.filter(username=jsonData['username'],password=jsonData['password'])
        res3={
            "username":res1[0].username,
             "password":res1[0].password,
               "type":res1[0].type,
                 "id":res1[0].id,

        }
        if len(res2)>0:
            content = {
                    'success': True,
                    'message': '登录成功',
                    'data':res3
                }
        else:
            content = {
                    'success': False,
                    'message': '密码错误'
                }
    else:
        content = {
                    'success': False,
                    'message': '用户不存在'
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def save(request):  # request是必须带的实例。类似class下方法必须带self一样   
    jsonData = json.loads(request.body.decode())
    res1=UserInfo.objects.filter(username=jsonData['username'])
    if len(res1)>0:
        content = {
                'success': False,
                'message': '用户已存在',
                'data':jsonData
            }
    else:
        UserInfo.objects.create(username=jsonData['username'], type=jsonData['type'],password=jsonData['password'] )#括号里面是表字段=值
        content = {
                    'success': True,
                    'message': '注册成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def page(request):  # request是必须带的实例。类似class下方法必须带self一样   
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pagesize = data['pageSize']
    username = data['username']
    res1=[]
    if username:
        res1=UserInfo.objects.filter(username=username)
    else:
        res1=UserInfo.objects.filter()
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
        college['username'] =p.username
        college['password']=p.password
        college['type']=p.type
        college['id']=p.id
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    id=jsonData['id']
    re=UserInfo.objects.get(id=id)
    try:
        if  jsonData['username']:
            re.username=jsonData['username']
        if  jsonData['password']:
            re.password=jsonData['password']
        if  jsonData['type']:
            re.type=jsonData['type']        
    except Exception as e:
        print(e)
    re.save()
    content = {
                    'success': True,
                    'message': '修改成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')