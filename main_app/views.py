from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Review
# views.py

# Add this cats list below the imports

# Create your views here.
def home(request): # home page view
    return render(request, 'home.html')

def show_reviews(request): # show an index of all the reviews
    reviews = Review.objects.all() # reviews will make a query for all reviews to be rendered to the index
    return render(request, 'reviews/index.html', {
        'reviews': reviews
    })

def view_review(request, review_id): # this will show a details page of ONE review
    review = Review.objects.get(id=review_id) # review, is equal to the id of one review, based on the reviews id, in which was included reviews query, and looped into separate reviews with their id's
    return render(request, 'reviews/view_review.html', {
        'review': review
    })

class PostReview(CreateView):
    model = Review
    fields = '__all__'

    success_url = '/reviews'

class UpdateReview(UpdateView):
    # I only want users to be able change the note
    model = Review
    fields = ['note']

class DeleteReview(DeleteView):
    model = Review
    success_url = '/reviews'