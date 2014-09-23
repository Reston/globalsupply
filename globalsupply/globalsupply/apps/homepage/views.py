#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from .forms import contactForm, boletinForm
from django.template import RequestContext
from django.core.mail import send_mail
from globalsupply.apps.productos.models import Producto, ImgProductos, Categoria
from zinnia.models import Entry
import nltk


def index(request):
	#gestion de suscripcion
	newsletter = True
	if request.method == 'POST':
		form = boletinForm(request.POST)
		if form.is_valid():
			form.save()
			newsletter = False
	else:
		form = boletinForm()
	#productos e imagenes de sus producto
	productos = Producto.objects.filter(destacado=True).order_by('creado_en')[:6]
	imagenes = ImgProductos.objects.filter(producto__in=list(productos))
	categoria = Categoria.objects.filter(destacado_index=True)[:5]
	#entradas de blog
	entradas = Entry.objects.order_by('-creation_date')[:3]
	for ent in entradas:
		quitar_html= nltk.clean_html(ent.content) 
		ent.content =  quitar_html[:65]
	ctx = {'productos': productos, 'imagenes': imagenes, 'categoria': categoria, 'form':form, 'newsletter':newsletter, 'entradas': entradas}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
	return render_to_response('homepage/quienesomos.html', context_instance=RequestContext(request))

def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
