from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'source', 'created_at')


admin.site.register(News, NewsAdmin)
