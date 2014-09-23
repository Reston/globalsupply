from django.conf.urls import patterns, url

urlpatterns = patterns(
	'globalsupply.apps.productos.views',
	url(r'^categorias/$', 'mostrar_categoria', name="categoria"),
	url(r'^tipos/(?P<slug>[-\w]+)/$', 'mostrar_tipo', name="tipo"),
	url(r'^productos/(?P<slug>[-\w]+)/$', 'mostrar_producto', name="producto"),
	url(r'^producto_detalle/(?P<slug>[-\w]+)/$', 'detalle_producto', name="productodetalle"),	
)
