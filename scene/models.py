#demo/api/models.py 
from django.db import models

 
class Scene(models.Model):
    #id可以不写，如果要设置，需申明AutoField(primary_key=True)
	create_time =  models.CharField(max_length=100)
	matchid = models.IntegerField()#比赛id
	name =  models.CharField(max_length=100)#场景名称
	reserve1 =  models.CharField(max_length=100)#拓扑图地址
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	user =  models.CharField(max_length=100)
	class Meta:
		db_table = 'scene'
		verbose_name = "Scene"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""