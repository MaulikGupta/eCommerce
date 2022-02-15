from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Item

# Create your views here.
class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'

# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'home-page.html', context)

def checkout(request):
    return render(request, 'checkout-page.html')
    
def product(request):
    return render(request, 'product-page.html')
