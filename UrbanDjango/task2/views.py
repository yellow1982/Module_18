from django.shortcuts import render
from django.views.generic import TemplateView

def func_temp(request):
    return render(request, 'func_template.html')

class class_temp(TemplateView):
    template_name = 'class_template.html'
