#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from globalsupply.apps.productos.models import Categoria, Tipo, Producto

class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'monthly'

	def items(self):
		return [
				'homepageindex',
				'homepageabout',
				'homepagecontact',
				# colocar los nombre de las url en este lugar. ejemplo: 'homepageworks'
				]

	def location(self, item):
		return reverse(item)

class CategoriaSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Categoria.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en

class TipoSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Tipo.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en

class ProductoSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.8

	def items(self):
		return Producto.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en