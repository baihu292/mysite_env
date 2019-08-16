from django.urls import path, re_path
from django.views.static import serve
from . import views
urlpatterns = [
        # path('index/', views.index),
        path('uploadFile/', views.uploadfile),
        re_path('bh/', views.wx_data),
        path('download/', views.download),
        # re_path('download/(?P<path>.*)$', serve, {'document_root': 'D:\\wxServer\\receive'})
]