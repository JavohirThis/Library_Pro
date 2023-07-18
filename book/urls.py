from django.urls import path
from .views import (AllBookView,DetailBookView,CreateBookView,
                    UpdateBookView,DeleteBookView,DetailAuthorView,DeleteAuthorView,CreateAuthorView,UpdateAuthorView,AllAuthorView)
urlpatterns = [
    path('',AllBookView.as_view()),
    path('<pk>',DetailBookView.as_view()),
    path('create/',CreateBookView.as_view()),
    path('update/<pk>/',UpdateBookView.as_view()),
    path('delete/<pk>/',DeleteBookView.as_view()),
    path('Author/<pk>/',DetailAuthorView.as_view()),
    path('Author/create/',CreateAuthorView.as_view()),
    path('Author/update/<pk>/',UpdateAuthorView.as_view()),
    path('Author/', AllAuthorView.as_view()),
    path('Author/delete/<pk>/', DeleteAuthorView.as_view()),

]