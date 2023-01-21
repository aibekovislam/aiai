from django.contrib import admin
from django.urls import path
from core.views import *
from core import views
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.products, name='main'),
    path('product/<int:id>/', products_page, name="product"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)