from django.db import models
from datetime import datetime

# 分类
class Category(models.Model):
    photos_name = models.CharField(max_length=100,null=False, blank=False,verbose_name='图片名称')

    def __str__(self):
        return self.photos_name

    class Meta:
        db_table = 'photos_category'

# 图片
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,verbose_name='类别关联')
    image = models.ImageField(upload_to='images/',null=False,blank=False, verbose_name='上传图片')
    # 图片描述
    description = models.TextField(max_length=500,null=True, blank=True,verbose_name='图片描述')
    date_time = models.DateTimeField(default=datetime.now(), verbose_name='创建日期')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'photos_photo'