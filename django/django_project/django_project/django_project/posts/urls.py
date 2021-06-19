
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post', views.new_post, name='new_post'),
    path('new_post_form', views.new_post_form, name='new_post_form'),
    path('post/<int:id>', views.get_post, name='get_post'),
    path('edit_post_form',views.edit_post_form, name='edit_post_form'),
    path('post/<int:id>/edit',views.edit_post, name='edit_post'),
    path('post/<int:id>/delete',views.delete_post, name='delete_post'),
    path('post/<int:id>/fav',views.fav),
    path('post/<int:id>/unfav',views.unfav),
    path('post/<int:id>/like',views.like),
    path('post/<int:id>/unlike',views.unlike),
    path('my_post',views.my_post, name='my_post'),
    path('user/<int:id>/profile',views.poster_profile),
    path('category/<str:name>',views.category),
    path("my_fav",views.my_fav),
    path("comment_form",views.comment_form),
    path("comment/<int:id>/delete",views.delete_comment),
]
