from django.views.generic.base import TemplateView


class PagesView(TemplateView):
    template_name= "home.html"
