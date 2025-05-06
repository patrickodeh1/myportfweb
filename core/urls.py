from django.urls import path
from .views import AboutView, AllProjectsView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('all-projects/', AllProjectsView.as_view(), name='all-projects')
]