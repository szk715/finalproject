#demo/api/models.py 
from django.db import models

 
class Match(models.Model):
    #id可以不写，如果要设置，需申明AutoField(primary_key=True)
	create_time =  models.CharField(max_length=100)
	name =  models.CharField(max_length=100)
	reserve1 =  models.CharField(max_length=100)#拓扑图地址
	reserve2 =  models.CharField(max_length=100)#裁判
	reserve3 =  models.CharField(max_length=100)#场景
	reserve4 =  models.CharField(max_length=100)#靶机id
	reserve5 =  models.CharField(max_length=100)#状态
	status =  models.CharField(max_length=100)
	class Meta:
		db_table = 'match'
		verbose_name = "Match"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""