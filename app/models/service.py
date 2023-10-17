from django.db import models

from app.models import User
from app.models.core import Brend


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brends = models.ForeignKey(Brend, on_delete=models.CASCADE)
    # Sotib olgan mahsulotlari
