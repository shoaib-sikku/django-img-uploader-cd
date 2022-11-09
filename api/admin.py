from django.contrib import admin
from api.models import ImageUploader
# Register your models here.

class ImageUploaderAdmin(admin.ModelAdmin):
    list_display = ('id','photo','date')

admin.site.register(ImageUploader,ImageUploaderAdmin)