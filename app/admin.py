from django.contrib import admin
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
admin.site.register(Product)
admin.site.register(Product_images)
admin.site.register(Savol_Javoblar)
admin.site.register(FeedBack)
admin.site.register(Opesaniya)
admin.site.register(Xarakteristika)
admin.site.register(Product_info)
admin.site.register(Brend)
admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(Xaridordan_savol)
admin.site.register(News_add)
admin.site.register(News)
admin.site.register(Advert)
admin.site.register(Partners_logo)
admin.site.register(Partners)
admin.site.register(Main)
admin.site.register(Category)
admin.site.register(SubCategory)
