from django.urls import path
from . import views 
urlpatterns=[
path('',views.index,name='index'),
path('settings',views.settings,name='settings'),
path('like-post',views.like_post,name='like-post'),
path('comments',views.comments,name='comments'),
path('upload',views.upload,name='upload'),
path('signup',views.signup,name='signup'),
path('signin',views.signin,name='signin'),
path('logout',views.logout,name='logout')
]