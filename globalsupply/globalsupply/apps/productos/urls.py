from django.conf.urls import patterns, url

urlpatterns = patterns(
	'globalsupply.apps.productos.views',
	url(r'^categorias/(?P<titulo>[-\w]+)/$', 'mostrar_categoria', name="categoria"),
	url(r'^tipos/(?P<titulo>[-\w]+)/$', 'mostrar_tipo', name="tipo"),
	url(r'^productos/(?P<titulo>[-\w]+)/$', 'mostrar_producto', name="producto"),
	url(r'^producto_detalle/(?P<titulo>[-\w]+)/$', 'detalle_producto', name="productoproducto"),	
)
