from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    pic = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def json(self):
        return dict(name=self.name, price=self.price, pic=self.pic, id=self.pk)
