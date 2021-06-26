from django.shortcuts import render
from newsletter.forms import EmailSignupForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    form = EmailSignupForm()

    context = {
        'form': form,
    }

    return render(request, 'home/index.html', context)
