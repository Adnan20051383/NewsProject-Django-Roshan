from django.contrib import admin

from news.models import News
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'source', 'tags',  'created_at')


admin.site.register(News, NewsAdmin)
