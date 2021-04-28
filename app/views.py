from django.views import generic
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Podcast
from .forms import CommentForm
from .decorators import check_recaptcha


@check_recaptcha
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and request.recaptcha_is_valid:
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = form.save(commit=False)
                    reply_comment.parent = parent_obj

            new_comment = form.save(commit=False)
            new_comment.post = post

            new_comment.save()

            messages.success(request, "Comentário adicionado com sucesso.")
            return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
        else:
            form = CommentForm()
            messages.error(request, "Houve um erro ao adicionar seu comentário.")

    print('post.hero.url', post.hero.url)
    context = {
        'post': post,
        'image': ".{}".format(post.hero.url),
        'comments': Comment.objects.filter(post=post.id, parent__isnull=True),
        'form': form,
    }

    return render(request, "post.html", context)


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


class IndexView(generic.ListView):
    queryset = Post.objects.filter(active=True).order_by('-created')
    template_name = 'index.html'
    paginate_by = 2

class PodcastView(generic.ListView):
    queryset = Podcast.objects.filter(active=True).order_by('-created')
    template_name = 'podcasts.html'
    paginate_by = 2

def search_result(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query) & Q(active=True)
    )
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(5)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    message = ""

    if paginator.count >= 2:
        message = "Encontramos {} postagens com os termos fornecidos".format(paginator.count)
    elif paginator.count == 1:
        message = "Encontramos 1 postagem com os termos fornecidos"
    else:
        message = "Não encontramos postagens com os termos fornecidos"

    context = {
        "query": query,
        "posts": posts,
        "message": message
    }

    return render(request, "search.html", context)



