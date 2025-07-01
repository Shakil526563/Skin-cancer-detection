from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from firstApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='homepage'),
    path('predictImage',views.predictImage,name='predictImage'),
    path('viewDataBase',views.viewDataBase,name='viewDataBase'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)