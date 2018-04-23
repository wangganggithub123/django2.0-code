from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from yhsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),   #富文本上传图片
    path('', views.home,name='home'),
    path('blog/',include('blog.urls')),
    path('comment/',include('comment.urls')),
    path('login/',views.user_login,name='login'),
    path('register/', views.register, name='register'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
