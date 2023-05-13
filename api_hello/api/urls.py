from django.urls import path
from .views import HelloVV, ListCreateTarefa, DetailUpdateDeleteTarefa, UserSignup
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatters = [
    path('hello/', HelloVV.as_view(), name='hello'),
    path('tarefas', ListCreateTarefa.as_view(), name='list-create-tarefa'),
    path('tarefas/<int:pk>', DetailUpdateDeleteTarefa.as_view(), name='detail-update-delete-filme'),
    path('signup', UserSignup.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='tokenPairView'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]