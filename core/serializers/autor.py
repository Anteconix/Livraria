from rest_framework.serializers import ModelSerializer
from core.models import Autor, Categoria, Editora, Livro

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
