from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")


def productos(request):
    return render(request,"productos/productos.html")

def nosotros(request):
    return render(request,"nosotros.html")

def registrar(request):
    return render(request, "perfiles/registrar.html")


def iniciar_sesion(request):
    return render(request,"iniciar_sesion.html")



def crear_producto(request):
    return render(request,"productos/crear_producto.html")


def panel_admin(request):
    return render(request,"admin/panel_admin.html")


def index_is(request):
    return render(request,"index_is.html")


def mi_perfil(request):
    return render(request,"perfiles/mi_perfil.html")

def mi_perfil_vendedor(request):
    return render(request,"perfiles/mi_perfil_vendedor.html")

def user_panel_admin(request):
    return render(request,"admin/user_panel_admin.html")

def product_panel_admin(request):
    return render(request,"admin/product_panel_admin.html")

def vendedor_panel_admin(request):
    return render(request,"admin/vendedor_panel_admin.html")

def panel_producto(request):
    return render(request,"productos/panel_producto.html")

def iniciar_sesion(request):
    return render(request,"iniciar_sesion.html")


def formulario_registrarse(request):
    return render(request,"perfiles/formulario_registrarse.html")



