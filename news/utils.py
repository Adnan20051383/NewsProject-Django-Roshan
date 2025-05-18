# news/utils.py

import requests
from bs4 import BeautifulSoup

from news.models import News


def scrape_zoomit_news():
    url = "https://www.zoomit.ir"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Could not fetch Zoomit"}

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("a.fNLyDV")

    news_list = []
    for article in articles[:5]:  # limit to first 10
        link = article.get("href")
        if not link.startswith("http"):
            link = "https://www.zoomit.ir" + link

        article_resp = requests.get(link)
        if article_resp.status_code != 200:
            continue

        article_soup = BeautifulSoup(article_resp.text, "html.parser")
        print(article_soup)
        title = article_soup.select_one("h1").text.strip() if article_soup.select_one("h1") else ""
        paragraphs = article_soup.select("p.joXpaW")
        content = " ".join([p.get_text(strip=True) for p in paragraphs])
        tags = [tag.get_text(strip=True) for tag in article_soup.select("span.NawFH")]

        news = News.objects.create(
            title=title,
            content=content,
            tags=tags,
            source="Zoomit.ir"
        )


        news_list.append({
            "title": title,
            "content": content,
            "tags": tags,
            "source": "Zoomit.ir",
            "url": link
        })

    return news_list
