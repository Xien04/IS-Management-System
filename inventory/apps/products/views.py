from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm
from .models import Product

class ProductView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"
    paginated_by = 10

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "product"

class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/form.html"
    success_url = reverse_lazy("products:list")
    success_message = "Product created successfully"

class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/form.html"
    success_url = reverse_lazy("products:list")
    success_message = "Product updated successfully"

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "products/confirm_delete.html"
    success_url = reverse_lazy("products:list")
    context_object_url = "product"