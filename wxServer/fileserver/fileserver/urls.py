from django.urls import path, re_path, include
from django.contrib import admin
from django.views.static import serve
from . import views
urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        re_path('', include('app.urls')),  # 有api地址(app)
        path('', include('app.urls')),  # 有api地址(app)
        path('', include('app.urls')),  # 有api地址(app)
        path('api/', views.bg_api),       # 获取api
        path('uploadFile01/', views.uploadfile01),   # 没有api地址(app)
        path('bh01/', views.wx_data01),    # 没有api地址(app)
        # path('', views.download01),    # 没有api地址(app)
        re_path('download/(?P<path>.*)$', serve, {'document_root': 'D:\\wxServer\\receive'})
]