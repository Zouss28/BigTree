from django.urls import path
from .views import profile_page_view

urlpatterns = [
    path('',profile_page_view, name='profile')
]
