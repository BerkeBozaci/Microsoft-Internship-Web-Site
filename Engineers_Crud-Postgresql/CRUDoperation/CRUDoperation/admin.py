from calendar import c
import imp
from django.contrib import admin
from CRUDoperation.models import *

@admin.register(Learningpaths)
class LearningpathsAdmin(admin.ModelAdmin):
    list_display = ("learningpath_id","description")

@admin.register(Learningpathsteps)
class LearningpathstepsAdmin(admin.ModelAdmin):
    list_display = ("name","learningpath_id", "lp_step_id")

@admin.register(Mips)
class MipsAdmin(admin.ModelAdmin):
    list_display = ("mip_name","mip_id")