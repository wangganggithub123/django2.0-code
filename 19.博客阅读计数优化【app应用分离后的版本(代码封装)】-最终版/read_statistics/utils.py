from django.contrib.contenttypes.models import ContentType
from .models import ReadNum

def read_statistics_once_read(request,obj):
    ct=ContentType.objects.get_for_model(obj)
    key="%s_%s_read" % (ct.model,obj.pk)
    # 获取cookie：根据获取cookie的key值'blog_%s_readed' % blog_pk，判断是否存在，不存在则阅读数+1
    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct,object_id=obj.pk).count():
            # 记录存在,则查询并阅读数+1，保存
            readnum=ReadNum.objects.get(content_type=ct,object_id=obj.pk)
        else:
            # 对应记录不存在，则创建并阅读数+1，保存(这样就会在阅读数管理页面点击后保存对应文章以及阅读数)
            readnum=ReadNum(content_type=ct,object_id=obj.pk)
        readnum.read_num += 1    #点击该篇文章，阅读数自增1
        readnum.save()
    return key