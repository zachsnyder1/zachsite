import uuid
from django.db import models


class Entry(models.Model):
    """
    Blog entries.
    """
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    tagline = models.CharField(max_length=80)
    text = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
