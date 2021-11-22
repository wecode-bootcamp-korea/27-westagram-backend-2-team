from django.urls import path

from .views import LoginView, UserView

urlpatterns = [
    path('signup/', UserView.as_view()),
    path('login/', LoginView)
]
