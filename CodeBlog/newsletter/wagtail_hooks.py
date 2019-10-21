from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Subscriber, Newsletter


class NewsletterAdmin(ModelAdmin):
    model = Newsletter
    edit_template_name = 'newsletter/modeladmin/newsletter_admin_edit.html'
    menu_label = 'Newsletter'
    menu_icon = 'doc-empty'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',
                    'subject',
                    'fromEmail',
                    'target_subs',
                    'target_non_subs',
                    'emails_sent_last',
                    'opens_last',
                    'open_rate_last',
                    'last_sent_date',)
    list_filter = ('title',
                    'subject',
                    'fromEmail',
                    'target_subs',
                    'target_non_subs',
                    'emails_sent_last',
                    'open_rate_last',
                    'last_sent_date',)
    search_fields = ('title',
                    'subject',
                    'fromEmail',
                    'target_subs',
                    'target_non_subs',
                    'emails_sent_last',
                    'opens_last',
                    'open_rate_last',
                    'last_sent_date',)
    readonly_fields = ('emails_sent_last',
                       'opens_last',
                    'open_rate_last',
                    'last_sent_date',)

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
    

    
modeladmin_register(NewsletterAdmin)
modeladmin_register(SubscriberAdmin)