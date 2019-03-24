from django.shortcuts import render
from project.models import Skill, Project
from django.shortcuts import render, get_object_or_404
import random

# Create your views here.
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