from django.contrib import admin
from .models import Course
# Register your models here.
# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','price','image']
