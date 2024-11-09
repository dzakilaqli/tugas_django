from django.urls import path, include
from clientbook_app import views

urlpatterns = [
    path('', views.pelanggan, name='pelanggan'),
]
