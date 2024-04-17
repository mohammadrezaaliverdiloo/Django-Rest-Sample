from django.contrib.auth import get_user_model
from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm 
from .views import Signup
from .views import HomePageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
        
class SignupPageTests(TestCase):
    
    username= "newuser"
    email= "newuser@gmail.com"
    
    def SetUp(self):
        url= reverse("account_signup")
        self.response= self.client.get(url)
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,"account/signup.html")
        self.assertContains(self.response,"Sign Up")
        self.assertNotContains(self.response,"Not true")
        
    def test_signup_form(self):
        new_user= get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)
        
    
    
    
    
    
# class CustomUserTests(TestCase):
    def setUp(self) -> None:
        url= reverse("signup")
        self.response= self.client.get(url)
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,"registration/signup.html")
        self.assertContains(self.response,"Sign Up")
        self.assertNotContains(self.response,"go out")
        
    def test_signup_form(self):
        form= self.response.context.get("form")
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,"csrfmiddlewaretoken")
        
    def test_signup_view(self):
        view= resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__,Signup.as_view().__name__)
        
        
        
        
# @classmethod
# def setUpTestData(cls):
# cls.user = get_user_model().objects.create_user(
# username="reviewuser",
# email="reviewuser@email.com",
# password="testpass123"
# )
# cls.special_permission = Permission.objects.get(
# codename="special_status"
# ) # new
# cls.book = Book.objects.create(
# title="Harry Potter",
# author="JK Rowling",
# price="25.00",
# )
# cls.review = Review.objects.create(
# book = cls.book,
# author = cls.user,
# review = "An excellent review",
# )
# def test_book_listing(self):
# self.assertEqual(f"{self.book.title}", "Harry Potter")
# self.assertEqual(f"{self.book.author}", "JK Rowling")
# self.assertEqual(f"{self.book.price}", "25.00")
# def test_book_list_view_for_logged_in_user(self): # new
# self.client.login(email="reviewuser@email.com", password="testpass123")
# response = self.client.get(reverse("book_list"))
# self.assertEqual(response.status_code, 200)
# self.assertContains(response, "Harry Potter")
# self.assertTemplateUsed(response, "books/book_list.html")
# def test_book_list_view_for_logged_out_user(self): # new
# self.client.logout()
# response = self.client.get(reverse("book_list"))
# self.assertEqual(response.status_code, 302) # new
# self.assertRedirects(
# response, "%s?next=/books/" % (reverse("account_login")))
# response = self.client.get(
# "%s?next=/books/" % (reverse("account_login")))
# self.assertContains(response, "Log In")
# def test_book_detail_view_with_permissions(self): # new
# self.client.login(email="reviewuser@email.com", password="testpass123")
# self.user.user_permissions.add(self.special_permission)
# response = self.client.get(self.book.get_absolute_url())
# no_response = self.client.get("/books/12345/")
# self.assertEqual(response.status_code, 200)
# self.assertEqual(no_response.status_code, 404)
# self.assertContains(response, "Harry Potter")
# self.assertContains(response, "An excellent review")
# self.assertTemplateUsed(response, "books/book_detail.html")