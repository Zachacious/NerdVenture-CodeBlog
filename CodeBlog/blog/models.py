from __future__ import unicode_literals

import datetime
from datetime import date

from django.utils.translation import gettext_lazy as _

from django import forms
from django.db import models
# from django.http import Http404, HttpResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format
from django.shortcuts import render

# import wagtail
from wagtail.admin.edit_handlers import (FieldPanel,
                                         StreamFieldPanel,
                                         ObjectList,
                                         TabbedInterface,
                                         MultiFieldPanel)
                                        #  FieldRowPanel,
                                        #  InlinePanel, 
                                        #  PageChooserPanel,
                                            
                                        #  HelpPanel, 
                                         
# from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core import blocks
from wagtail.core.fields import StreamField  # RichTextField,
from wagtail.core.models import Page  # Orderable
from wagtail.embeds.blocks import EmbedBlock
# from wagtail.images.blocks import ImageChooserBlock

from blog.blocks import ImageChooserBlock, ParallaxHeaderBlock, BlogPostListBlock

from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
# from wagtail.snippets.blocks import SnippetChooserBlock
# from wagtail.search.models import Query

# from blog.blocks import BlogListBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
# from modelcluster.tags import ClusterTaggableManager
# from taggit.models import Tag as TaggitTag
# from taggit.models import TaggedItemBase
# from wagtailmd.utils import MarkdownField, MarkdownPanel

from django.dispatch import receiver
from django.db.models.signals import pre_delete

from wagtail.core.signals import page_published
from wagtail.contrib.frontend_cache.utils import PurgeBatch

from wagtailmodelchooser.edit_handlers import ModelChooserPanel

from wagtailcodeblock.blocks import CodeBlock

from optin.blocks import OptinChooserBlock

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from author.models import AuthorProfile

from wagtailcache.cache import WagtailCacheMixin

from topic.models import Topic


