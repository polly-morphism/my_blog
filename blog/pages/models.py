from django.db import models
from django.template.defaultfilters import slugify
import transliterate
from datetime import datetime
import time

class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=128)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    photo = models.ImageField(upload_to='blogposts', null = True, blank = True)

    def save(self, *args, **kwargs):
        self.created_at = str(datetime.now())
        if not self.id:
            self.slug = slugify(self.title)
            if self.slug == "":
                self.slug = slugify(transliterate.translit(self.title, reversed=True))
        super(BlogPost, self).save(*args, **kwargs)
