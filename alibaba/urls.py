"""
URL configuration for alibaba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ticketsales.views import tripListView,tripDetailsView,tripTimeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticketsales/trip/list', tripListView),   # dar bala ham farakhani mikonm.
    path('ticketsales/trip/details/<int:trip_id>',tripDetailsView),
    path('ticketsales/trip/time/',tripTimeView)



]
# zamnai ke hanooz ax k darim ro ru server upload nakrdim va mikhahim anha ra da mohit localhost bebebinim az in dastoor estefadeh mikonim.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


