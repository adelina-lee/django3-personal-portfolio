from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('',
         views.all_blogs,
         name='all_blogs'),
    path('<int:blog_id>/',  # When someone comes to this url /blog, is there any path in this url that's an int?
         views.detail,
         name='detail'),
]
