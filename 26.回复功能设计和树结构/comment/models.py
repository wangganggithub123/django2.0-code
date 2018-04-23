from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    user = models.ForeignKey(User,related_name='comments',on_delete=models.DO_NOTHING,verbose_name='评论者')

    root = models.ForeignKey('self',null=True,related_name='root_comment',on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self',null=True,related_name='parent_comment',on_delete=models.DO_NOTHING)
    reply_to = models.ForeignKey(User,related_name='replies',null='True',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-comment_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name



