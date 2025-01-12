from django.urls import path
#from blogging.views import list_view, detail_view
from blogging.views import PostListView, PostDetailView, StubView

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),
    path('stub/', StubView.as_view(), name = 'stub_view'),
]