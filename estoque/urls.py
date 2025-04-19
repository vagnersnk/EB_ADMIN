from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings


@login_required(login_url='/login/')
def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('', redirect_to_admin),  # Redireciona a raiz para o admin
    path('admin/', admin.site.urls),  # O Django admin.
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    # outras urls do seu projeto
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
