from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Subscriber

class SubscriberAdmin(ModelAdmin):
    model = Subscriber
    menu_label = 'Subscriber'
    menu_icon = 'user'
    # menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('email',
                    'subscribed',
                    'date',
                    'optin_used',
                    )
    list_filter = (
        'email',
        'subscribed',
        'date',
        'optin_used',
    )
    search_fields = (
        'email',
        'subscribed',
        'date',
        'optin_used',
    )
    
    readonly_fields = ('date','optin_used',)
    
modeladmin_register(SubscriberAdmin)