from django.contrib import admin

from .models import Organization
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'owner',
    )
    list_display_links = (
        'name',
    )    
    filter_horizontal = (
        'team',
    )      
admin.site.register(Organization,OrganizationAdmin)