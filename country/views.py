from  .models import Country
from .serializers import CountryModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class CountryModelViewSet(ReadOnlyModelViewSet):
    model = Country
    serializer_class = CountryModelSerializer
    queryset = Country.objects.all()
    permission_classes = [AllowAny]

