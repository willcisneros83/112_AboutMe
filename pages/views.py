from django.views.generic import TemplateView

#oop object oriented programming

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutMeView(TemplateView):
    template_name = "about.html"
