#demo/api/models.py 
from django.db import models

 
class Matchuser(models.Model):
    #id可以不写，如果要设置，需申明AutoField(primary_key=True)
	create_time =  models.CharField(max_length=100)
	matchid = models.IntegerField()#比赛id
	name =  models.CharField(max_length=100)#用户账号
	reserve1 =  models.CharField(max_length=100)#比赛结果
	reserve2 =  models.CharField(max_length=100)#参赛者类型
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)#分数
	reserve5 =  models.CharField(max_length=100)#判罚
	status =  models.CharField(max_length=100)#用户类型
	class Meta:
		db_table = 'matchuser'
		verbose_name = "Matchuser"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""