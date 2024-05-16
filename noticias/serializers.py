from .models import Noticia
from rest_framework.serializers import ModelSerializer

class NoticiaSerializer(ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"
