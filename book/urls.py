from django.urls import path
from .views import (AllCreateBookView,DetailDelUpBookView,DetailDelUpAuthorView,AllCreateAuthorView)
urlpatterns = [
    path('',AllBookView.as_view()),
    path('<pk>/',DetailDelUpBookView.as_view()),
    path('Author/', AllAuthorView.as_view()),
    path('Author/<pk>/',DetailDelUpAuthorView.as_view()),
]