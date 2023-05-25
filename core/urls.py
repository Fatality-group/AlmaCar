from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', include('main_page.urls')),
    # path('account/', include('account.urls')),
    path('ServiceAdditional/', include('additional_service.urls')),
    path('condition/', include('condition.urls')),
    path('contact/', include('contact.urls')),
    path('personal_area/', include('personal_area.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
