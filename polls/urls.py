from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.polls_index, name='polls_index'),
    path('<int:question_id>/', views.polls_detail, name='polls_detail'),
    path('<int:question_id>/results/', views.polls_results, name='polls_results'),
    path('<int:question_id>/vote/', views.polls_vote, name='polls_vote'),
]