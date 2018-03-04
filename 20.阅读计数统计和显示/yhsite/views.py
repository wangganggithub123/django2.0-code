from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data
from blog.models import Blog

def home(request):
    blog_content_type=ContentType.objects.get_for_model(Blog) #获取文件类型
    dates,read_nums=get_seven_days_read_data(blog_content_type)     #查询该文件类型下前7天的阅读数

    return render(request,'home.html',{'dates':dates,'read_nums':read_nums})