from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from hosts.models import Host, HostCategory


class Index(View):
    template_name = "pages/index.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class About(View):
    template_name = "pages/about.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class Contact(View):
    template_name = "pages/contact.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class Domains(View):
    template_name = "pages/domains.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class Terms(View):
    template_name = "pages/terms.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class SingleDomain(View):
    template_name = "pages/single-domain.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class Hosting(View):
    template_name = "pages/hosting.html"

    def get(self, request, slug):
        host_cate = get_object_or_404(HostCategory, slug=slug, disabled=False)
        categories = HostCategory.objects.all()
        hosts_iran = Host.objects.filter(
            category__id=host_cate.id, location=Host.LOC_IRAN
        )
        hosts_ero = Host.objects.filter(
            category__id=host_cate.id, location=Host.LOC_EUROPE
        )
        return render(
            request=request,
            template_name=self.template_name,
            context={
                "host_iran": hosts_iran,
                "host_ero": hosts_ero,
                "host_cate": host_cate,
                "categories": categories,
            },
        )


def handler404(request, exception, template_name="base/error_404.html"):
    return render(request, template_name, status=404, context={"page404": True})
