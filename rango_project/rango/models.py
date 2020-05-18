from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"name={self.name}"


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"title={self.title}, category={self.category}, url={self.url}"
