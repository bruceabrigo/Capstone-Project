from django.shortcuts import render
from .models import Review
# views.py

# Add this cats list below the imports

# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.html', {
        'reviews': reviews
    })