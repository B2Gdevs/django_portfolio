from django.urls import path
import algorithms.views as algo_views

urlpatterns = [
    path('', algo_views.index_view, name='algorithms'),
    path('/binary_search/', algo_views.binary_search_view,
         name='binary_search')
]