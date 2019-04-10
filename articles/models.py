from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Article(models.Model):
    title=models.CharField(_('title'),max_length=128)