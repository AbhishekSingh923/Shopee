from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Product
from .forms import ProductForm


# Create your views here.

class ProductUploadView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/upload_product.html'


    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)
    

    def get_success_url(self):
        return '/products/'


