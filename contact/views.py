from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page and form """

    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has sent, \
                we'll get back to you shortly.")
        else:
            messages.error(request, "Sorry, your message did not send this time, \
                please try again.")

        return redirect(reverse('contact'))
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
