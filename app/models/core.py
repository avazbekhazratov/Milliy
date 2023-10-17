from django.db import models

from app.models import User


class Category(models.Model):
    name = models.CharField(max_length=199, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    subctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.subctg}"


class Main(models.Model):
    img = models.ImageField(upload_to='main/images')
    title = models.CharField(max_length=51)
    title_desc = models.CharField(max_length=300)
    title_com = models.CharField(max_length=50)
    title_com_desc = models.CharField(max_length=300)
    title_ass = models.CharField(max_length=50)
    title_ass_desc = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Partners(models.Model):
    title = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.title


class Partners_logo(models.Model):
    img = models.ImageField(upload_to='partners/images')

    def __str__(self):
        return self.id


class Advert(models.Model):  # reklama
    logo = models.CharField(max_length=200)
    title = models.CharField(max_length=256)
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class News_add(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='news/images')

    def __str__(self):
        return self.title


class Xaridordan_savol(models.Model):
    savol_turi = models.CharField(max_length=128)
    javobi = models.TextField()

    def __str__(self):
        return self.savol_turi


class Company(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='news/images')

    def __str__(self):
        return self.title


class Contact(models.Model):
    location = models.CharField(max_length=500)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.phone


class Brend(models.Model):
    title = models.CharField(max_length=128)
    img = models.ImageField(upload_to='brend/images')


class Product_info(models.Model):
    brend = models.CharField("Brend nomi", max_length=128)
    model = models.CharField("Maxsulot turi", max_length=128)  # Maxsulot turi
    sert = models.CharField("Sertifikat", max_length=128)
    product_name = models.CharField("Maxsulot nomi", max_length=200)
    dioganal = models.CharField(null=True, blank=True, max_length=100)  # Maxsulot dioganali
    protsesr = models.CharField(null=True, blank=True, max_length=200)  # Maxsulot protsesri

    def __str__(self):
        return f"{self.brend} | {self.model}"


class Xarakteristika(models.Model):
    protssesor = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    kesh = models.CharField(max_length=200)
    chipset = models.CharField(max_length=200)

    screen = models.CharField("Izobrajenia", max_length=200)
    ekran = models.CharField(max_length=200)
    tip = models.CharField(max_length=200)
    matritsa = models.CharField(max_length=200)
    chastota = models.CharField(max_length=200)
    video_karta = models.CharField(max_length=200)
    video_prot = models.CharField(max_length=200)
    video_tip = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.protssesor} | {self.screen}"


class Opesaniya(models.Model):
    img = models.ImageField(upload_to='product/images/opesaniya')
    title = models.CharField(max_length=200)
    text = models.TextField()


class FeedBack(models.Model):  # Foydalanuvchilar Fikri
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reating = models.CharField(max_length=2, choices=[
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ])
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fikri"


class Savol_Javoblar(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Yozilgan savollar"


class Product_images(models.Model):
    img = models.ImageField(upload_to='product')


class Product(models.Model):
    product = models.ForeignKey(Product_info, on_delete=models.CASCADE)
    xaraktristika = models.ForeignKey(Xarakteristika, on_delete=models.CASCADE)
    opesaniya = models.ForeignKey(Opesaniya, on_delete=models.CASCADE)
    vapros = models.ForeignKey(Savol_Javoblar, on_delete=models.CASCADE)
    #
    img = models.ManyToManyField(Product_images)
    title = models.CharField(max_length=200)
    shop_name = models.CharField(max_length=200)
    desc = models.TextField()
    color = models.CharField(max_length=200)
    quent = models.IntegerField(default=1)
    memory = models.CharField(max_length=300, blank=True, null=True)
    price = models.IntegerField()
    disc_price = models.IntegerField()  # chegirma narxi

    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
