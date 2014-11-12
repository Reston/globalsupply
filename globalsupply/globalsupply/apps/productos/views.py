#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Categoria, Producto, ImgProductos, Tipo
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def detalle_producto(request, slug):
	producto = get_object_or_404(Producto, slug=slug)
	imagenes = ImgProductos.objects.filter(producto=producto)
	ctx = {'producto': producto, 'imagenes': imagenes}
	return render_to_response('productos/producto_detalle.html', ctx, context_instance=RequestContext(request))

def mostrar_producto(request, slug, template='productos/productos.html', page_template='productos/producto_lista.html'):
	mensaje = ''
	tipo = get_object_or_404(Tipo, slug=slug)
	#lista_tipos = Tipo.objects.all()
	productos = Producto.objects.filter(tipo=tipo.pk)
	imagenes = ImgProductos.objects.filter(producto__in=productos)
	if request.is_ajax():
		template = page_template
	if request.POST:
		palabra_busqueda = request.POST.get('busqueda', '')
		if (palabra_busqueda):
			#buscar en titulo la palabra
			productos = Producto.objects.filter(titulo__icontains=palabra_busqueda)
			if not (productos):
				#buscar en codigo la palabra
				productos = Producto.objects.filter(codigo__icontains=palabra_busqueda)
				if not (productos):
					mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {
		'tipo': tipo,
		'page_template': page_template,
		'productos': productos,
		'imagenes': imagenes,
		#'lista_tipos': lista_tipos,
		'mensaje': mensaje
	}
	return render_to_response(template, ctx, context_instance=RequestContext(request))

def mostrar_tipo(request, slug, template='productos/tipos.html', page_template='productos/tipos_lista.html'):
	palabra_busqueda = request.POST.get('busqueda', '')
	mensaje = ''
	categoria = get_object_or_404(Categoria, slug=slug)
	tipos = Tipo.objects.filter(categoria__slug=slug)
	if request.is_ajax():
		template = page_template
	if (palabra_busqueda):
		tipos = Tipo.objects.filter(titulo__icontains=palabra_busqueda)
		if not (tipos):
			mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {'categoria': categoria, 'tipos': tipos, 'page_template': page_template, 'mensaje': mensaje}
	return render_to_response(template, ctx, context_instance=RequestContext(request))


def mostrar_categoria(request, template='productos/categoria.html', page_template='productos/categoria_lista.html'):
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


def busqueda_avanzada(request):
	palabra_busqueda = request.GET.get('busqueda', '')
	productos = Producto.objects.all()
	if (palabra_busqueda):
		productos = Producto.objects.filter(Q(titulo__icontains=palabra_busqueda) | Q(codigo__icontains=palabra_busqueda) | Q(tipo__titulo__icontains=palabra_busqueda) | Q(tipo__categoria__titulo__icontains=palabra_busqueda))
	paginator = Paginator(productos, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		producto_pagina = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		producto_pagina = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		producto_pagina = paginator.page(paginator.num_pages)
	ctx = {'producto_pagina': producto_pagina, 'productos': productos}
	return render_to_response('productos/busqueda.html', ctx, context_instance=RequestContext(request))