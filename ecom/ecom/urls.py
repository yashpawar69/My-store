from django.conf import settings   # ✅ correct import
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

if settings.DEBUG:   # ✅ good practice
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
