from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.permissions import BasePermission, IsAdminUser, AllowAny, SAFE_METHODS
from django.views import View
from feeds.models import Post
from django.core import serializers
import random, re, html, json

from django.core.paginator import Paginator

class get_feed_page(APIView):
    
    def post(self, request):
        try:
            data = request.data
            
            pages = Paginator(Post.objects.all().order_by('created'), 8)
                        
            page = pages.page(data['page_num'])
            
            feeds = []
                        
            for post in page:
                
                #get img url
                #TODO: make it's own method
                img_src_regex = re.compile(r'\<img.+src\=(?:\"|\')(.+?)(?:\"|\')(?:.+?)\>')
                
                img_url = img_src_regex.search(post.body)
                
                if(img_url and img_url.group(1)):
                    img_url = img_url.group(1)
                
                #if the image body doesnt have an image tag, use the feed's source image
                if(not img_url):
                    img_url = post.source.image_url
                    
                post.feed_img = img_url
                
                #get desc
                #TODO: make it's own method
                p_regex = re.compile(r'\<\s*p[^>]*\>(.*)\<\s*/\s*p\>') # grab paragraph tags <p>
                
                tag_regex = re.compile(r'<[^>]*>') # grab all tags
                
                first_p = p_regex.search(post.body)
                
                if(first_p and first_p.group(1)):
                    first_p = p_regex.search(post.body).group(1) # get the first <p> text
                    desc = first_p 
                else:
                    desc = first_p 
                
                desc = tag_regex.sub('', desc) # remove any other tags within the <p>
                
                desc = html.unescape(desc) # convert html entities to normal text
                
                desc = desc[:200] # truncate down to 200 chars
                
                desc += '...' # add elipsis
                
                post.desc = desc
                
                feeds.append({
                    'title' : str(post.title),
                    'image' : str(img_url),
                    'desc' : str(desc),
                    'source' : str(post.source.name),
                    'link' : str(post.link),
                    'has_next' : page.has_next() # TODO: better way to do this - each feed post knows if this is the last page
                })
                
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
        
    #    (serializers.serialize('json', page), safe=False) 
        # return HttpResponse(serializers.serialize('json', page), status=200)
        # return HttpResponse(json.dumps(feeds), status=200)
        return HttpResponse(json.dumps(feeds), status=200)
    
    