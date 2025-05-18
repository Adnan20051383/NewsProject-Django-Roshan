from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.db.models import Q


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
