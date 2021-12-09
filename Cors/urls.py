from django.urls import path
from .views import MyTokenObtainPairView

urlpatterns = [
    path(
        'create/', MyTokenObtainPairView.as_view()
    )
]
