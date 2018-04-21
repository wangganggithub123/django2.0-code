from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Comment


def update_comment(request):
    # 数据检查
    if not request.user.is_authenticated:
        return render(request,'error.html',{'message':'用户未登录，请登录后再做评论'})
    text = request.POST.get('text','').strip()
    if text == '':
        return render(request,'error.html',{'message':'评论内容不能为空，请输入内容后再提交评论'})
    try:
        content_type = request.POST.get('content_type','')
        object_id = int(request.POST.get('object_id',''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_object = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request,'error.html',{'message':'评论对象不存在'})

    # 检查通过，保存数据
    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_object
    comment.save()

    # 保存数据后返回当前页面
    referer = request.META.get('HTTP_REFERER',reverse('home'))
    return redirect(referer)
