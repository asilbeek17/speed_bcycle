from django.forms.models import ModelFormMetaclass
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from django.views.generic.edit import BaseUpdateView

from app.form import *
from app.form import ProductModelForm
from app.models import *


# def index_view(request):
#     return render(request, 'index.html')

class IndexVIew(ListView):
    model = Product
    template_name = 'index.html'


def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

# def gallery_view(request):
#     return render(request, 'details.html')


class DetailView(DetailView):
    model = Product
    template_name = 'details.html'


def testimonial_view(request):
    return render(request, 'testimonial.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)


class UpdateBlogView(UpdateView):
    model = Product
    fields = ('title', 'image', 'text', 'price', 'quantitiy', 'category')
    template_name = 'CRUD/update.html'

# def update_product(request, product_pk):
#     category = Category.objects.all()
#     product = Product.objects.filter(id=product_pk).first()
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#         return redirect('index')
#
#     form = ProductModelForm(instance=product)
#     context = {
#         "form": form,
#         'categories': category
#     }
#     return render(request, 'CRUD/update.html', context)



class DeleteBlogView(DeleteView):
    model = Product
    template_name = 'CRUD/delete.html'
    success_url = reverse_lazy('index')


# class ContactPage(FormView):
#     template_name = 'contact.html'
#     success_url = reverse_lazy('index')
#     form_class = ContactForm

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)





