from django.urls import path
from app.views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('gallery/', gallery_view, name='gallery'),
    path('testimonial/', testimonial_view, name='testimonial'),
]