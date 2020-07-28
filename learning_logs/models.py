from django.db import models

# Create your models here.
class Topic(models.Model):
        """A topic the user is learning about"""
        text = models.CharField(max_length=200)
        date_added = models.DateTimeField(auto_now_add=True)
    # Two fields
        def __str__(self):
            """ Return a string representation of the model."""
            return self.text
# different fields  https://docs.djangoproject.com/en/1.8/ref/models/fields/


class Entry(models.Model):
        """Journal entry under a topic """
        topic = models.ForeignKey(
            Topic,
            on_delete=models.CASCADE
            )
        text = models.TextField()
        date_added = models.DateTimeField(auto_now_add = True)

        class Meta:
            verbose_name_plural = 'entries'

        def __str__(self):
            """ Return a string representation of the mdoel """
            return self.text[:50] + "..."

    