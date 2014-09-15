# coding: utf-8
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from decimal import Decimal


class Categoria(models.Model):
	titulo = models.CharField(max_length=50, help_text='Hasta 50 caracteres y solamente alfanuméricos', unique=True)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	imagen = models.ImageField(upload_to='imgcategorias')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(Categoria, self).save(*args, **kwargs)

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('categoria', kwargs={'titulo': titulo})

class Tipo(models.Model):
	categoria = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length=50, help_text='Hasta 50 caracteres y solamente alfanuméricos', unique=True)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	imagen = models.ImageField(upload_to='imgtipos')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(Tipo, self).save(*args, **kwargs)

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('tipo', kwargs={'titulo': titulo})

class Producto(models.Model):
	tipo = models.ForeignKey(Tipo)
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos')
	codigo = models.CharField(max_length=20)
	descripcion_corta = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	descripcion = HTMLField()	
	precio = models.DecimalField(max_digits=30, decimal_places=2)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	disponible = models.BooleanField(default=True, help_text='Disponibilidad del producto')
	destacado = models.BooleanField(default=False, help_text='Para salir en el index')
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(Producto, self).save(*args, **kwargs)

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('productoproducto', kwargs={'titulo': titulo})


class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')
