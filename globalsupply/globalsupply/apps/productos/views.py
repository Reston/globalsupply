#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Categoria, Producto, ImgProductos, Tipo
from django.shortcuts import get_object_or_404


def detalle_producto(request, titulo):
	servicio = False
	producto = get_object_or_404(Producto, titulo=titulo)
	imagenes = ImgProductos.objects.filter(producto=producto)
	if (producto.precio_dolares == 0):
		servicio = True
	ctx = {'producto': producto, 'imagenes': imagenes, 'servicio': servicio}
	return render_to_response('productos/producto.html', ctx, context_instance=RequestContext(request))

def mostrar_productos(request, titulo, template='productos/productos.html', page_template='productos/producto_lista.html'):
	mensaje = ''
	tipo = get_object_or_404(Tipo, slug=titulo)
	lista_tipos = Tipo.objects.all()
	productos = Producto.objects.filter(tipo=tipo.pk)
	imagenes = ImgProductos.objects.filter(producto__in=productos)
	if request.is_ajax():
		template = page_template
	if request.POST:
		palabra_busqueda = request.POST.get('busqueda', '')
		if (palabra_busqueda):
			productos = Producto.objects.filter(titulo__icontains=palabra_busqueda)
			if not (productos):
				mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {
		'tipo': tipo,
		'page_template': page_template,
		'productos': productos,
		'imagenes': imagenes,
		'lista_tipos': lista_tipos,
		'mensaje': mensaje
	}
	return render_to_response(template, ctx, context_instance=RequestContext(request))

def mostrar_tipos(request, template='homepage/tipos.html', page_template='homepage/tipos_lista.html'):
	palabra_busqueda = request.POST.get('busqueda', '')
	mensaje = ''
	tipos = Tipo.objects.all()
	if request.is_ajax():
		template = page_template
	if (palabra_busqueda):
		tipos = Tipo.objects.filter(titulo__icontains=palabra_busqueda)
		if not (tipos):
			mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {'tipos': tipos, 'page_template': page_template, 'mensaje': mensaje}
	return render_to_response(template, ctx, context_instance=RequestContext(request))


def mostrar_categorias(request, template='productos/categorias.html', page_template='productos/categorias_lista.html'):
	palabra_busqueda = request.POST.get('busqueda', '')
	mensaje = ''
	categorias = Categoria.objects.all()
	if request.is_ajax():
		template = page_template
	if (palabra_busqueda):
		categorias = Categoria.objects.filter(titulo__icontains=palabra_busqueda)
		if not (categorias):
			mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {'categorias': categorias, 'page_template': page_template, 'mensaje': mensaje}
	return render_to_response(template, ctx, context_instance=RequestContext(request))