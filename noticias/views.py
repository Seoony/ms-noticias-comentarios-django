from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoticiaSerializer
from .models import Noticia

@api_view(["GET"])
def get_noticias(request):
    noticias = Noticia.objects.all()
    serializer = NoticiaSerializer(noticias, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_noticia(request, pk):
    noticia = Noticia.objects.get(id=pk)
    serializer = NoticiaSerializer(noticia, many=False)
    return Response(serializer.data)
  
@api_view(["POST"])
def create_noticia(request):
    serializer = NoticiaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT"])
def update_noticia(request, pk):
    noticia = Noticia.objects.get(id=pk)
    serializer = NoticiaSerializer(instance=noticia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def delete_noticia(request, pk):
    noticia = Noticia.objects.get(id=pk)
    noticia.delete()
    return Response("Noticia deleted successfully")
