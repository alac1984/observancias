import uuid
from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'post-heros/{uuid.uuid4()}.{ext}'
    return filename


STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)


class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Post(Base):

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    hero = StdImageField('Hero', upload_to=get_file_path, variations={
        'medium': {'width': 1200, 'height': 799, 'crop': True},
        'small': {'width': 800, 'height': 533, 'crop': True},
        'thumb': {'width': 400, 'height': 266, 'crop': True}
    }, blank=True)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created']

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

