from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    '''User signup
       POST -- /signup
    '''

    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)
