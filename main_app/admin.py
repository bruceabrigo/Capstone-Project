from django.contrib import admin

from .models import Review, AllCollections, UploadPhoto
# Register your models here.
admin.site.register(Review)
admin.site.register(AllCollections)
admin.site.register(UploadPhoto)


