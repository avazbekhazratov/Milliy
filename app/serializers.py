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


class News_add_Ser(serializers.ModelSerializer):
    class Meta:
        model = News_add
        fields = "__all__"


class Xaridordan_Ser(serializers.ModelSerializer):
    class Meta:
        model = Xaridordan_savol
        fields = "__all__"


class Product_info_Ser(serializers.ModelSerializer):
    class Meta:
        model = Product_info
        fields = "__all__"


class Partners_logo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Partners_logo
        fields = "__all__"


class AdvertSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = "__all__"


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class BrendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = "__all__"


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
