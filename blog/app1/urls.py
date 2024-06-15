from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', blog_api),
    path('blogs/<int:pk>/', blog_details_api)
]