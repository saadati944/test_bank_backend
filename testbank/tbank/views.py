from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name="index"
    def get(self, request, **kwargs):
        return render(request, 'index.html')
