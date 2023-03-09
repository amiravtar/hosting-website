from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django import forms
from .models import Image
from django_svg_image_form_field import SvgAndImageFormField


# Register your models here.
class ImageForm(forms.ModelForm):
    # To accept svg
    class Meta:
        model = Image
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class ImageAdmin(admin.ModelAdmin):
    IMAGE_SIZE = 50
    list_display = ["title", "photo_tag"]
    form = ImageForm

    def photo_tag(self, obj):
        return mark_safe(
            format_html(
                '<a href="{img}"><img src="{img}" style="width:{size}px;height={size}px;"></a>',
                img=obj.get_photo_url,
                size=self.IMAGE_SIZE,
            )
        )


admin.site.register(Image, ImageAdmin)
