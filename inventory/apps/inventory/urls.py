from django.urls import path

from . import views

app_name = "inventory"

urlpatters = [
    path("", views.InventoryListView.as_view(), name="list"),
    path("create/", views.InventoryCreateView.as_view(), name="create"),
    path("<int:pk>/", views.InventoryDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.InventoryUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.InventoryDeleteView.as_view(), name="delete"),
]