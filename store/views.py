from .models import *
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template

def home(request):
    configTable = globalConfig.objects.all()
    if configTable:
        config = configTable[0]
    else:
        config=[]
    all_product_list = Product.objects.all()
    template = get_template('store/home.html')
    context = {
        'all_product_list': all_product_list,
        'config': config,
    }
    return HttpResponse(template.render(context, request))