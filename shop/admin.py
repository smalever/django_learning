from django.contrib import admin
from .models import Category, Course

admin.site.site_header = "Shop Admin"
admin.site.site_title = "Shop Admin Portal"
admin.site.index_title = "Welcome to Shop Portal"


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'id']


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'id']
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
