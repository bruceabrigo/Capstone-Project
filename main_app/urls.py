from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collections', views.collections, name='collections'),
    path('reviews', views.show_reviews, name='reviews'),
    path('reviews/<int:review_id>/', views.view_review, name='edit_review'),
    path('reviews/create/', views.PostReview.as_view(), name='create_review'),
    path('reviews/<int:pk>/update/', views.UpdateReview.as_view(), name='update_review'),
    path('reviews/<int:pk>/delete/', views.DeleteReview.as_view(), name='delete_review'),
    path('collections/portraits/', views.portraits_collection, name='portraits'),
    path('collections/prom/', views.prom_collection, name='prom'),
#   path('contact', views.contact, name='contact'),
]
