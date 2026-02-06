from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import SupplierForm
from .models import Supplier
# Create your views here.

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = "suppliers/list.html"
    context_object_name = "suppliers"
    paginate_by = 10

class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = "suppliers/detail.html"
    context_object_name = "supplier"

class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/form.html"
    success_url = reverse_lazy("suppliers:list")
    success_message = "Supplier created successfully"

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = "suppliers/confirm_delete.html"
    success_url = reverse_lazy("suppliers:list")
    context_object_name = "supplier"