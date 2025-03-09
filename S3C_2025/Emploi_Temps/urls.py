from django.urls import path
from .views import EnseignantListCreateAPIView, EnseignantRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),
]
