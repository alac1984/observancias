from django.views import generic
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from .decorators import check_recaptcha


class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 2

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

    context = {
        'post': post,
        'comments': Comment.objects.filter(post=post.id, parent__isnull=True),
        'form': form,
    }

    return render(request, "post.html", context)


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


