from itertools import chain
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View

from evaluation360.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from .forms import ContributeurFormset

from .models import Avis_Agent, Avis_Encadre, Contributeur, Evaluation
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate 

from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import pandas as pd

from django.views import View
from django.contrib.auth.models import User

from django.core.mail import EmailMessage, get_connection

from .forms import *

from .models import Avis_B

from django.template.loader import get_template
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import io

import smtplib
    
def index(request):
     return render(request, 'index.html')

def end(request):
     return render(request, 'end.html')

def evaluePage(request):
  return render(request, 'evalue_page.html')

def questionsPage(request):
     return render(request, 'questions.html')


@login_required
def etapequestion(request):
  if request.user.is_authenticated:
        current_username = request.user.username
        return render(request, 'etapequestion.html', {'current_username': current_username})
  else:
        return redirect('index')


@login_required 
def questionbeneficiare(request):
  form_test = AvisForm()
  return render(request, 'questionslevel1.html', {'form_test': form_test})


@login_required 
def questionfonctionnel(request):
     return render(request, 'questionslevel1.html')

@login_required 
def questionencadres(request):
     return render(request, 'questionslevel3.html')

@login_required
def survey_detail(request):
    if request.method == 'POST':
      details = AvisForm(request.POST)
      if details.is_valid():
        post = details.save(commit=False)
        post.save()
        
        return render(request, 'end.html')
    else:
       form = AvisForm()
       context = {'form': form }
    return render(request, 'questionslevel1.html', context)

@login_required
def survey_detail2(request):
    if request.method == 'POST':
      details = AvisAgentForm(request.POST)
      if details.is_valid():
        post = details.save(commit=False)
        post.save()
        
        return render(request, 'end.html')
    else:
       form = AvisAgentForm()
       context = {'form': form }
    return render(request, 'questionslevel2.html', context)

@login_required
def survey_detail3(request):
    if request.method == 'POST':
      details = AvisEncadreForm(request.POST)
      if details.is_valid():
        post = details.save(commit=False)
        post.save()
        
        return render(request, 'end.html')
    else:
       form = AvisAgentForm()
       context = {'form': form }
    return render(request, 'questionslevel3.html', context)





class ManageEvaluationListView(ListView):
   model = Evaluation
   template_name = 'evaluations/manage/evaluation/list.html'
   def get_queryset(self):
      qs = super().get_queryset()
      return qs.filter(owner_evalue=self.request.user)
   
class OwnerMixin(object):
 def get_queryset(self):
   qs = super().get_queryset()
   return qs.filter(owner_evalue=self.request.user)
 
class OwnerEditMixin(object):
  def form_valid(self, form):
    form.instance.owner_evalue = self.request.user
    return super().form_valid(form)
  
class OwnerEvaluationMixin(OwnerMixin, LoginRequiredMixin,PermissionRequiredMixin):
 model = Evaluation
 fields = ['titre','evalue_nom', 'evalue_prenom', 'evalue_poste', 'time']
 success_url = reverse_lazy('manage_evaluation_list')
 
class OwnerEvaluationEditMixin(OwnerEvaluationMixin, OwnerEditMixin):
  template_name = 'evaluations/manage/evaluation/form.html'

class ManageEvaluationListView(OwnerEvaluationMixin, ListView):
 template_name = 'evaluations/manage/evaluation/list.html'
 permission_required = 'evaluations.view_evaluation'

class EvaluationTableaudebord(OwnerEvaluationMixin, ListView):
 template_name = 'evaluations/manage/evaluation/tableaudebord.html'
 permission_required = 'evaluations.view_evaluation'
 #permission2_required = 'contributeur.view_contributeur'


class EvaluationCreateView(OwnerEvaluationEditMixin, CreateView):
  permission_required = 'evaluations.add_evaluation'

class EvaluationUpdateView(OwnerEvaluationEditMixin, UpdateView):
  permission_required = 'evaluations.change_evaluation'

class EvaluationDeleteView(OwnerEvaluationMixin, DeleteView):
 template_name = 'evaluations/manage/evaluation/delete.html'
 permission_required = 'evaluations.delete_evaluation'


