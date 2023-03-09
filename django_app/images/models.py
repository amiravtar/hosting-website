from django.db import models

def image_image_path(instance, filename):
    "Generate restaurant image path"
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "image_image/{0}.{1}".format(instance.title, filename.split(".")[-1])


# Create your models here.
class Image(models.Model):
    title = models.CharField(verbose_name="Title", max_length=20, unique=True)
    image = models.ImageField(
        verbose_name="Image",
        upload_to=image_image_path,
        height_field=None,
        width_field=None,
        max_length=None,
    )

    @property
    def get_photo_url(self):
        if self.image:
            return self.image.url
        return ""

    def __str__(self) -> str:
        return self.title
