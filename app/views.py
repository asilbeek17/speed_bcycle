from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from app.form import *
from app.form import ProductModelForm
from app.models import *


# def index_view(request):
#     return render(request, 'index.html')

class IndexVIew(ListView):
    Product.objects.order_by('price')
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_queryset(self):
        title = self.request.GET.get('title')
        if title:
            return Product.objects.filter(title__icontains=title)
        return Product.objects.all()


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    form = ContactForm

    if request.method == "POST":
        phone = request.POST['phone']
        message = request.POST['message']

        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    else:
        return render(request, 'contact.html')


# def gallery_view(request):
#     return render(request, 'details.html')


class DetailView(DetailView):
    model = Product
    template_name = 'details.html'


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


class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Product
    fields = ('title', 'text', 'price', 'quantitiy', 'category', 'image', 'image2', 'image3')
    template_name = 'CRUD/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'CRUD/delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'CRUD/create.html'
    fields = ('title', 'text', 'price', 'quantitiy', 'category', 'image', 'image2', 'image3')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class ContactPage(LoginRequiredMixin, FormView):
#     template_name = 'contact.html'
#     success_url = reverse_lazy("index")
#     form_class = ContactForm
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.save()
#         return super().form_valid(form)





