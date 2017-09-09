# Create your views here.
from django.http import HttpResponse

def welcome(request):
    response = HttpResponse("Welcome to Python/Django Programming World")
    return response

