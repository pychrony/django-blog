from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestPostsFeed(Feed):
    title = "Latest Blog Posts"
    link = "/rss/"
    description = "Updates on the latest blog posts from my blog."

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text[:200]  # Show the first 200 characters of the post text

    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
