from django.urls import path
from blogging.views import stub_view 
from blogging.views import list_view
from blogging.views import detail_view
from blogging.views import add_post

urlpatterns = [
    path(r'', list_view, name="blog_index"),
    
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    
    path(r'add_post/', add_post, name="add_post"),
]