from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('app.urls') ),
    path('', include('paypal.standard.ipn.urls')),
    path('payments/', include('payments.urls', namespace='payments')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "APPNA South Texas Chapter"
admin.site.site_title = "APPNA Admin Portal"
admin.site.index_title = "Welcome to APPNA South Texas Chapter "