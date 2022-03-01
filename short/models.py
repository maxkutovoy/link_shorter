from django.db import models

# Create your models here.

class Link(models.Model):
    full_link = models.URLField("Ссылка")
    slug = models.SlugField(
        "Короткая ссылка",
        max_length=100,
        unique=True,
        db_index=True,
    )

