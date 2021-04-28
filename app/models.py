import uuid
from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True

class Post(Base):

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    hero = models.FileField()
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()

    class Meta:
        ordering = ['-created']
    
    def save(self, *args, **kwargs):
        self.hero.name = str(uuid.uuid4()) + self.hero.name
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField("Nome", max_length=80)
    email = models.EmailField("Email")
    body = models.TextField("Mensagem", max_length=1100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "comment_id {} | post_id {} | username {}".format(self.id, self.post, self.name)


class Podcast(Base):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=250)
    hero = models.FileField()
    url = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title