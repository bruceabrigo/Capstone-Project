from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)

    # add a meta class to sort each review by which date it was created on
    # potentially re-order by its rating
    class Meta:
        ordering = ['created_on']