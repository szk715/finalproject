#demo/api/models.py 
from django.db import models

 
class Images(models.Model):
    #id可以不写，如果要设置，需申明AutoField(primary_key=True)
	create_time =  models.CharField(max_length=100)
	name =  models.CharField(max_length=100)
	path =  models.CharField(max_length=100)#镜像地址
	reserve1 =  models.CharField(max_length=100)
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	class Meta:
		db_table = 'images'
		verbose_name = "Images"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""