from django.db import models
from django.urls import reverse_lazy


class HostSpecs(models.Model):
    TYP_MAIN = "main"
    TYP_SUB = "sub"
    TYP_CHOICE = [(TYP_MAIN, "اصلی"), (TYP_SUB, "جزعی")]

    title = models.CharField(verbose_name="Name", max_length=30)
    icon = models.ForeignKey(
        "images.Image",
        null=True,
        blank=True,
        verbose_name="Image",
        on_delete=models.SET_NULL,
    )
    detail = models.TextField(verbose_name="Detail", null=True, blank=True)
    slashed = models.BooleanField(verbose_name="Slashed", default=False)
    typ = models.CharField(verbose_name="Type", max_length=10, choices=TYP_CHOICE)

    def __str__(self) -> str:
        return f"{self.title},{str(self.slashed)}"


class HostCategory(models.Model):
    BADGE_NEW = "new"
    BADGE_SOON = "soon"
    BADGE_NONE = "none"
    BADGE_CHOICE = [(BADGE_NEW, "جدید"), (BADGE_SOON, "بزودی"), (BADGE_NONE, "بدون بج")]

    name = models.CharField(verbose_name="Name", max_length=30, blank=False, null=False)
    slug = models.SlugField(
        verbose_name="Slug Name", max_length=30, unique=True, blank=False, null=False
    )
    badge = models.CharField(
        verbose_name="Badge", max_length=10, default=BADGE_NONE, choices=BADGE_CHOICE
    )
    text = models.TextField(verbose_name="Description Text", blank=True, null=True)
    short_text = models.CharField(
        verbose_name="Short Description", max_length=80, default="", blank=True
    )
    image = models.ForeignKey(
        "images.Image",
        null=True,
        blank=True,
        verbose_name="Image",
        on_delete=models.SET_NULL,
    )
    icon = models.ForeignKey(
        "images.Image",
        null=True,
        blank=True,
        verbose_name="Icon",
        on_delete=models.SET_NULL,
        related_name="host_categories_icon"
    )
    disabled = models.BooleanField(verbose_name="DIsabled", default=False)

    @property
    def get_photo_url(self):
        if self.image:
            return self.image.get_photo_url
        return ""

    @property
    def get_icon_url(self):
        if self.icon:
            return self.icon.get_photo_url
        return ""

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        if self.disabled:
            return "#"
        return reverse_lazy("pages:Hosting", kwargs={"slug": self.slug})

    @property
    def get_badge_css_class(self):
        if self.badge == self.BADGE_NEW:
            return "st-new"
        elif self.badge == self.BADGE_SOON:
            return "st-soon"
        else:
            return ""


class Host(models.Model):
    LOC_IRAN = "iran"
    LOC_EUROPE = "europe"
    LOCATION_CHOICE = [(LOC_IRAN, "ایران"), (LOC_EUROPE, "اروپا")]
    category = models.ForeignKey(
        HostCategory, verbose_name="Category", on_delete=models.PROTECT
    )
    title = models.CharField(verbose_name="Name", max_length=25)
    sub_title = models.CharField(verbose_name="Sub Title", max_length=25)
    image = models.ForeignKey(
        "images.Image",
        null=True,
        blank=True,
        verbose_name="Image",
        on_delete=models.SET_NULL,
    )
    link = models.URLField(verbose_name="Url to Host in whmcs", max_length=200)
    price = models.IntegerField(verbose_name="Price (Toman)", null=False, blank=False)
    sub_price = models.CharField(verbose_name="Sub Price", max_length=40)
    location = models.CharField(
        verbose_name="Location",
        max_length=15,
        blank=False,
        null=False,
        choices=LOCATION_CHOICE,
    )
    trending = models.BooleanField(verbose_name="Trending", default=False)
    specs = models.ManyToManyField(HostSpecs, verbose_name="Specs")

    @property
    def get_location_text(self):
        location_choices_dict = dict(self.LOCATION_CHOICE)
        return location_choices_dict[self.location]

    @property
    def get_photo_url(self):
        if self.image:
            return self.image.get_photo_url
        return ""

    def __str__(self) -> str:
        return f"{self.title} ,{self.get_location_text} ,{self.sub_title}"
