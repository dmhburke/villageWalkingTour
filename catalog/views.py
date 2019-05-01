from django.shortcuts import render

# Add models
#from catalog.models import

# Add forms


# Create your views here.
def agenda (request):
    """View function for agenda of site."""
    # Define views

    context = {}
    # Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'agenda.html', context=context)

def hotelchelsea (request):
    """View function for Hotel Chelsea"""
    # Define views

    context = {}
    # Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'hotelchelsea.html', context=context)

def washingtonsqpark (request):
    """View function for Washington Square Park"""
    # Define views

    context = {}
    # Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'washingtonsqpark.html', context=context)

def gerdes (request):
    """View function for Gerdes"""
    # Define views
    context = {}
# Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'gerdes.html', context=context)

def bleecker (request):
    """View function for Bleecker"""
    # Define views

    context = {}
# Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'bleecker.html', context=context)

def macdougal (request):
    """View function for MacDougal"""
    # Define views

    context = {}
# Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'macdougal.html', context=context)

def cafewha (request):
    """View function for CafeWha"""
    # Define views

    context = {}
    # Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'cafewha.html', context=context)

def jones (request):
    """View function for Jones St"""
    # Define views

    context = {}
    # Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'jones.html', context=context)
