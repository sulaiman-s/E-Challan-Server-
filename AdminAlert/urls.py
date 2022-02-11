from django.urls import path

from AdminAlert.views import AlertsView

urlpatterns=[
    path('alert/',AlertsView.as_view())
]