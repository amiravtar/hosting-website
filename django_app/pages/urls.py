from django.urls import path

from .views import Index, About, Contact, Domains, Terms, SingleDomain, Hosting

app_name = "pages"
urlpatterns = [
    path("", Index.as_view(), name="Index"),
    path("about/", About.as_view(), name="About"),
    path("contact/", Contact.as_view(), name="Contact"),
    path("domains/", Domains.as_view(), name="Domains"),
    path("terms/", Terms.as_view(), name="Terms"),
    path("single-domain/", SingleDomain.as_view(), name="SingleDomain"),
    path("<slug:slug>/", Hosting.as_view(), name="Hosting"),
]
