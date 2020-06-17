from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'website')


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('id', 'style')


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('id', 'color')


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ('id',
                  'size',
                  'brand_name',
                  'manufacturer',
                  'color',
                  'material',
                  'shoe_type',
                  'fasten_type'
                  )
