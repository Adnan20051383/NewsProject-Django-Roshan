from django.http import JsonResponse
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.db.models import Q

from .utils import scrape_zoomit_news


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.query_params.getlist('tag')
        include_keywords = self.request.query_params.getlist('include')
        exclude_keywords = self.request.query_params.getlist('exclude')

        # filter tags
        if tags:
            for tag in tags:
                queryset = queryset.filter(tags__icontains=tag)

        # filter include kw
        if include_keywords:
            include_q = Q()
            for keyword in include_keywords:
                include_q |= Q(content__icontains=keyword) | Q(title__icontains=keyword)
            queryset = queryset.filter(include_q)

        # filter exclude kw
        if exclude_keywords:
            for keyword in exclude_keywords:
                queryset = queryset.exclude(content__icontains=keyword).exclude(title__icontains=keyword)

        return queryset


def zoomit_news_view(request):
    news_list = scrape_zoomit_news()

    # Get query params
    tags = request.GET.getlist('tag')
    include_keywords = request.GET.getlist('include')
    exclude_keywords = request.GET.getlist('exclude')

    # Filter tags
    if tags:
        news_list = [
            news for news in news_list
            if any(tag in news.get('tags', []) for tag in tags)
        ]

    # Filter include kw
    if include_keywords:
        news_list = [
            news for news in news_list
            if any(
                kw.lower() in news.get('title', '').lower() or
                kw.lower() in news.get('content', '').lower()
                for kw in include_keywords
            )
        ]

    # Filter exclude kw
    if exclude_keywords:
        news_list = [
            news for news in news_list
            if all(
                kw.lower() not in news.get('title', '').lower() and
                kw.lower() not in news.get('content', '').lower()
                for kw in exclude_keywords
            )
        ]

    return JsonResponse(news_list, safe=False, json_dumps_params={'ensure_ascii': False})
