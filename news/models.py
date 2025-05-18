from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255, help_text="Comma-separated tags")
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
