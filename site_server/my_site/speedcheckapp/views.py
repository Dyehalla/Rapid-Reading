from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class StartView(TemplateView):
    template_name = 'speedcheckapp/speed-check-start.html'


def test_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris luctus, leo non mollis lacinia, lorem ipsum convallis tortor, fermentum aliquet risus orci id arcu. Morbi ac gravida ipsum. Phasellus ultricies lacus nec accumsan hendrerit. Mauris ut nulla ac quam dapibus sagittis. Vivamus finibus felis a urna bibendum, eget congue nisi fermentum. Fusce efficitur ante neque, id accumsan lacus mattis lobortis. Morbi sed vulputate nisl. Nullam auctor vitae magna a porta. Quisque a pellentesque lacus. Nam dictum nisi purus, et egestas nisl pulvinar vestibulum. Integer sit amet metus arcu. Praesent vestibulum dui turpis, id blandit neque bibendum eu. Nunc pellentesque eget nisl a viverra. Donec eu dui vitae ante tristique posuere. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel sapien nisi Nullam a gravida arcu. Aenean molestie et tortor non rutrum. Suspendisse nec orci malesuada, imperdiet turpis a, gravida ante. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque porttitor finibus metus, quis cursus magna volutpat a. Nulla egestas in diam eu efficitur. Curabitur ut diam nulla. Nullam suscipit, elit ut ullamcorper blandit, ligula ligula tempor nisl, ac gravida mauris lorem non quam. Aliquam erat volutpat. Phasellus ultrices egestas arcu eu molestie.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nisi velit, rutrum eu auctor viverra, tristique eget nulla. Donec sagittis commodo libero, at maximus sapien varius imperdiet. Vivamus elit sapien, finibus vitae suscipit vitae, pretium ut tortor. Mauris eu auctor lorem, eget aliquet risus. Fusce pulvinar mollis ipsum sit amet tincidunt. Pellentesque vitae laoreet nibh, ut lobortis erat. Suspendisse non mi vitae odio condimentum imperdiet scelerisque ac est. Maecenas quis augue metus. Quisque vitae mauris lectus. Vivamus eget felis mauris. Sed a augue enim.'
        context = {
            'text': text,
        }
        request.session['words'] = len(text.split())
        return render(request, 'speedcheckapp/test.html', context=context)

    request.session['time'] = request.POST.get('time')
    return redirect('result')


class ResultView(TemplateView):
    template_name = 'speedcheckapp/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        time = self.request.session['time']
        words = self.request.session['words']
        if time:
            if len(time) < 3:
                context['minutes'] = 0
                context['seconds'] = int(time)
                context['words'] = words
                context['speed'] = round(int(words) / (int(time) / 60), 1)
            else:
                if len(time) == 3:
                    context['minutes'] = int(time[0])
                    context['seconds'] = int(time[1:])
                    context['speed'] = round(int(words) / ((int(time[0])) + int(time[1:]) / 60), 1)
                else:
                    context['minutes'] = int(time[:2])
                    context['seconds'] = int(time[2:])
                    context['speed'] = round(int(words) / (int(time[:2]) + int(time[2:]) / 60), 1)
                context['words'] = words
        return context

