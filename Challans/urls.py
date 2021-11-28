from django.urls import path
from .views import ChallanView, ChallanViewDetail


urlpatterns = [
    path('allchallans/', ChallanView.as_view()),
    path('allchallans/<int:id>', ChallanViewDetail.as_view()),

]
