from django.urls import path
from . import views

title="knowledge_base"
urlpatterns = [
    path('', views.home, name='home'),
    path(r'knowledge_base', views.knowledge_base, name=title),
    path(r'faq', views.faq, name='faq')
]


