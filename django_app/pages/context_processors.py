from django.conf import settings  # import the settings file
from hosts.models import HostCategory


def global_settings(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        "WHMCS_URL": settings.WHMCS_URL,
        "WHMCS_SIGHNUP": settings.WHMCS_SIGHNUP,
        "WHMCS_TICKET": settings.WHMCS_TICKET,
        "WHMCS_AFFILATE": settings.WHMCS_AFFILATE,
        "WHMCS_DOMAIN_SEARCH": settings.WHMCS_DOMAIN_SEARCH,
        "LORA_URL": settings.LORA_URL,
        "LORA_BLOG": settings.LORA_BLOG,
        "WHMCS_LOGIN": settings.WHMCS_LOGIN,
        "HOST_CATEGORIES": HostCategory.objects.all().only("name", "badge"),
    }
