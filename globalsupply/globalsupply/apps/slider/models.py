# coding: utf-8
from django.db import models

class SliderItem(models.Model):
	title = models.CharField(max_length=140)
	image = models.ImageField(upload_to='imgslider',
	help_text="Se recomienda usar fotos de más de 800 de ancho por al menos 600 de alto, además de un tamaño aceptable para facilitar la carga de los usuarios.")
	texto_banner = models.TextField(max_length=145, help_text="Máximo 145 Caracteres.")
	texto_banner_en = models.TextField(max_length=145,  help_text="ENGLISH TITLE - Máximo 145 Caracteres.")

	def __unicode__(self):
		return self.title
