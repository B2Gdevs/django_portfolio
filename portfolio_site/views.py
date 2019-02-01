from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from project.models import Skill, Project
from portfolio_site.utils import format_email
from portfolio_site.forms import ContactForm
import random

import sendgrid
import os
from sendgrid.helpers.mail import *



def home(request):

    skills = Skill.objects
    projects = Project.objects


    context = {'skills':skills,
               'projects':projects}
               
    return render(request, 'base.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects
    
    # need to only keep a reference to 4 projects on the detail page
    if len(projects.all()) < 4:
        max_num = len(projects.all())
    else:
        max_num = 4
    project_indices = [random.randint(1, len(projects.all())) for i in range(max_num)] 
    
    projects = [get_object_or_404(Project, pk=i) for i in project_indices]
    context = {'project': project,
               'projects': projects}
    

    return render(request, 'detail.html', context)

    # Create your views here.
def contact(request):

    form = ContactForm(request.POST or None)

    context = {'form' : form}

    if form.is_valid():
        to = [settings.EMAIL_HOST_USER]
        body = format_email(form.cleaned_data['subject'], form.cleaned_data['email'], form.cleaned_data['message'])


        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email(form.cleaned_data['email'])
        subject = form.cleaned_data['subject']
        to_email = Email(settings.EMAIL_HOST_USER)
        content = Content("text/plain", body)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        
        # send_mail(form.cleaned_data['subject'], body, form.cleaned_data['email'],to)
        messages.success(request, "Thanks for contacting me! I will get in touch as quickly as I can.")

    return render(request, "contact.html", context)