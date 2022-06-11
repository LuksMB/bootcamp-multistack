from django.urls import URLPattern, path
from .views import AdoptionList

urlpatterns = [path("", AdoptionList.as_view())]
