from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = "home.html"
    
    
class Signup(LoginRequiredMixin,CreateView):
    form_class= CustomUserCreationForm
    success_url= reverse_lazy("login")
    template_name= "registration/signup.html"
    
    
