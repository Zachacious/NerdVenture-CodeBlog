from django.http import HttpResponse
from wagtail.core import hooks

@hooks.register('before_serve_document', order=-1)
def serve_document(document, request):
    subscribed = False
    
    if 'NV-Subscribed' in request.COOKIES:
        subscribed = request.COOKIES['NV-Subscribed']
                
    if not subscribed:
        return HttpResponse("<h2>NerdVenture.net<h2><p>You must be subscribed to download!</P>")
        
hooks.register('before_serve_document', serve_document)