from django.db import models

class GhostPost(models.Model):
    isBoast = models.BooleanField()
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.content

    @property
    def total_count(self):
        return self.upvotes - self.downvotes