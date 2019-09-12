from django import template
from header.models import Header

register = template.Library()

@register.inclusion_tag("header/tags/header.html", takes_context=True)
def headers(context):
    request = context.get("request")
    
    return {
        "request": request,
        "headers": Header.objects.all(),
    }
