from django.urls import path
from .views import dashboard, edit_link_view, delete_link_view,link_view

urlpatterns = [
    path('',dashboard, name='Dashboard'),
    path('edit/<int:id>', edit_link_view, name='edit'),
    path('delete/<int:id>', delete_link_view, name='delete'),
    path('<str:username>/', link_view, name='link_view'),
]
