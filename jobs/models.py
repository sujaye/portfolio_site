from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def summary_pretty(self):
        return self.title[:30]
