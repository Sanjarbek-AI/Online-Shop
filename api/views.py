from rest_framework.generics import ListAPIView

from api.serializers import NewsModelSerializer
from home.models import NewsModel


class NewsListAPIView(ListAPIView):
    serializer_class = NewsModelSerializer
    queryset = NewsModel.objects.all()
