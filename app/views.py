from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')


