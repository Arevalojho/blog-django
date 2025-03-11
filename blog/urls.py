from django.urls import path
from .views import (
                        PublicationListView, 
                        PublicationDetailView,
                        PublicationCreateView,
                    )


urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('Publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('Publication/new/', PublicationCreateView.as_view(), name='publication-create'),
]
   
