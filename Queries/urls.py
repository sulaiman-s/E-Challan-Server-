from django.urls import path
from . import views
urlpatterns = [
    path('query/', views.QueriesView.as_view()),
    path('upload/', views.UploadsView.as_view()),
    path('image/', views.MLImageView.as_view())
]
