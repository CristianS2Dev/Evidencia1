from django.conf import settings
from django.conf.urls.static import static
# URLS <<<TIENDA>>>

from django.urls import path
from .import views


urlpatterns =[
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("registrar/", views.registrar, name="registrar"),
    path("crear_producto/", views.crear_producto, name="crear_producto"),
    path("panel_admin/", views.panel_admin, name="panel_admin"),
    path("index_is/", views.index_is, name="index_is"),
    path("mi_perfil/", views.mi_perfil, name="mi_perfil"),
    path("mi_perfil_vendedor/", views.mi_perfil_vendedor, name="mi_perfil_vendedor"),
    path("user_panel_admin/", views.user_panel_admin, name="user_panel_admin"),
    path("product_panel_admin/", views.product_panel_admin, name="product_panel_admin"),
    path("vendedor_panel_admin/", views.vendedor_panel_admin, name="vendedor_panel_admin"),
    path("panel_producto/", views.panel_producto, name="panel_producto"),
    path("iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path("formulario_registrarse/", views.formulario_registrarse, name="formulario_registrarse"),
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)