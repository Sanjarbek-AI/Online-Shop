from django.urls import path

from api.views import NewsListAPIView

app_name = 'api'

urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='news'),
]
