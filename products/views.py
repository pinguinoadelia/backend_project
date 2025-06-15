# products/views.py
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['disable_add'] = True
        return ctx

