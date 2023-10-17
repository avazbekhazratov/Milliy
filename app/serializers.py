from rest_framework import serializers
from app.models import (
    Category,
    SubCategory,
    Main,
    Partners,
    Partners_logo,
    Advert,
    News,
    News_add,
    Xaridordan_savol,
    Company,
    Contact,
    Brend,
    Product_info,
    Xarakteristika,
    Opesaniya,
    FeedBack,
    Savol_Javoblar,
    Product,
    Product_images
)


# class ProductsSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def get_image_url(self, obj):
#         request = self.context.get('request')
#         if obj.img:
#             return obj.img.url
#         return None


# class ProductImg(serializers.ModelSerializer):
#     class Meta:
#         model = Product_images
#         fields = "__all__"
#
#     def get_image_url(self, obj):
#         request = self.context.get('request')
#         if obj.img:
#             return obj.img.url
#         return None


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = "__all__"


class MyModelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image_urls(self, obj):
        return [img.img.url for img in obj.img.all()]
