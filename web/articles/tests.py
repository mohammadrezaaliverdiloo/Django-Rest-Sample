from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from .models import Book
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title= "Harry Potter",
            content= "JK Roppppppppppwling",
            date= datetime.now(),
    )
    def test_article_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.content}", "JK Roppppppppppwling")
        self.assertEqual(f"{self.book.date}", datetime.now())

    def test_article_list_view(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response,"article/article_list.html")

    def test_article_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/p/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "article/article_detail.html")