class EvaluationContributeurUpdateView(TemplateResponseMixin, View):
  template_name ='evaluations/manage/contributeur/formset.html'
  evaluation = None

  def get_formset(self, data=None) :
    return ContributeurFormset(instance=self.evaluation, data=data)
  
  def dispatch(self, request, pk):
    self.evaluation = get_object_or_404(Evaluation, id=pk, owner_evalue=request.user)
    return super().dispatch(request, pk)
  
  def get(self, request, *args, **kargs):
    formset=self.get_formset()
    return self.render_to_response({'evaluation' : self.evaluation, 'formset' : formset})
  
  def post(self, request, *args, **kargs):
    formset = self.get_formset(data=request.POST)
    if formset.is_valid():
      formset.save()
      return redirect('manage_evaluation_list')
    return self.render_to_response({'evaluation': self.evaluation, 'formset' : formset})
  
class EvaluationTableaudebord(FormView,ListView):
  model = Evaluation
  template_name = 'evaluations/manage/evaluation/tableaudebord.html'
  evaluation = None
  def get_queryset(self):
      qs = super().get_queryset()
      return qs.filter(owner_evalue=self.request.user)
  
  def get_context_data(self, **kargs):
    context = super().get_context_data(**kargs)
    contributeur=Contributeur.objects.filter(evaluation_id=self.kwargs.get('pk'))
    my_data=list(Contributeur.objects.filter(evaluation_id=self.kwargs.get('pk')).values_list('contributeur1_mail', flat=True))
    my_data2=list(Contributeur.objects.filter(evaluation_id=self.kwargs.get('pk')).values_list('contributeur2_mail', flat=True))
    for i in my_data2 :
       my_data.append(i)
    evaluation=Evaluation.objects.filter(id=self.kwargs.get('pk'))
    email=Email.objects.all()
    context['contributeur']= contributeur
    context['evaluation']=evaluation
    context['email']= email
    return context
  
  form_class = Mailform
  context_object_name='mydata'
  
  success_url = '/'
  #success_urls = reverse('evaluation_tableaudebord')

  def form_valid(self, form):
    
    sujet_mail ="Evaluation 360"
    reicipient_message = form.cleaned_data['email']
    nom = form.cleaned_data['nom']
    prenom = form.cleaned_data['prenom']
    poste = form.cleaned_data['poste']
    evalue_nom = form.cleaned_data['evalue_nom']
    form = Email
    context = {
        'nom': nom,
        'prenom': prenom,
        'poste': poste,
        'evalue_nom' : evalue_nom
    }

    html_message = render_to_string('evaluations/manage/evaluation/email.html', context)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
      subject = sujet_mail,
      body = plain_message,
      from_email= None,
      to = [reicipient_message]
    )

    message.attach_alternative(html_message, "text/html")
    message.send(fail_silently=False,)
     
    obj = Email(
      sujet = sujet_mail,
      message =  "message envoye",
      email = reicipient_message,
      nom = nom,
      prenom = prenom,
      evalue_nom = evalue_nom
      
    )
    obj.save()
    pk=self.kwargs.get('pk')
    #return super().form_valid(form)
    return redirect(reverse('evaluation_tableaudebord', kwargs={'pk': pk}))
    #return HttpResponseRedirect(reverse('evaluation_tableaudebord'))


class EvaluationResultats(ListView):
  model = Evaluation
  
  template_name = 'evaluations/manage/evaluation/resultats.html'

  def get_queryset(self):
      qs = super().get_queryset()
      return qs.filter(owner_evalue=self.request.user)
  
  def get_context_data(self, **kargs):
    context = super().get_context_data(**kargs)
    contributeur=Contributeur.objects.filter(evaluation_id=self.kwargs.get('pk'))
    resultats_beneficiaire=Avis_B.objects.filter(evaluation_titre=self.kwargs.get('pk')).values()
    resultats_agent=Avis_Agent.objects.filter(evaluation_titre=self.kwargs.get('pk')).values()
    resultats_encadre=Avis_Encadre.objects.filter(evaluation_titre=self.kwargs.get('pk')).values()
    evaluation=Evaluation.objects.filter(id=self.kwargs.get('pk'))
    email=Email.objects.all()
    context['contributeur']= contributeur
    context['evaluation']=evaluation
    context['email']=email
    context['resultats_beneficiaire']=resultats_beneficiaire
    context['resultats_agent']=resultats_agent
    context['resultats_encadre']=resultats_encadre

    dfnote_B = pd.DataFrame(list(resultats_beneficiaire))
    dfnote_B = dfnote_B[['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6']]
    note_B=round(((dfnote_B.sum(axis=1))*2)/3, 2)
    note_B= pd.to_numeric(note_B, errors='coerce')
    globale_B = (note_B.sum())/2

    context['note_B'] = note_B
    context['globale_B'] = globale_B

    dfnote_A = pd.DataFrame(list(resultats_encadre))
    dfnote_A = dfnote_A[['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6']]
    note_A=round(((dfnote_A.sum(axis=1))*2)/3, 2)
    note_A= pd.to_numeric(note_A, errors='coerce')
    globale_A = (note_A.sum())/len(dfnote_A)

    
    context['note_A'] = note_A
    context['globale_A'] = globale_A

    dfnote_C = pd.DataFrame(list(resultats_agent))
    dfnote_C = dfnote_C[['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6']]
    note_C=round(((dfnote_C.sum(axis=1))*2)/3, 2)
    note_C= pd.to_numeric(note_C, errors='coerce')
    globale_C = (note_A.sum())/len(dfnote_A)
    
    context['note_C'] = note_C
    context['globale_C'] = globale_C
  
    return context
