import uuid
from django.db import models

# Create your models here.

class Link(models.Model):
    full_link = models.URLField("Ссылка")
    slug = models.SlugField(
        "Slug короткой ссылки",
        max_length=100,
        default=uuid.uuid4(),
        unique=True,
        db_index=True,
    )
