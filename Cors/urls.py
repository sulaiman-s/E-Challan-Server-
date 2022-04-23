from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('create/', MyTokenObtainPairView.as_view()),
    path('account/', include('django.contrib.auth.urls'))
]
