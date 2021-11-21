from django.urls import path
from users.views import UserView

urlpatterns = [
    path('/create', UserView.as_view())
]

