from rest_framework import serializers

from item.models import Category as CategorytModel
from item.models import Item as ItemwModel
from item.models import Order as OrderwModel
from item.models import ItemOrder as ItemOrderwModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategorytModel   #어떤 모델을 쓸지 지칭
        fields = ["name"]


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = ItemwModel   #어떤 모델을 쓸지 지칭
        fields = ["name", "category", "image_url"]
        
class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, source="item_set")
    class Meta:
        model = OrderwModel   #어떤 모델을 쓸지 지칭
        fields = ["delivery_address", "order_date", "item"]

class ItemOrderSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()

    class Meta:
        model = ItemOrderwModel   #어떤 모델을 쓸지 지칭
        fields = ["order", "item", "item_count"]



