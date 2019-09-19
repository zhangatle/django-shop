from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


# Create your views here.
class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

