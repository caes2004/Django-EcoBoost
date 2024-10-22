from django.contrib import admin
from.models import User
from .models import Producto
from django.utils.translation import gettext_lazy as _
# Register your models here.
admin.site.register(User)

admin.site.register(Producto)

# Cambiar el título del sitio
admin.site.site_header = _("Admin EcoBoost")

# Cambiar el título que aparece en la ventana del navegador
admin.site.site_title = _(" Admin")

# Cambiar el mensaje de bienvenida en la página de inicio del admin
admin.site.index_title = _("Bienvenido a la administración de Ecoboost")