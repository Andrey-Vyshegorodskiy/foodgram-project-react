from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/docs/', TemplateView.as_view(
         template_name='/api/docs/redoc.html'), name='redoc'),
    path('api/', include('api.urls')),
    path('api/', include('users.urls')),
    path('admin/', admin.site.urls),

]
