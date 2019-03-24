"""
Views for rendering html and performing actions on data passed to the app.

Author: Benjamin Garrard
"""
from django.shortcuts import render


def nba_view(request):
    """
    Render the NBA prediction html.

    Parameters
    ----------
    request : request
        The request received from the client.  

    Returns
    -------
    render
        The rendered page with any information passed to it through django.

    """
    context = {}
    return render(request, 'nba_prediction.html', context)