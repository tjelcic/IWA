from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Ticket, Projection, Person

admin.site.register(Ticket)
admin.site.register(Projection)

class PersonAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff', 
            'is_superuser')  
    search_fields = ('email', 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Person, PersonAdmin)
