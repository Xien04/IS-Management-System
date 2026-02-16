from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import InventoryItemForm
from .models import InventoryItem

class InventoryListView(LoginRequiredMixin, ListView):
    model = InventoryItem
    template_name = "inventory/list.html"
    context_object_name = "items"
    paginate_by = 10

class InventoryDetailView(LoginRequiredMixin, DetailView):
    model = InventoryItem
    template_name = "inventory/detail.html"
    context_object_name = "item"

class InventoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = InventoryItem
    template_name = "inventory/form.html"
    success_url = reverse_lazy("inventory:list")
    success_message = "Inventory item created successfully."

class InventoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InventoryItem
    template_name = "inventory/form.html"
    success_url = reverse_lazy("inventory:list")
    success_message = "Inventory Item udpated successfully."

class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = "inventory/confirm_delete.html"
    success_url = reverse_lazy("inventory:list")
    context_object_name = "item"