from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

from .forms import ContactForm

def contact(request):
    """ A view to return the contact page and form """

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        send_mail(
            message_name,
            message_email,
            message_subject,
            message,

            ['roxannejade853@gmail.com']
        )

        return render(request, 'contact.html')
