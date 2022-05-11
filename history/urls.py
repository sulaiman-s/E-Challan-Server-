from django.urls import path
from .views import UserHistoryView,WardenHistoryView,UserHistoryDelete,WardenHistoryDelete
urlpatterns=[
    path('userhistory/',UserHistoryView.as_view()),
    path('userhistory/<str:name>',UserHistoryDelete.as_view()),
    path('wardenhistory/',WardenHistoryView.as_view()),
    path('wardenhistory/<str:name>',WardenHistoryDelete.as_view())
]