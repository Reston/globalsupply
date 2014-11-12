# coding: utf-8
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
#from decimal import Decimal
from django.template import defaultfilters


class Categoria(models.Model):
	titulo = models.CharField(max_length=50, help_text='Hasta 50 caracteres y solamente alfanuméricos', unique=True)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	destacado_index = models.BooleanField(default=False, help_text='Para salir en el index. Max 5 destacados.')
	imagen = models.ImageField(upload_to='imgcategorias', blank=True)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Marca'
		verbose_name_plural = 'Marcas'

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(Categoria, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('tipo', kwargs={u'slug': self.slug})


class Tipo(models.Model):
	categoria = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length=50, help_text='Hasta 50 caracteres y solamente alfanuméricos', unique=True)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	imagen = models.ImageField(upload_to='imgtipos', blank=True)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return unicode(self.titulo)+' - '+unicode(self.categoria)

	class Meta:
		verbose_name = 'Tipo de repuesto'
		verbose_name_plural = 'Tipos de repuestos'

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(Tipo, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('producto', kwargs={u'slug': self.slug})

class Producto(models.Model):
	tipo = models.ForeignKey(Tipo)
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos')
	codigo = models.CharField(max_length=20)
	existencia = models.IntegerField()
	descripcion_corta = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	descripcion = HTMLField()	
	precio = models.DecimalField(max_digits=30, decimal_places=2)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	disponible = models.BooleanField(default=True, help_text='Disponibilidad del producto')
	destacado = models.BooleanField(default=False, help_text='Para salir en el index, Max 6.')
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(Producto, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('productodetalle', kwargs={u'slug': self.slug})


class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')
