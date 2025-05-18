from django.urls import path

from . import views
from .views import NewsListAPIView

urlpatterns = [
    path('api/news/', NewsListAPIView.as_view(), name='news-list'),
    path('zoomit/news', views.zoomit_news_view, name='zoomit_news'),
]
