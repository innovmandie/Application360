from django import forms
from django.forms.models import inlineformset_factory
from .models import Avis_B, Email, Evaluation, Contributeur
from evaluationapp import models



class LoginForm(forms.Form):
    nom = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width:300px;', 'class': 'fr-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'style': 'width:300px;', 'class': 'fr-input'}))


class Mailform(forms.Form):
   
    nom = forms.CharField(max_length=200)
    prenom = forms.CharField(max_length=200)
    poste = forms.CharField(max_length=200)
    email = forms.EmailField()
    evalue_nom = forms.CharField(max_length=200)
    fields =[ "nom","prenom", "poste","email", "evalue_nom"]

    class Meta:
        model = Email
        exclude = ['sujet', 'message', 'created_at']

ContributeurFormset = inlineformset_factory(Evaluation, Contributeur, fields=['type_contributeur', 'evaluation', 'contributeur1_nom', 'contributeur1_prenom', 'contributeur1_mail', 'contributeur2_nom','contributeur2_prenom', 'contributeur2_mail'],  max_num=3, min_num=3, extra=3, can_delete=True)

class AvisForm(forms.ModelForm):
    class Meta:
        model = models.Avis_B
        fields = ["evaluation_titre", "nom_contributeur", "nom_evalue", "note_1", "commentaire_note_1", "note_2", "commentaire_note_2", "note_3", "commentaire_note_3", "note_4", "commentaire_note_4", "note_5", "commentaire_note_5", "note_6", "commentaire_note_6",]
    evaluation_titre = forms.TextInput()
    nom_contributeur = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'notation2'}))
    nom_evalue = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class' : 'notation2'}))
    note_1 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_1 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_2 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_2 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_3 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_3 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_4 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_4 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_5 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_5 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_6 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_6 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))

class AvisAgentForm(forms.ModelForm):
    class Meta:
        model = models.Avis_Agent
        fields = ["evaluation_titre", "nom_contributeur", "nom_evalue", "note_1", "commentaire_note_1", "note_2", "commentaire_note_2", "note_3", "commentaire_note_3", "note_4", "commentaire_note_4", "note_5", "commentaire_note_5", "note_6", "commentaire_note_6"]
    evaluation_titre = forms.TextInput()
    nom_contributeur = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'notation2'}))
    nom_evalue = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class' : 'notation2'}))
    
    note_1 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_1 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_2 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_2 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_3 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_3 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_4 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_4 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_5 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_5 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_6 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_6 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))


class AvisEncadreForm(forms.ModelForm):
    class Meta:
        model = models.Avis_Encadre
        fields = ["evaluation_titre", "nom_contributeur", "nom_evalue", "note_1", "commentaire_note_1", "note_2", "commentaire_note_2", "note_3", "commentaire_note_3", "note_4", "commentaire_note_4", "note_5", "commentaire_note_5", "note_6", "commentaire_note_6",]
    evaluation_titre = forms.TextInput()
    nom_contributeur = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'notation2'}))
    nom_evalue = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class' : 'notation2'}))
    note_1 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_1 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_2 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_2 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_3 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_3 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_4 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_4 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_5 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_5 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))
    note_6 = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'type': 'number', 'step': '1', 'class' : 'notation'}))
    commentaire_note_6 = forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class' : 'notation3'}))