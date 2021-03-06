from django.contrib import admin
from .models import Usuario, Proyecto

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'fecha_nacimiento',
		'foto_perfil',
		'profesion',
		'presentacion',
		'enlace_referencias',
		'id'
		
		)

	search_fields =('user', 'profesion',)

class ProyectoAdmin(admin.ModelAdmin):
	list_display = (
		'nombre_proyecto',
		'descripcion_proyecto',
		'foto_proyecto',
		'foto_proyecto2',
		'fecha_publicacion',
		'nombre_usuario',
		'rubro',
		'id'
		
		)

	list_filter=('fecha_publicacion',
		'rubro',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
