from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment, Podcast


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'description', 'author',
                    'created', 'modified', 'active')
    list_filter = ('active',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'email', 'post', 'parent')
    list_filter = ('post', 'name', 'email')
    search_fields = ['name', 'email']
    summernote_fields = ('body',)

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'hero', 'url' )
    prepopulated_fields = {'slug': ('title',)}