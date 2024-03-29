"""django-shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from goods.views_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # 商品列表页
    path('goods/', GoodsListView.as_view(), name="goods-list"),
    path('docs/', include_docs_urls(title='mx'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
