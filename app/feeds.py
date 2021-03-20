from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Últimas postagens do blog Observâncias"
    link = "/ultimas/"
    description = "Esse blog é um diário do seu autor. Falamos sobre assuntos variados aqui."

    def items(self):
        return Post.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])