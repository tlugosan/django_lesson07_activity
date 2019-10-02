from django.urls import path
from blogging.views import stub_view 
from blogging.views import list_view

urlpatterns = [
    path(r'', list_view, name="blog_index"),
    path(r'posts/(\d+)/', stub_view, name="blog_detail"),
]