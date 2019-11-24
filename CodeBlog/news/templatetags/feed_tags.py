from django import template

from feeds.models import Post

import random, re, html

from django.core.paginator import Paginator


register = template.Library()


@register.simple_tag(takes_context=True)
def get_feeds(context):
    context['feed_posts'] = Post.objects.all()
    return ''

@register.simple_tag(takes_context=True)
def get_feeds_page(context, page_num):
    pages = Paginator(Post.objects.all(), 10)
    context['feed_page'] = pages.page(page_num)
    return ''

@register.simple_tag(takes_context=True)
def get_random_size_cls(context):
    sizes = [
        '', # 1x1
        # 'grid2x1',
        # 'grid1x2',
        # 'grid2x2',
        # 'grid3x1',
        # 'grid1x3',
        # 'grid2x3',
        # 'grid3x2',
        # 'grid3x3'
    ]
    
    return random.choice(sizes)

@register.simple_tag()
def get_feed_img_url(post):
    img_src_regex = re.compile(r'\<img.+src\=(?:\"|\')(.+?)(?:\"|\')(?:.+?)\>')
    url = img_src_regex.search(post.body)
    if(url):
        return url.group(1)
    
    url = post.source.image_url
    
    return url

@register.simple_tag()
def get_desc(data):
    p_regex = re.compile(r'\<\s*p[^>]*\>(.*)\<\s*/\s*p\>') # grab paragraph tags <p>
    tag_regex = re.compile(r'<[^>]*>') # grab all tags
    desc = p_regex.search(data).group(1) # get the first <p> text
    desc = tag_regex.sub('', desc) # remove any other tags within the <p>
    desc = html.unescape(desc) # convert html entities to normal text
    desc = desc[:200] # truncate down to 200 chars
    desc += '...' # add elipsis
    return desc