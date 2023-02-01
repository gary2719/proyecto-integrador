from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from api.serializers import BooksSerializer
from api.models import Books

@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de libros.'),
    retrieve=extend_schema(description='Permite obtener un libro'),
    create=extend_schema(description='Permite crear un libro.'),
    update=extend_schema(description='Permite actualizar un libro'),
    destroy=extend_schema(description='Permite eliminar un libro'),
)
class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()