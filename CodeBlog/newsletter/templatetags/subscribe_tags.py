from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_subscribed(context):

    request = context.get("request")
    
    subscribed = False
    
    if 'NV-Subscribed' in request.COOKIES:
        subscribed = request.COOKIES['NV-Subscribed']
    
    # return {
    #     "is_subscribed": subscribed,
    # }
    context['subscribed'] = subscribed
    
    # return subscribed
    return ''
