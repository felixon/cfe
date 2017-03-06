from django.contrib import admin
from .models import Join
# Register your models here.
class joinAdmin(admin.ModelAdmin):
    list_display = ['__str__','friends','timestamp', 'updated']
    class Meta:
        model = Join



admin.site.register(Join, joinAdmin)