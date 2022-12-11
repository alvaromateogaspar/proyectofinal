from django.urls import path

from Formula1App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('',views.home, name="Inicio"),
    path ('escuderias',views.escuderias, name="Escuderias"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)