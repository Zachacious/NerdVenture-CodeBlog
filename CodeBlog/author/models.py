from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmodelchooser import register_model_chooser

@register_model_chooser
class AuthorProfile(models.Model):
    ''' Basic Author Bio 
    - used on pages 
    - configured via admin/author profiles 
    - author pages can be accessed by the routable page /authors/<full-name>
        - configured in blog.blog_index_page'''
    
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    email = models.EmailField("Email", max_length=254)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    desc = RichTextField(blank=True)
    
    panels = [
        FieldRowPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
        ]),
        FieldPanel('email'),
        ImageChooserPanel('photo'),
        FieldPanel('desc', classname='full'),
    ]
    
    def full_name(self):
        ''' Returns the display version of the authors name '''
        return self.first_name + ' ' + self.last_name
    
    def full_name_condensed(self):
        ''' Returns the author's full name without spaces'''
        return self.first_name + self.last_name
    
    @classmethod
    def get_author_from_full_name(cls, name):
        ''' Returns an AuthorProfile object, if any, for the fullname given.
            - the name given should be the condensed full name of the author'''
        authors = AuthorProfile.objects.all()
        for author in authors:
            fullname = author.first_name + author.last_name
            if fullname.lower() == name.lower():
                return author
        return None
    
    def __str__(self):
        return self.full_name()
        