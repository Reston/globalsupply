from django.contrib import admin
#from django.contrib.contenttypes import generic
from .models import Categoria, Producto, Tipo, ImgProductos, ValorDolar
from .forms import ProductoForm, CategoriaForm


class CategoriaAdmin(admin.ModelAdmin):
	form = CategoriaForm
	list_display = ('titulo', 'breve_descripcion', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'breve_descripcion']


class TipoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'breve_descripcion', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'breve_descripcion']


class ImgProductosInline(admin.TabularInline):
	model = ImgProductos


class ProductoAdmin(admin.ModelAdmin):
	form = ProductoForm
	list_display = ('titulo', 'codigo', 'descripcion_corta', 'tipo', 'destacado', 'disponible', 'creado_en', 'modificado_en',)
	list_display_links = ('titulo', 'descripcion_corta',)
	list_filter = ('disponible', 'destacado', 'tipo')
	search_fields = ['titulo', 'codigo', 'tipo__titulo']
	inlines = [
		ImgProductosInline,
	]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ValorDolar)
