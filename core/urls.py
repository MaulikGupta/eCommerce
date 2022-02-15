from itertools import product
from django.urls import URLPattern, path
from .views import HomeView, checkout, ItemDetailView

app_name = 'core'

urlpatterns = [
    # path('', home, name='home_page'),
    path('', HomeView.as_view(), name='home_page'),
    path('checkout/', checkout, name='checkout_page'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product_page'),
]