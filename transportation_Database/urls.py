
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from transportation import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
#Tyrannosaur-rex88
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('primecars/system/admin/', admin.site.urls),

    path('',include('transportation.urls')),
    path('',views.home, name='home'),
    #path('Gallery/',include('Gallery.urls')),
    path('reset/', auth_views.PasswordResetView.as_view(template_name='public/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='public/password_reset_done.html'), name='password_reset_done'),
    path('resetpass/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='public/password_reset_confirm.html'), name='password_reset_confirm'),
    path('resetpass/done/', auth_views.PasswordResetCompleteView.as_view(template_name='public/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/',include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
