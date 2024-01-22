# views.py
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import EmailForm

def index(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            C_User = form.cleaned_data['C_User']
            from_email = 'tanweerahmedzop5@gmail.com'
            recipient_list = ['postskaka@gmail.com']

            # Render the email template
            email_content = render_to_string('email_template.html', {'subject': subject, 'message': message, 'C_User': C_User})

            send_mail(subject, email_content, from_email, recipient_list, html_message=email_content)

            return render(request, 'email_sent.html')
    else:
        form = EmailForm()

    return render(request, 'email_form.html', {'form': form})
