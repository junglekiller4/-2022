from rest_framework import viewsets
from printing3d.serializers import *
from printing3d.models import *
from django_filters.rest_framework import DjangoFilterBackend
from .service import ModeltFilter

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model3d.objects.all().order_by('id')
    serializer_class = ModelsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ModeltFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User3d.objects.all().order_by('id')
    serializer_class = UsersSerializer

class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell3d.objects.all().order_by('id')
    serializer_class = SellsSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

class MinMaxViewSet(viewsets.ModelViewSet):
    queryset = Model3d.objects.all()
    serializer_class = MinMaxSerializer