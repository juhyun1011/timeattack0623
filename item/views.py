from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from item.models import Category as CategoryModel
from item.models import Item as ItemModel
from item.models import Order as COrderModel
from item.models import ItemOrder as ItemOrderModel

from item.serializers import CategorySerializer
from item.serializers import ItemSerializer
from item.serializers import OrderSerializer
from item.serializers import ItemOrderSerializer

# Create your views here.

class ItemView(APIView):

    def get(self, request):
        item = 


        return Response(CategorySerializer(items, many=True).data)



    def post(self, request):

        return Response({})
