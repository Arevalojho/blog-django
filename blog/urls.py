from django.urls import path
from .views import (
                        PublicationListView, 
                        PublicationDetailView,
                        PublicationCreateView,
                        PublicationUpdateView,
                        PublicationDeleteView,
                    )


urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('Publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('Publication/new/', PublicationCreateView.as_view(), name='publication-create'),
    path('Publication/<int:pk>/update/', PublicationUpdateView.as_view(), name='publication-update'),
    path('Publication/<int:pk>/delete/', PublicationDeleteView.as_view(), name='publication-delete'),
]
   
