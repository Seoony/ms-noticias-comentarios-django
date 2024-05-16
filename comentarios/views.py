from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ComentarioSerializer
from .models import Comentario

@api_view(["GET"])
def get_comentarios(request):
    comentarios = Comentario.objects.all()
    serializer = ComentarioSerializer(comentarios, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_comentario(request, pk):
    comentario = Comentario.objects.get(id=pk)
    serializer = ComentarioSerializer(comentario, many=False)
    return Response(serializer.data)
  
@api_view(["POST"])
def create_comentario(request):
    serializer = ComentarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
  
@api_view(["PUT"])
def update_comentario(request, pk):
    comentario = Comentario.objects.get(id=pk)
    serializer = ComentarioSerializer(instance=comentario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
  
@api_view(["DELETE"])
def delete_comentario(request, pk):
    comentario = Comentario.objects.get(id=pk)
    comentario.delete()
    return Response("Comentario deleted successfully")
