from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexVIew.as_view(), name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('detail/<int:pk>/', DetailView.as_view(), name='product_detail'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('create/', CreateBlogView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBlogView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteBlogView.as_view(), name='delete'),
]
