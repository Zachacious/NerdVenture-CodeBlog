from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)

@register.simple_tag()
def get_menu_item_active_class(menu_item, pageurl):
    if menu_item.link == pageurl:
        return 'active'
    else:
        return ''