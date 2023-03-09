from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Host, HostCategory, HostSpecs

# Register your models here.


class SpecsTabularInline(admin.TabularInline):
    model = Host.specs.through
    extra = 1


class HostAdmin(admin.ModelAdmin):
    inlines = [SpecsTabularInline]
    list_display = [
        "title",
        "sub_title",
        "price",
        "category",
        "get_location_text",
        "link",
        "photo_tag",
    ]
    IMAGE_SIZE = 50
    exclude = ["specs"]

    def photo_tag(self, obj):
        return mark_safe(
            format_html(
                '<a href="{img}"><img src="{img}" style="width:{size}px;height={size}px;"></a>',
                img=obj.get_photo_url,
                size=self.IMAGE_SIZE,
            )
        )


class HostCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "photo_tag", "icon_tag"]
    IMAGE_SIZE = 50

    def photo_tag(self, obj):
        return mark_safe(
            format_html(
                '<a href="{img}"><img src="{img}" style="width:{size}px;height={size}px;"></a>',
                img=obj.get_photo_url,
                size=self.IMAGE_SIZE,
            )
        )

    def icon_tag(self, obj):
        return mark_safe(
            format_html(
                '<a href="{img}"><img src="{img}" style="width:{size}px;height={size}px;"></a>',
                img=obj.get_icon_url,
                size=self.IMAGE_SIZE,
            )
        )


class HostSpecsAdmin(admin.ModelAdmin):
    pass


admin.site.register(HostCategory, HostCategoryAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(HostSpecs, HostSpecsAdmin)
