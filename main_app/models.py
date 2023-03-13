from django.db import models
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=300)
    created_on = models.DateField('created on')

    # add a meta class to sort each review by which date it was created on
    # potentially re-order by its rating
    class Meta:
        ordering = ['-created_on']
    
    def get_absolute_url(self):
        return reverse('edit_review', kwargs={'review_id': self.id})
    
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=300)
    last_name = forms.CharField(max_length=300)
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea, max_length=1000)
    
class AllCollections(models.Model):
    collection = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # give an image an url to be associated to
    # add a date to the collections
    # created_on = models.DateField('created on')
    def __str__(self):
        return self.collection
    # order by date
    # class Meta:
    #     ordering = ['-created_on']
    
class UploadPhoto(models.Model):
    url = models.CharField(max_length=200)
    # provide the photo an FK, to be associated with its collection
    collection = models.ForeignKey(AllCollections, on_delete=models.CASCADE)

    def __str__(self):
        return f'Saved to the {self.collection_id} @{self.url}'

