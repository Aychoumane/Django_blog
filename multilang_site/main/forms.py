from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Article
from django.utils import timezone

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publication_date']
        #Pour la traduction l'outil traduction django
        labels = {
            'title': _('Titre'),
            'content': _('Contenu'),
            'publication_date': _('Date de publication'),
        }
        #Changer les attributs 
        widgets = {
            'publication_date': forms.DateInput(attrs={
                'placeholder': 'DD/MM/YYYY',
                'class': 'form-control',  
                'type': 'date',  
                'value': timezone.now().strftime('%d-%m-%Y')
            }),
        }