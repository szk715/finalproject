#demo/api/models.py
 
from django.db import models

 
class UserInfo(models.Model):
    #id可以不写，如果要设置，需申明AutoField(primary_key=True)
    username = models.CharField(max_length=20,blank=True,null=False,verbose_name='姓名')
    password = models.CharField(max_length=20,blank=True,null=False,verbose_name='密码')
    type = models.IntegerField() 
    class Meta:
        db_table = 'user_info'
        verbose_name = "用户模块"
        verbose_name_plural = verbose_name
 
    def __str__(self):
        # 重写直接输出类的方法
        return self.username
