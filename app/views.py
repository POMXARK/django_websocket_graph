from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.forms import LoginUserForm
from app.models import Ai1, Ai2
from app.serializers import Ai1Serializer, Ai2Serializer


class LoginUser(LoginView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    form_class = LoginUserForm
    template_name = 'app/login.html'

    def get_success_url(self):
        username = self.request.user.username
        if username == 'user1' or username == 'user2':
            return reverse_lazy('home')


class TableViewSetAi1(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Ai1Serializer
    queryset = Ai1.objects.all()
    permission_classes = [IsAuthenticated]


class TableViewSetAi2(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Ai2Serializer
    queryset = Ai2.objects.all()
    permission_classes = [IsAuthenticated]


def logout_user(request):
    logout(request)
    return redirect('login')
