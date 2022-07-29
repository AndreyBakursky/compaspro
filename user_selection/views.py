from rest_framework import viewsets
from .models import UserNew
from .serializers import UserNewSerializer


class UserNewViewSet(viewsets.ModelViewSet):
    queryset = UserNew.objects.all()
    serializer_class = UserNewSerializer
