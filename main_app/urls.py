from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews', views.show_reviews, name='reviews'),
#   path('collections', views.collections, name='collections'),
#   path('contact', views.contact, name='contact'),
]
