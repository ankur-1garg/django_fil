from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.forms import contactForm


def home(request):
    print(request.POST)
    return render(request, 'homeboy.html')


def contact(request):
    """
    Handle the contact form submission.
    If the request method is POST, validate the form data and print the cleaned data.
    If the form is not valid or the request method is not POST, render an empty form.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered contact form page.
    """
    # form = contactForm()
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, email, message)

    else:
        form = contactForm()
    print(request.POST)

    return render(request, 'contactapp.html', {contact: form})
