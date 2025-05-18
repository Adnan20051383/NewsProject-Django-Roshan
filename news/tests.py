from rest_framework.test import APITestCase
from django.urls import reverse

from news.models import News


class NewsAPITestCase(APITestCase):

    def setUp(self):

        News.objects.create(
            title='First News',
            content='This article is about the economy and real facts.',
            tags='business,rumor'
        )
        News.objects.create(
            title='Second News',
            content='This article is about football and the sports industry.',
            tags='sports'
        )
        News.objects.create(
            title='Third News',
            content='This is a fake news article.',
            tags='misc,rumor'
        )

    def print_json(self, response, title):
        print(f"\n--- {title} ---")
        print(f"Response status: {response.status_code}")
        print("JSON Output:")
        print(response.json())

    def test_list_all_news(self):
        url = reverse('news-list')
        response = self.client.get(url)
        self.print_json(response, "Test: List All News")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_filter_by_tag(self):
        url = reverse('news-list')
        response = self.client.get(url, {'tag': 'sports'})
        self.print_json(response, "Test: Filter by Tag 'sports'")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Second News')

    def test_filter_by_included_keyword(self):
        url = reverse('news-list')
        response = self.client.get(url, {'include': 'football'})
        self.print_json(response, "Test: Filter by Included Keyword 'football'")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Second News')

    def test_filter_by_excluded_keyword(self):
        url = reverse('news-list')
        response = self.client.get(url, {'exclude': 'fake'})
        self.print_json(response, "Test: Filter by Excluded Keyword 'fake'")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_combined_include_and_exclude(self):
        url = reverse('news-list')
        response = self.client.get(url, {'include': 'economy', 'exclude': 'fake'})
        self.print_json(response, "Test: Include 'economy' and Exclude 'fake'")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'First News')
