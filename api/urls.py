from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

# api/v1/courses/   GET, POST
# api/v1/courses/1/   GET, DELETE
# api/v1/categories/   GET
# api/v1/categories/1/   GET

# for POST, DELETE add header
# Key : Authorization
# Value : ApiKey admin:699b50ab2952

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path('', include(api.urls), name='index'),
]
