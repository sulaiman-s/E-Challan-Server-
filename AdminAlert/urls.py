from django.urls import path

from AdminAlert.views import AlertsImageView,AlertsMessageView

urlpatterns=[
    path('images/',AlertsImageView.as_view()),
    path('msgs/',AlertsMessageView.as_view())
]