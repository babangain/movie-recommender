from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('reco/', include('reco.urls')),
    path('admin/', admin.site.urls),
]