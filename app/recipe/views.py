import imp
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authenticate_class = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')