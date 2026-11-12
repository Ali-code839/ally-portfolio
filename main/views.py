# Import Django form helpers for the contact form.
from django import forms

# Import Django's message system so the visitor receives feedback.
from django.contrib import messages

# Import Django's redirect and render shortcuts.
from django.shortcuts import redirect, render

# Import Django's email helper.
from django.core.mail import send_mail

# Import the portfolio Project model.
from portfolio.models import Project


# Define the fields visitors can complete on the contact page.
class ContactForm(forms.Form):

    # Ask for the visitor's name.
    name = forms.CharField(max_length=100, required=True)

    # Ask for a valid email address.
    email = forms.EmailField(required=True)

    # Ask for the project subject.
    subject = forms.CharField(max_length=200, required=True)

    # Ask for the project message.
    message = forms.CharField(widget=forms.Textarea, required=True)


# Render the homepage with the newest six portfolio projects.
def home(request):

    # Fetch projects newest first and limit the homepage to six cards.
    projects = Project.objects.all().order_by('-created_at', '-id')[:6]

    # Render the homepage with those projects.
    return render(request, 'home.html', {'projects': projects})


# Handle the contact form page and submitted messages.
def contact(request):

    # Check whether the visitor submitted the form.
    if request.method == 'POST':

        # Build a form object using the submitted data.
        form = ContactForm(request.POST)

        # Continue only when all fields are valid.
        if form.is_valid():

            # Get the visitor's information from the validated form.
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Create the email content that you will receive.
            email_message = f"""
You have received a new message from your portfolio website.

NAME:
{name}

EMAIL:
{email}

PROJECT:
{subject}

MESSAGE:
{message}
"""

            try:
                # Send the email to your Gmail address.
                send_mail(
                    subject=f'Portfolio Contact: {subject}',
                    message=email_message,

                    # Your Gmail address is the sender.
                    from_email='mpatially@gmail.com',

                    # Your Gmail address receives the message.
                    recipient_list=['mpatially@gmail.com'],

                    # Make Django report an error if sending fails.
                    fail_silently=False,
                )

                # Tell the visitor that the message was sent successfully.
                messages.success(
                    request,
                    'Thanks! Your message has been sent successfully.'
                )

            except Exception:

                # Show a safe error message without exposing technical details.
                messages.error(
                    request,
                    'Sorry, we could not send your message. Please try again later.'
                )

            # Return the visitor to the homepage.
            return redirect('main:home')

    else:

        # Create an empty form when the visitor first opens the page.
        form = ContactForm()

    # Render the contact page with the form.
    return render(request, 'contact.html', {'form': form})