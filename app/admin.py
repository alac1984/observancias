from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'description', 'author',
                    'status', 'created', 'modified', 'active')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'email', 'post', 'parent')
    list_filter = ('post', 'name', 'email')
    search_fields = ['name', 'email']
    summernote_fields = ('body',)

