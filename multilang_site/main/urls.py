from django.urls import path
from . import views
from .views import article_list, create_article, set_language, chatbot_view, chatbot_response

urlpatterns = [
    path('set-language/', views.set_language, name='set_language'),
    path('articles/', views.article_list, name='article_list'),
    path('chatbot/', chatbot_view, name='chatbot_view'),
    path('chatbot/response/', chatbot_response, name='chatbot_response'),
    path('articles/create/', create_article, name='create_article'),
]