"""
Views for rendering html and performing actions on data passed to the app.

python 3.7 is used.  This is a dependency that must be known for pickle.

Author: Benjamin Garrard
"""
from django.shortcuts import render
from predictions import utils


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
    result = None
    display_result = False
    team = None
    op_team = None
    quarter = None
    if request.method == "POST":
        team = request.POST.get("team")
        op_team = request.POST.get("opposing_team")
        quarter = request.POST.get("quarter")
        result = utils.predict(team, op_team, quarter)
        display_result = True

    team_names = utils.load_binary("predictions/pickled/data/unique_teams.pkl")
    quarters = utils.load_binary("predictions/pickled/data/quarters.pkl")
    context = {
        "team_names": team_names,
        "quarters": quarters,
        "result": result,
        "display_result": display_result,
        "team": team,
        "op_team": op_team,
        "quarter": quarter
    }
    return render(request, 'nba_prediction.html', context)
