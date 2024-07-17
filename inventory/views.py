from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        sku = request.query_params.get('sku', None)
        if sku is not None:
            try:
                item = Item.objects.get(sku=sku)
                serializer = ItemSerializer(item)
                return Response(serializer.data)
            except Item.DoesNotExist:
                return Response({'error': 'Item not found'}, status=404)
        return Response({'error': 'SKU not provided'}, status=400)
