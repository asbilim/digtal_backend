from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from website.views import ContactViewSet, NewsletterViewset , EmployeeViewset
from django.conf.urls.static import static
from django.conf import settings
router = SimpleRouter()

router.register('contact', ContactViewSet, basename='api-contact')
router.register('newsletter', NewsletterViewset, basename='api-newsletter')
router.register('employee', EmployeeViewset, basename='api-employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)