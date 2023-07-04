from django.conf import settings
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = tinymce_models.HTMLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-date"]
