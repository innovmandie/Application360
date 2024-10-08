from django.contrib import admin
from .models import Avis_Agent, Avis_B, Avis_Encadre, Email, Thematique, Evaluation, Contributeur


@admin.register(Thematique)
class ThematiqueAdmin(admin.ModelAdmin):
 list_display = ['titre']
 prepopulated_fields={'titre': ('titre',)}


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
 list_display = ['sujet', 'nom', 'prenom', 'poste', 'message', 'email', 'created_at']

 
class ContributeurInline(admin.StackedInline):
 model = Contributeur


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
 list_display = ['titre','evalue_nom']
 list_filter = ['evalue_nom', 'titre']
 search_fields = ['titre', 'evalue_nom']
 prepopulated_fields={'titre': ('titre',)}
 inlines = [ContributeurInline]

admin.site.register(Avis_B)
admin.site.register(Avis_Agent)
admin.site.register(Avis_Encadre)
