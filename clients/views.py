
from rest_framework import viewsets
from .serializer import Clientserializer
from .models import Client





class view(viewsets.ModelViewSet):
    serializer_class = Clientserializer
    queryset= Client.objects.all()
    
   
    