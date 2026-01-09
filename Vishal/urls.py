from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from piks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chat_room, name='chat'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('send/', views.send_message),
    path('getMessages/', views.get_messages),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)