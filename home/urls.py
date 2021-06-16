from django.urls import path

from home.views import HomeTemplateView, ContactCreateView, NewsListView, NewsDetailView

app_name = 'home'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='detail'),
]
