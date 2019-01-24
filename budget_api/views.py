"""Views to handle auth with Django REST framework."""
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .serializers import UserSerializer, User


class RegisterApiView(generics.CreateAPIView):
    """View for registering a new user."""
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])
