from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 2


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


class PostView(generic.TemplateView):
    template_name = 'post.html'
