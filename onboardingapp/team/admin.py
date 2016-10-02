from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *
from .forms import UserCreationForm, UserChangeForm


class TeamUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm


    # ...
    fieldsets = ((None, {'fields': (
        'username',
        'email', 
        'password',
    )}),('Personal info', {'fields': (
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        # ...
        'account',
        'is_temp',
        'exp_date',
        'last4_card_num',
        'phone',
        'customer_id',
        'subscription_id',
    )}),('Permissions', {'fields': (
        'is_superuser',
    )}),)

    # ..
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'is_active', 'password1', 'password2')}
        ),
    )

    # ..
    filter_horizontal = ()    

    # ...
    list_display = ('id','username','email', 'is_active', 'is_superuser','account')
    list_display_links = ('username',)    
    list_filter = ('is_superuser','is_active')    
    search_fields = ('email','username')
    ordering = ('id',)

admin.site.register(TeamUser, TeamUserAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('pk','name','owner',)
    list_display_links = ('name',)
    filter_horizontal = ('admin','member','service','invited')        
admin.site.register(Team,TeamAdmin)

# admin.site.register(TeamUser)
admin.site.register(Service)
admin.site.register(Account)
