from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"name={self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=120)
    url = models.URLField(max_length=400)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"title={self.title}, category={self.category}, url={self.url}"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # additional attributes
    profile_website = models.URLField(max_length=400, blank=True)
    profile_image = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return f"username : {self.user.username}, email_id : {self.user.email}, is_active : {self.user.is_active}"
