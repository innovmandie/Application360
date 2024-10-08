from django.urls import path
from django.contrib.auth import views as auth_views
from evaluationapp import views






urlpatterns = [
    path('', views.index, name='index'),
    path('evalue/', views.evaluePage, name='evaluePage'),
    path('questions/', views.questionsPage, name='questionsPage'),
    path('etapequestion/', views.etapequestion, name='etapequestion'),
    path('end/', views.end, name='end'),
    path('questionbeneficiaire/', views.survey_detail, name='questionbeneficiare'),
    path('questionfonctionnel/', views.survey_detail2, name='questionfonctionnel'),
    path('questionencadres/', views.survey_detail3, name='questionencadres'),
    path('mine/',views.ManageEvaluationListView.as_view(),name='manage_evaluation_list'),
    path('create/',views.EvaluationCreateView.as_view(),name='evaluation_create'),
    path('<pk>/edit/',views.EvaluationUpdateView.as_view(),name='evaluation_edit'),
    path('<pk>/delete/',views.EvaluationDeleteView.as_view(),name='evaluation_delete'),
    path('<pk>/contributeur/', views.EvaluationContributeurUpdateView.as_view(), name='evaluation_contributeur_update'),
    path('<int:pk>/tableaudebord/', views.EvaluationTableaudebord.as_view(), name='evaluation_tableaudebord'),
    path('<int:pk>/resultats/', views.EvaluationResultats.as_view(), name='evaluation_resultats'),
    path('evaluation/<int:pk>/resultatspdf/', views.EvaluationPDF.as_view(), name='resultatspdf'),

]