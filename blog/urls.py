from django.urls import path
from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView, PostDeletelView, UserPostListView
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('terms/', views.termsOfUse, name="terms"),
    path('contact/', views.contactUs, name='contact'),
    path('sendEmails/', views.sendWeekMails, name='send_mail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/delete/', PostDeletelView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/new/error/', PostCreateView.as_view(), name='post-error'),
    path('about/', views.about, name='blog-about'),
    url(r'up/$', views.up_vote, name="up_vote"),
    url(r'down/$', views.down_vote, name="down_vote")
    ]
