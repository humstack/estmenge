from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from smtplib import *
import os


from .forms import ContactForm

# Create your views here.
USERNAME = os.environ["RECIPIENT"]
PASSWORD = os.environ["RECIPIENT_PASSWORD"]
SMTP_HOST = os.environ["SMTP_HOST"]


def send_message(request, subject, sender, message):
    try:
        with SMTP(SMTP_HOST) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                msg=f"Subject: {subject}\n\n {message}\n My email is: {sender}",
                from_addr=sender,
                to_addrs=USERNAME
            )
    except SMTPException as smtpe:
        messages.error(
            request=request,
            message=f"An error occurred. Could not send the message. Please try again.\n\n{smtpe}"
        )
    except Exception as exc:
        messages.error(
            request=request,
            message=f"An error occurred. Could not send the message. Please try again.\n\n{exc}"
        )
    else:
        messages.success(request=request, message="Message sent successfully. Thank you")


def home(request):
    """Display an empty form and send email message"""
    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            send_message(request, request.POST["subject"], request.POST['email'], request.POST['message'])

            return HttpResponsePermanentRedirect("/")

    else:
        form = ContactForm()

    return render(request, "index.html", {'form': form})
