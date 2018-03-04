from django.db import models
from django.db.models.fields import exceptions
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Blog_type(models.Model):
    type_name=models.CharField(max_length=15,verbose_name=u'分类名')

    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'标题')
    blog_type=models.ForeignKey(Blog_type,on_delete=models.DO_NOTHING)
    content=RichTextUploadingField()
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    created_time=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    last_update_time=models.DateTimeField(auto_now=True,verbose_name=u'修改时间')
    is_delete=models.BooleanField(default=False,verbose_name=u'是否删除')

    # 添加方法,添加的get_read_num方法，用于在admin管理后台的blog页面显示阅读数。即在admin.py的BlogAdmin类的list_display添加read_num
    def get_read_num(self):
        # 返回该篇文章的阅读数,此处如果该文章还没有阅读数，会有个异常，该异常是的默认阅读数不是0，而是-
        try:
            return self.readnum.read_num
        except exception.ObjectDoesNotExist:
            return 0

    class Meta:
        ordering=['-created_time']
        verbose_name='博客'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
    


class ReadNum(models.Model):
    read_num=models.IntegerField(default=0,verbose_name='阅读数')
    blog=models.OneToOneField(Blog,on_delete=models.DO_NOTHING,verbose_name='标题')

    class Meta:
        verbose_name='阅读数'
        verbose_name_plural=verbose_name

