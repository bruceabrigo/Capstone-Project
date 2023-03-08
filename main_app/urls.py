from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews', views.show_reviews, name='reviews'),
    path('reviews/<int:review_id>/', views.view_review, name='edit_review'),
    path('reviews/create/', views.PostReview.as_view(), name='create_review'),
#   path('contact', views.contact, name='contact'),
]
