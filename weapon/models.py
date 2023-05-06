#demo/api/models.py 
from django.db import models

 
class Weapon(models.Model):#靶机
    #id可以不写，如果要设置，需申明AutoField(primary_key=True)
	create_time =  models.CharField(max_length=100)
	name =  models.CharField(max_length=100)#数据库名
	reserve1 =  models.CharField(max_length=100)#数据端口
	reserve2 =  models.CharField(max_length=100)#地址
	reserve3 =  models.CharField(max_length=100)#数据库用户名
	reserve4 =  models.CharField(max_length=100)#数据库密码
	reserve5 =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	class Meta:
		db_table = 'weapon'
		verbose_name = "weapon"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""