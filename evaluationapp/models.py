from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class Thematique(models.Model):
    titre = models.CharField(max_length=200)
    class Meta:
       ordering = ['titre']
    def __str__(self):
          return self.titre
YEAR_CHOICES = [(r,r) for r in range(2020, datetime.date.today().year+4)]

class Evaluation(models.Model):
    owner_evalue = models.ForeignKey(User,related_name='evalue_created',on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    evalue_nom = models.CharField(max_length=200)
    evalue_prenom = models.CharField(max_length=200)
    evale_mail = models.EmailField(max_length=200)
    evalue_poste= models.CharField(max_length=200)
    time= models.IntegerField(('time'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    date_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ['titre']
    def __str__(self):
        return self.titre
    

class Contributeur(models.Model):
    evaluation = models.ForeignKey(Evaluation,related_name='contributeur',on_delete=models.CASCADE)
    Beneficiaire = "Beneficiaire"
    Collegue = "Collegue"
    Agent_encadre= "Agent_encadre"
    Type_CHOICES =(
        (Beneficiaire, "Beneficiaire"),
        (Collegue, "Collegue en lien fonctionnel"),
        (Agent_encadre, "Agent encadre"),
    )
    type_contributeur= models.CharField(max_length=20, choices = Type_CHOICES, default = Beneficiaire)
    contributeur1_nom = models.CharField(max_length=200)
    contributeur1_prenom = models.CharField(max_length=200)
    contributeur1_mail= models.EmailField(max_length=200)
    contributeur2_nom = models.CharField(max_length=200)
    contributeur2_prenom = models.CharField(max_length=200)
    contributeur2_mail= models.EmailField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ['-created']
    def __str__(self):
        return self.evaluation
    
class Email(models.Model):
    sujet = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    poste = models.CharField(max_length=200)
    evalue_nom = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.sujet

class Avis_B(models.Model):
    evaluation_titre = models.ForeignKey(Evaluation,related_name='avis_beneficiaire',on_delete=models.CASCADE)

    nom_contributeur = models.CharField(max_length=200)
    nom_evalue = models.CharField(max_length=200)
    note_1 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_1 = models.CharField(max_length=400)
    note_2 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_2 = models.CharField(max_length=400)
    note_3 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_3 = models.CharField(max_length=400)
    note_4 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_4 = models.CharField(max_length=400)
    note_5 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_5 = models.CharField(max_length=400)
    note_6 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_6 = models.CharField(max_length=400)

    def __str__(self):
        return self.evaluation_titre
    
class Avis_Agent(models.Model):
    evaluation_titre = models.ForeignKey(Evaluation,related_name='avis_agent',on_delete=models.CASCADE)

    nom_contributeur = models.CharField(max_length=200)
    nom_evalue = models.CharField(max_length=200)
    note_1 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_1 = models.CharField(max_length=400)
    note_2 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_2 = models.CharField(max_length=400)
    note_3 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_3 = models.CharField(max_length=400)
    note_4 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_4 = models.CharField(max_length=400)
    note_5 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_5 = models.CharField(max_length=400)
    note_6 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_6 = models.CharField(max_length=400)
    def __str__(self):
        return self.evaluation_titre
    
class Avis_Encadre(models.Model):
    evaluation_titre = models.ForeignKey(Evaluation,related_name='avis_encadre',on_delete=models.CASCADE)

    nom_contributeur = models.CharField(max_length=200)
    nom_evalue = models.CharField(max_length=200)
    note_1 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_1 = models.CharField(max_length=400)
    note_2 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_2 = models.CharField(max_length=400)
    note_3 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_3 = models.CharField(max_length=400)
    note_4 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_4 = models.CharField(max_length=400)
    note_5 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_5 = models.CharField(max_length=400)
    note_6 = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    commentaire_note_6 = models.CharField(max_length=400)

    def __str__(self):
        return self.evaluation_titre

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    rating = models.IntegerField()
    # Add other fields as needed