#######################################################
  
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
class EvaluationPDF(ListView):
  model = Evaluation
  template_name = 'evaluations/manage/evaluation/resultats_pdf.html'
  def get_queryset(self):
    qs = super().get_queryset()
    return qs.filter(owner_evalue=self.request.user)
  def get_context_data(self, **kargs):
    context = super().get_context_data(**kargs)
    contributeur=Contributeur.objects.filter(evaluation_id=self.kwargs.get('pk'))
    resultats_beneficiaire=Avis_B.objects.filter(evaluation_titre=self.kwargs.get('pk')).values()
    resultats_agent=Avis_Agent.objects.filter(evaluation_titre=self.kwargs.get('pk')).values()
    resultats_encadre=Avis_Encadre.objects.filter(evaluation_titre=self.kwargs.get('pk')).values()
    evaluation=Evaluation.objects.filter(id=self.kwargs.get('pk'))
    email=Email.objects.all()
    context['contributeur']= contributeur
    context['evaluation']=evaluation
    context['email']=email
    context['resultats_beneficiaire']=resultats_beneficiaire
    context['resultats_agent']=resultats_agent
    context['resultats_encadre']=resultats_encadre

    dfnote_B = pd.DataFrame(list(resultats_beneficiaire))
    dfnote_B = dfnote_B[['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6']]
    note_B=round(((dfnote_B.sum(axis=1))*2)/3, 2)
    note_B= pd.to_numeric(note_B, errors='coerce')
    globale_B = (note_B.sum())/2

    context['note_B'] = note_B
    context['globale_B'] = globale_B

    dfnote_A = pd.DataFrame(list(resultats_encadre))
    dfnote_A = dfnote_A[['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6']]
    note_A=round(((dfnote_A.sum(axis=1))*2)/3, 2)
    note_A= pd.to_numeric(note_A, errors='coerce')
    globale_A = (note_A.sum())/len(dfnote_A)

    
    context['note_A'] = note_A
    context['globale_A'] = globale_A

    dfnote_C = pd.DataFrame(list(resultats_agent))
    dfnote_C = dfnote_C[['note_1', 'note_2', 'note_3', 'note_4', 'note_5', 'note_6']]
    note_C=round(((dfnote_C.sum(axis=1))*2)/3, 2)
    note_C= pd.to_numeric(note_C, errors='coerce')
    globale_C = (note_A.sum())/len(dfnote_A)
    
    context['note_C'] = note_C
    context['globale_C'] = globale_C
    story = []
    
    # Initialise the simple document template
    doc = SimpleDocTemplate(f".pdf",
                            page_size=letter,
                            bottomMargin=.4 * inch,
                            topMargin=.4 * inch,
                            rightMargin=.8 * inch,
                            leftMargin=.8 * inch)
    
    # set the font style
    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    data = chain(resultats_beneficiaire, resultats_encadre)

    for count, d in enumerate(data, 1):
        p_count = Paragraph(f" Data: {count} ")
        story.append(Spacer(1, 12))
        story.append(p_count)
        for k, v in d.items():
            # extract and add key value pairs to PDF
            p = Paragraph(k + " : " + str(v), styleN)
            story.append(p)
            story.append(Spacer(1, 2))
    # build PDF using the data
    doc.build(story)
  
    return context
  


     
   