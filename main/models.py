from django.db import models
from PIL import Image
# Create your models here.

CONTENT_TYPES = (
    ('Image', 'Image'),
    ('Video', 'Video'),
    ('Audio', 'Audio'),
    ('Text', 'Text'),
)


class Content(models.Model):
    type = models.CharField( max_length=5, choices=CONTENT_TYPES)
    file = models.FileField()
    thumbnail = models.FileField(null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.type == 'Image':
            size = (200, 200)
            image = Image.open(self.file)
            image.thumbnail(size)
            image.save("media/"+str(self.file) + ".thm", "JPEG")
            self.thumbnail = (str(self.file) + ".thm")
