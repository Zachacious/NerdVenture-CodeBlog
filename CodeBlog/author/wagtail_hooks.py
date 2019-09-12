from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import AuthorProfile


class AuthorProfileAdmin(ModelAdmin):
    ''' The admin interface for AuthorProfile'''
    model = AuthorProfile
    menu_label = 'Author Profile'
    menu_icon = 'user'
    # menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    
    # filtering
    
    list_display = ('first_name',
                    'last_name',
                    'email',
                    # 'desc',
                    )
    list_filter = (
        'first_name',
        'last_name',
        'email',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    
    
modeladmin_register(AuthorProfileAdmin)
