from django.db import models
from PIL import Image
from cv2 import cv2

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
        elif self.type == 'Video':
            vidcap = cv2.VideoCapture("media/"+str(self.file))
            vidcap.set(cv2.CAP_PROP_POS_MSEC, 1000)  # cue to 1 sec
            success, image = vidcap.read()
            print(success)
            print(image)
            if success:
                cv2.imwrite("media/"+str(self.file)+".jpg", image)
                size = (200, 200)
                image2 = Image.open("media/"+str(self.file)+".jpg")
                image2.thumbnail(size)
                image2.save("media/"+str(self.file) + ".thm", "JPEG")
                self.thumbnail = (str(self.file) + ".thm")
