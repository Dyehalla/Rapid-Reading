from django.shortcuts import render
from django.views.generic import TemplateView

from speedcheckapp.models import Result


class HomePage(TemplateView):
    template_name = 'app/main-page.html'


def my_results_view(request):
    context = {
        'results': Result.objects.filter(user_profile=request.user.profile)
    }
    return render(request, 'app/profile-results.html', context=context)
