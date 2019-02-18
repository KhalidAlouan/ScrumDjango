from django.contrib import admin
from cor.models import *
# Register your models here.

class InLineSprint(admin.TabularInline):
	model=Sprint
	extra=1

class InLineSpec(admin.TabularInline):
	model=Spec
	extra=1
class ProjecteAdmin(admin.ModelAdmin):
	inlines=[InLineSprint,InLineSpec]

class SprintAdmin(admin.ModelAdmin):
	list_display=['projecte','data_inici','data_final','hores']

class SpecAdmin(admin.ModelAdmin):
	list_display=['projecte','dificultat','hores','descripcion']

admin.site.register(Projecte,ProjecteAdmin)
admin.site.register(Spec,SpecAdmin)
admin.site.register(Sprint,SprintAdmin)

