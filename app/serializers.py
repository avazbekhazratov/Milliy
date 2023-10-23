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


class Savol_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Savol_Javoblar
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


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


class MainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"


class PartnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = "__all__"


class Feed_backserializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"

class Opesaniyaserializer(serializers.ModelSerializer):
    class 