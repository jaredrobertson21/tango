from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'aboutmessage': "This is the About page context variable"}
    return render(request, 'rango/about.html', context_dict)