from celery import shared_task
from .utils import scrape_zoomit_news
from .models import News

@shared_task
def fetch_and_save_zoomit_news():
    news_list = scrape_zoomit_news()

    for item in news_list:
        if not News.objects.filter(title=item["title"]).exists():
            News.objects.create(
                title=item["title"],
                content=item["content"],
                tags=",".join(item["tags"]),
                source=item["source"]
            )