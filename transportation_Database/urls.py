#Tyrannosaur-rex88

from django.contrib import admin #Django’s built-in admin interface
from django.urls import path, include, re_path #functions to define URL patterns

from django.conf import settings #access to settings like MEDIA_ROOT, DEBUG, and etc.
from django.conf.urls.static import static #for serving media files in development
from transportation import views #import views from the transportation app
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve #for serving static/media files in development
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views #built-in auth views (login, password reset, and etc.)

urlpatterns = [
    #these two lines allow direct access to media and static files during development
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    #admin panel URL
    path('primecars/system/admin/', admin.site.urls),

    #include all routes defined in the transportation app’s urls.py
    path('',include('transportation.urls')),

    #direct access to the home view
    path('',views.home, name='home'),
    #path('Gallery/',include('Gallery.urls')),

    #password reset flow using Django’s built-in auth views (with custom templates)
    path('reset/', auth_views.PasswordResetView.as_view(template_name='public/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='public/password_reset_done.html'), name='password_reset_done'),
    path('resetpass/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='public/password_reset_confirm.html'), name='password_reset_confirm'),
    path('resetpass/done/', auth_views.PasswordResetCompleteView.as_view(template_name='public/password_reset_complete.html'), name='password_reset_complete'),

    #Django Allauth (used for login, registration, social auth, and etc.)
    path('accounts/',include('allauth.urls')),
]

#if the app is in DEBUG mode, also serve uploaded media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
