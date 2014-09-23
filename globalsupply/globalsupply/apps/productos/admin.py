from django.contrib import admin
#from django.contrib.contenttypes import generic
from .models import Categoria, Producto, Tipo, ImgProductos
from .forms import ProductoForm, CategoriaForm
from import_export.admin import ImportExportMixin


class CategoriaAdmin(admin.ModelAdmin):
	form = CategoriaForm
	prepopulated_fields = {'slug': ('titulo',)}
	list_display = ('titulo', 'breve_descripcion', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'breve_descripcion']


class TipoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	list_display = ('titulo', 'breve_descripcion', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'breve_descripcion']


class ImgProductosInline(admin.TabularInline):
	model = ImgProductos


class ProductoAdmin(ImportExportMixin, admin.ModelAdmin):
	form = ProductoForm
	prepopulated_fields = {'slug': ('titulo',)}
	list_display = ('titulo', 'codigo', 'existencia', 'descripcion_corta', 'tipo', 'destacado', 'disponible', 'creado_en', 'modificado_en',)
	list_display_links = ('titulo', 'descripcion_corta',)
	list_filter = ('disponible', 'destacado', 'tipo')
	search_fields = ['titulo', 'codigo', 'tipo__titulo']
	inlines = [
		ImgProductosInline,
	]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Producto, ProductoAdmin)
