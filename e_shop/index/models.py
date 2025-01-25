from django.db import models


# Create your models here.
class NewCategory(models.Model):
    category_name = models.CharField(max_length=64)
    added_date = models.DateTimeField()


class News(models.Model):
    news_name = models.CharField(max_length=256, default="None")
    zagolovok = models.TextField()
    asosiy_matn = models.TextField()
    news_category = models.ForeignKey(NewCategory, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

