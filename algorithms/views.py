from django.shortcuts import render


# Create your views here.
def index_view(request):
    context = {}
    return render(request, 'algo_index.html', context)


def binary_search_view(request):
    context = {}
    return render(request, 'binarysearch.html', context)


def linear_search_view(request):
    context = {}
    return render(request, 'linearsearch.html', context)