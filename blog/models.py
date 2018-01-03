from django.db import models
from django.utils import timezone
from tinymce import HTMLField
import pytils

#from django.template.defaultfilters import slugify
#from autoslug import AutoSlugField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)
    #category = models.ForeignKey('articles.Categorie')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    text = HTMLField('Text')

    slug = models.SlugField(max_length=100, unique=True)
    def __unicode__(self):
        return self.title
    def save(self, **kwargs):
        if not self.id:
            self.slug = pytils.translit.slugify(self.title)
        return super(Post, self).save(**kwargs)

    #slug = models.SlugField(max_length=100, populate_from='title', unique=True, db_index=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
