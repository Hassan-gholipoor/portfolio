from django.views.generic.list import ListView
from . import models


class Home(ListView):
    model = models.Personal
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['personal'] = models.Personal.objects.get(pk=1)
        context['skills'] = models.Skills.objects.all()
        context['social'] = models.SocialMedia.objects.get(pk=1)
        context['ed'] = models.Education.objects.all()
        context['ex'] = models.Experience.objects.all()
        return context