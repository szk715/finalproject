import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from myweapon.models import Myweapon
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import pymysql
from weapon.models import Weapon
from match.models import Match
from matchuser.models import Matchuser
def list(request):  # request是必须带的实例。类似class下方法必须带self一样  
    res=Myweapon.objects.filter().all()
    resList=[]
    for p in res:
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
        college['user'] =p.user
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
    re=Myweapon.objects.get(id=id)
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
    newre['user'] =re.user
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
    re=Myweapon.objects.get(id=id).delete()   
    content = {
                'success': True,
                'message': '删除成功',             
            }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def fire(request):
    query_dict = request.GET
    id = query_dict.get('id')
    user = query_dict.get('user')  
    weaponid= query_dict.get('weaponid') 
    res1=Match.objects.get(id=id)
    re=Weapon.objects.get(id=res1.reserve4)
    res2=Myweapon.objects.get(id=weaponid)
    msg=''
    try:
        conn = pymysql.connect(host=re.reserve2,user=re.reserve3,password=re.reserve4,port=int(re.reserve1),database=re.name)#创建数据库连接
        cursor = conn.cursor()#创建游标
        sql=res2.reserve2#要执行的sql语句
        result=cursor.execute(sql)#提交sql语句       
        conn.commit()#提交缓存
        cursor.close()#关闭游标
        conn.close()#关闭数据库连接
        msg=str(result)
    except Exception as e:
        print(e)
        msg='攻击失败'
    content = {
                    'success': True,
                    'message': msg,
                    'data':msg
                }
    mu=Matchuser.objects.get(name=user,matchid=int(id))
    mu.reserve1=msg
    mu.reserve2='攻击成功'
    mu.save()
    mated=Matchuser.objects.filter(matchid=id,reserve2='攻击成功')
    if(len(mated)==2):
        res1.reserve5="end"
        res1.save()

    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def defense(request):
    query_dict = request.GET
    id = query_dict.get('id')
    user = query_dict.get('user')  
    weaponid= query_dict.get('weaponid') 
    res1=Match.objects.get(id=id)
    re=Weapon.objects.get(id=res1.reserve4)
    res2=Myweapon.objects.get(id=weaponid)
    msg=''
    try:
        conn = pymysql.connect(host=re.reserve2,user=re.reserve3,password=re.reserve4,port=int(re.reserve1),database=re.name)#创建数据库连接
        cursor = conn.cursor()#创建游标       
        sql=res2.reserve2#要执行的sql语句
        # result=cursor.execute(hash(sql))#提交sql语句
        cursor.execute(sql) 
        result=cursor.fetchall()
        conn.commit()#提交缓存
        cursor.close()#关闭游标
        conn.close()#关闭数据库连接
        res12=[]
        for row in result:
            name = row[0]
            age = row[1]
            res12.append(hash(f"name: {name}, age: {age}"))           
        msg=res12
    except Exception as e:
        msg='防御失败'
    content = {
                    'success': True,
                    'message': msg,
                    'data':msg
                }
    mu=Matchuser.objects.get(name=user,matchid=id)
    mu.reserve1=msg
    mu.reserve2='1'
    mu.save()
    mated=Matchuser.objects.filter(matchid=id,reserve2='1').all()
    if(len(mated)==2):
        res1.reserve5="end"
        res1.save()
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Myweapon.objects.create(create_time=now,name=jsonData['name'],reserve1=jsonData['reserve1'],reserve2=jsonData['reserve2'],reserve3=jsonData['reserve3'],reserve4=jsonData['reserve4'],reserve5=jsonData['reserve5'],status=jsonData['status'],user=jsonData['user'])#括号里面是表字段=值
    content = {
                    'success': True,
                    'message': '新增成功',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = Myweapon.objects.get(id=jsonData['id'])
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
        if  jsonData['user']:
            re.user=jsonData['user']
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
        res1=Myweapon.objects.filter(name=search)
    else:
        res1=Myweapon.objects.filter()
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
        college['user'] =p.user
        resList.append(college)        
    content = {
                    'success': True,
                    'message': '查询成功',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')