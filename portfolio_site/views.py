from django.shortcuts import render, get_object_or_404
# from django.core.mail import send_mail
# from django.contrib import messages
# from django.conf import settings
# from portfolio_site.utils import format_email
from project.models import Skill, Project
from portfolio_site.forms import ContactForm
import random

# import sendgrid
# import os
# from sendgrid.helpers.mail import Content, Email, Mail


def home(request):
    """
    home() gathers skills and projects to be displayed on the homepage.

    This method renders the homepage using the base.html template and
    injects the skills and projects that are stored within the database into
    the template.

    Parameters
    ----------
    request : Request
        Request is the request made to the web server such as POST, GET, and
        etc.

    Returns
    -------
    render : render
        Render is the object that renders the html, injects the data, and
        displays everything to the user.
    """
    skills = Skill.objects
    projects = Project.objects

    context = {'skills': skills,
               'projects': projects}

    return render(request, 'base.html', context)


def detail(request, project_id):
    """
    detail() renders the detail page with data from the projects model.

    This method finds the project objects within the database and randomly
    selects a 4 of them to be displayed on the detail page.

    Parameters
    ----------
    request : Request
        Request is the request made to the web server such as POST, GET, and
        etc.

    Returns
    -------
    render : render
        Render is the object that renders the html, injects the data, and
        displays everything to the user
    """
    project = get_object_or_404(Project, pk=project_id)
    projects = Project.objects

    # need to only keep a reference to 4 projects on the detail page
    if len(projects.all()) < 4:
        max_num = len(projects.all())
    else:
        max_num = 4

    project_indices = []

    for i in range(max_num):
        num = random.randint(1, len(projects.all()))
        while num in project_indices:
            num = random.randint(1, len(projects.all()))

        project_indices.append(num)

    projects = [get_object_or_404(Project, pk=i) for i in project_indices]
    context = {'project': project,
               'projects': projects}

    return render(request, 'detail.html', context)


def contact(request):
    """
    contact() is used to display and gather the contact information of users.

    This method creates the form that is used in the contact.html page
    and gathers the content from the form and puts that in to the database.

    Parameters
    ----------
    request : Request
        Request is the request made to the web server such as POST, GET, and
        etc.

    Returns
    -------
    render : render
        Render is the object that renders the html, injects the form, and
        displays everything to the user
    """
    form = ContactForm(request.POST or None)

    context = {'form': form}

    if form.is_valid():
        pass
        # to = [settings.EMAIL_HOST_USER]
        # body = format_email(form.cleaned_data['subject'],
        #                     form.cleaned_data['email'],
        #                     form.cleaned_data['message'])

        # sg = sendgrid.SendGridAPIClient(
        #     apikey=os.environ.get("SENDGRID_API_KEY"))
        # from_email = Email(form.cleaned_data['email'])
        # subject = form.cleaned_data['subject']
        # to_email = Email(settings.EMAIL_HOST_USER)
        # content = Content("text/plain", body)
        # mail = Mail(from_email, subject, to_email, content)
        # # response = sg.client.mail.send.post(request_body=mail.get())
        # # send_mail(form.cleaned_data['subject'], body, form.cleaned_data['email'],to)
        # messages.success(request, "Thanks for contacting me! I will get in touch as quickly as I can.")

    return render(request, "contact.html", context)