from django.shortcuts import render, redirect
from .models import Contact

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('/')

    return render(request, 'main/index.html')