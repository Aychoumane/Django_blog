from django.conf import settings 
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import translation
#from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .forms import ArticleForm
import json
import requests


# Create your views here.


# Vue articles/menu principal
def article_list(request):
    articles = Article.objects.all()  # Récupère tous les articles depuis la base de données
    context = {
        'articles': articles,  
    }
    return render(request, 'main/article_list.html', context)

def set_language(request):
    user_language = request.GET.get('language', 'fr')
    translation.activate(user_language)
    request.session[settings.LANGUAGE_COOKIE_NAME] = user_language
    return redirect(request.META.get('HTTP_REFERER', '/'))


# Vue chatbot 

def chatbot_view(request):
    return render(request, 'main/chatbot.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_message = json.loads(request.body).get('message')
        response_message = get_gpt_response(user_message)
        return JsonResponse({'message': response_message})

def get_gpt_response(message):
    api_key = settings.OPENAI_API_KEY  
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'prompt': message,
        'max_tokens': 150
    }
    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        error_response = response.json()
        error_message = "Erreur : " + error_response.get('error', {}).get('message', 'Unknown error')+ "\n"
        error_type = "Erreur type : " + error_response.get('error', {}).get('type', 'Unknown type') + "\n"
        return "Erreur dans la génération de la réponse.\n" + error_message + error_type


#Vue création d'article

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'main/create_article.html', {'form': form})