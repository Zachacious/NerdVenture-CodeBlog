from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_paginated_posts(context, page, post_per_page):
    return page.get_paginated_posts(context['request'], post_per_page)