class BlogIndexPage(WagtailCacheMixin, RoutablePageMixin, Page):
    ''' A page to list all the blog post. 
    Also used for category and search results.'''
    
    sidebar = models.ForeignKey(
        'sidebar.Sidebar',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        # help_text='Should be close to 400px X 100px'
    )
    
    settings_panels = Page.settings_panels + [
        SnippetChooserPanel('sidebar'),
    ]
    
    template = 'blog/blog_index_page.html'
    
    def get_context(self, request, *args, **kwargs):
        context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)
        
        context['blog_page'] = self
        # context['categories_all'] = BlogCategory.objects.all()
        
        paginator = Paginator(self.get_posts(), 10)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context['posts'] = posts
        context['route_title'] = 'All Post'
        
        return context

    def get_posts(self):
        return BlogPostPage.objects.live().order_by('-date')
        # return BlogPostPage.objects.descendant_of(self).live().order_by('-date')

    def get_paginated_posts(self, request, posts_per_page):
        paginator = Paginator(self.get_posts(), posts_per_page)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
            
        return {'posts': posts, 'paginator': paginator}

    @route('^$')
    def post_list(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        return Page.serve(self, request, *args, **kwargs)
    
    @route('^author/(?P<author>[-\w]+)/$', name="author")
    def post_by_author(self, request, author, *args, **kwargs):
        # Get blogs
        blogs = []
        articles = BlogPostPage.objects.live().all()
        for article in articles:
            if article.author_profile:
                blog_author = article.author_profile
                if blog_author.full_name_condensed().lower() == author.lower():
                    blogs.append(article)
                
        # print(request.GET)
            
        context = self.get_context(request)
        context['page'] = self
        context['posts'] = blogs
        context['route_title'] = 'Author'
        
        self.get_author_profile = AuthorProfile.get_author_from_full_name(author)

        return render(request, self.template, context)
    
    @route('^topic/(?P<topic_slug>[-\w]+)/$', name="topic")
    def post_by_topic(self, request, topic_slug, *args, **kwargs):                
        try:
            topic = Topic.objects.get(slug=topic_slug)
        except Exception:
            topic = None
                
        try:
            post = BlogPostPage.objects.live().filter(topics__in=[topic])
        except Exception:
            post = None
            
        print(topic)
        context = self.get_context(request)
        context['page'] = self
        context['posts'] = post
        context['route_title'] = 'Topic'
        context['sel_topic'] = topic
        
        return render(request, self.template, context)
    
    @route(r'^(\d{4})/$')
    @route(r'^(\d{4})/(\d{2})/$')
    @route(r'^(\d{4})/(\d{2})/(\d{2})/$')
    def post_by_date(self, request, year, month=None, day=None, *args, **kwargs):
        self.posts = self.get_posts().filter(date__year=year)
        if month:
            self.posts = self.posts.filter(date__month=month)
            df = DateFormat(date(int(year), int(month), 1))
            self.search_term = df.format('F Y')
        if day:
            self.posts = self.posts.filter(date__day=day)
            self.search_term = date_format(date(int(year), int(month), int(day)))
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
    def post_by_date_slug(self, request, year, month, day, slug, *args, **kwargs):
        post_page = self.get_posts().filter(slug=slug).first()
        if not post_page:
            raise Http404
        return Page.serve(post_page, request, *args, **kwargs)
    
    @route('^search/$')
    def search_post(self, request, *args, **kwargs):
        # Get blogs
        # blogs = CustomPage.objects.type(CustomPage).live()
        # items = self.get_posts().descendant_of(self).live()
        items = self.get_posts().live()
        
        search_query = request.GET.get('query', None)
        
        if search_query:
            items = items.search(search_query)
            
            # Log the query so Wagtail can suggest promoted results
            # Query.get(search_query).add_hit()
            
        else:
            items = Page.objects.none()
            
        context = self.get_context(request)
        context['page'] = self
        context['posts'] = items
        context['route_title'] = 'Search'
        
        self.search_term = search_query

        return render(request, self.template, context)
    
    def get_sitemap_urls(self, request):
        # return [] to remove page from sitemap
        sitemap = super().get_sitemap_urls(request)
        authors = AuthorProfile.objects.all()
        for author in authors:
            fullname = author.full_name_condensed()
            sitemap.append(
                {
                    'location': self.full_url + self.reverse_subpage('author', args=(fullname, )),
                    'lastmod': (self.last_published_at or self.latest_revision_created_at),
                    'priority': 0.1,
                    # 'changefreq': 'Monthly',
                }
            )
        
        return sitemap
    
    # attempt to invalidate paginated pages -- may need work
    def get_cached_paths(self):
        yield '/'
        paginator = Paginator(self.get_posts(), 10)
        for page_number in range(1, paginator.num_pages + 1):
            yield '/?page=' + str(page_number)


class BlogPostPage(WagtailCacheMixin, Page):
    ''' Page for blog post that facilitates a streamfield '''
    
    template = 'blog/blog_post_page.html'
    
    is_blog_post = True
    
    header_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+',
            # help_text='Should be close to 400px X 100px'
        )
    summary = models.TextField(_("Summary Text"), blank=True, max_length=200)
    date = models.DateTimeField(verbose_name="Post date", default=datetime.datetime.today)
    body = StreamField([
        # (_('Heading'), blocks.CharBlock(classname="full title")),
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        # (_('Quote'), blocks.BlockQuoteBlock()),
        # (_('Email'), blocks.EmailBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Code'), CodeBlock(label='Code Editor')),
        
    ],null=True,blank=True)
    
    sidebar = models.ForeignKey(
        'sidebar.Sidebar',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        # help_text='Should be close to 400px X 100px'
    )
    
    author_profile = models.ForeignKey(
        'author.AuthorProfile',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        # help_text='Should be close to 400px X 100px'
    )
    
    keywords = models.CharField(_("SEO Keywords"), max_length=255, blank=True)
    genre = models.CharField(_("SEO Genre"), max_length=255, blank=True)
    
    topics = ParentalManyToManyField('topic.Topic', blank=True)
    # categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    # tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image', widget=forms.CheckboxSelectMultiple),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
        
        # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        # FieldPanel('tags'),
    ]
    
    promote_panels = Page.promote_panels +[
        FieldPanel('genre'),
        FieldPanel('keywords'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
        ModelChooserPanel('author_profile'),
        SnippetChooserPanel('sidebar'),
        MultiFieldPanel(
            [
                FieldPanel("topics", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Topics"
        ),
    ]
    
    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(promote_panels, heading='SEO'),
            ObjectList(settings_panels, heading='Settings'),
        ]
    )
    
    def wordcount(self):
        count = 0
        for block in self.body:
            if block.block_type == 'Text':
                count += len(str(block.value).split())
            elif block.block_type == 'Rich_Text':
                count += len(str(block.value).split())
            elif block.block_type == 'Code':
                count += len(str(block.value).split())
                
        return count
    
    def read_time(self):
        return self.wordcount / 225
    
    
class CustomPage(WagtailCacheMixin, Page):
    ''' Any other type of page'''
    
    header = StreamField([
        # (_('Heading'), blocks.CharBlock(classname="full title")),
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Quote'), blocks.BlockQuoteBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Code'), CodeBlock(label='Code Editor')),
        (_('Parallax_Header'), ParallaxHeaderBlock()),
    ],null=True,blank=True)
    
    summary = models.TextField(_("Summary Text"), blank=True, max_length=200)
    date = models.DateTimeField(verbose_name="Post date", default=datetime.datetime.today)
    body = StreamField([
        # (_('Heading'), blocks.CharBlock(classname="full title")),
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Quote'), blocks.BlockQuoteBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Code'), CodeBlock(label='Code Editor')),
        (_('Recent_Post'), BlogPostListBlock()),
    ],null=True,blank=True)
    
    keywords = models.CharField(_("SEO Keywords"), max_length=255, blank=True)
    genre = models.CharField(_("SEO Genre"), max_length=255, blank=True)
    
    sidebar = models.ForeignKey(
    'sidebar.Sidebar',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    # help_text='Should be close to 400px X 100px'
    )
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('header'),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
    ]
    
    promote_panels = Page.promote_panels +[
        FieldPanel('genre'),
        FieldPanel('keywords'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
        SnippetChooserPanel('sidebar'),
    ]
    
    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(promote_panels, heading='SEO'),
            ObjectList(settings_panels, heading='Settings'),
        ]
    )
    
# Cache invalidation when post are published so that index pages will update
def blog_page_changed(thepage):
    batch = PurgeBatch()
    for blog_index in BlogIndexPage.objects.live():
        if thepage in blog_index.get_posts().object_list:
            batch.add_page(blog_index)
            
        batch.purge()
        
@receiver(page_published, sender=BlogPostPage)
def blog_published_handler(instance, **kwargs):
    blog_page_changed(instance)


@receiver(pre_delete, sender=BlogPostPage)
def blog_deleted_handler(instance, **kwargs):
    blog_page_changed(instance)