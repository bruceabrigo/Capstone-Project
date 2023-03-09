from django.db import models
from django.urls import reverse

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
    
class AllCollections(models.Model):
    # add a date to the collections
    created_on = models.DateField('created on')

    class Meta:
        ordering = ['-created_on']