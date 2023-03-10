from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Review, AllCollections, UploadPhoto, ContactForm
import os
import uuid
import boto3
from django.conf import settings
# for contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

AWS_ACCESS_KEY = settings.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
S3_BUCKET = settings.S3_BUCKET
S3_BASE_URL = settings.S3_BASE_URL

def photos(request):
    secret_key = os.environ['SECRET_KEY']
# views.py

# Create your views here.
def home(request): # home page view
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home')
      
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# ----------------- Debugging -----------------
def collections(request):
    collections = AllCollections.objects.all()
    covers = AllCollections.objects.all()[1:2]
    return render(request, 'collections.html', {'collections': collections, 'covers': covers})
# ----------------- Debugging -----------------


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

# create individual portrait reviews
# each collection is to render all photos in that collections one-to-many relationship
def portraits_collection(request, collection_id):
    collection = AllCollections.objects.get(id=collection_id)
    return render(request, 'collections/portaits.html', {'collection': collection})

def prom_collection(request, collection_id):
    collection = AllCollections.objects.get(id=collection_id)
    return render(request, 'collections/portaits.html', {'collection': collection})

# create a custom function to upload an image to AWS
def upload_photo(request, collection_id):
    photo_file = request.FILES.get('photo-file', None)

    if photo_file:
        # if present, we'll use this to create  a ref to the boto3
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        # CREATE A UNIQUE KEY FOR OUR PHOTOS
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # we're going to use try... except which is like try...catch in js
        # to handle the situation if anything should go wrong
        try:
            # if success
            s3.upload_fileobj(photo_file, S3_BUCKET, key)
            # build the full url setting to upload s3
            url = f'{S3_BASE_URL}{S3_BUCKET}/{key}'
            # if our upload(that used boto3) was succesful
            # we want to use that photo locations to create a Photo model
            photo = UploadPhoto(url=url, collection_id=collection_id)
            # save the instance to the database
            photo.save()
        # except is our catch
        except Exception as error:
            # pring an error message
            print('Error uploading image', error)
            return redirect('collections')
    return redirect('collections')



