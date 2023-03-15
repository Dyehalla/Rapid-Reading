from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'app/main-page.html'

