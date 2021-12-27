from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("This is the about page!")

def contact(request):
    return HttpResponse("This is the contact page!")

def show_age(request, age):
    return HttpResponse("My age is {}".format(age))

def even_or_odd(request, odd_or_even):
    if odd_or_even%2 == 0:
        return HttpResponse("The number you passed is even: %s" %odd_or_even)
    else:
        return HttpResponse("The number you passed is odd: %s" %odd_or_even)

def books(request):
    favourite_books = {
        'Ajibola': 'This is Ajibola books',
        'Ridwan': 'This is Ridwan books',
        'Olaide': 'This is Olaide books'
    }
    
    return render(request, 'first_app/index.html', context=favourite_books)
