from django.shortcuts import render,redirect
from django.views import generic

from bases.views import SinPrivilegios
from .models import Cliente


class ClienteView(SinPrivilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required="fac.view_cliente"