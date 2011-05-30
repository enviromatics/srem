from django.contrib.gis import admin
from models import Shapefile, Feature, \
Attribute, AttributeValue
admin.site.register(Shapefile, admin.ModelAdmin)
admin.site.register(Feature, admin.GeoModelAdmin)
admin.site.register(Attribute, admin.ModelAdmin)
admin.site.register(AttributeValue, admin.ModelAdmin)
 
