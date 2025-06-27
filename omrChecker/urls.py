from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index,name="index"),
    path('upload_image/', views.upload_image,name="upload_image"),
    path('view/', views.view_image, name='view_image'),
    path('view/setPosition', views.setPosition, name='setPosition'),
    path('get_columnStudentOmr/', views.get_columnStudentOmr, name='get_columnStudentOmr'),
    path('get_columnAnswerKey/', views.get_columnAnswerKey, name='get_columnAnswerKey'),
    path('delDataBase/', views.delDataBase, name='delDataBase'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
