from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from main.views.balances import BalancesView

urlpatterns = [

    path('users/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('balance', BalancesView.as_view()),
]
