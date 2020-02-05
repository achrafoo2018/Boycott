from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from threading import Thread, Lock
import time


def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})

def contactUs(request):
    if request.method == "POST":
        receivers = []
        admins = User.objects.filter(is_superuser=True)
        for admin in admins:
            receivers.append(admin.email)
        if request.user.is_authenticated == True:
            subject = request.user.email + ", Subject : " + request.POST["subject"]
        else:
            subject = request.POST["email"] + ", Subject : " + request.POST["subject"]
        message = request.POST["message"]
        send_mail(subject, message, settings.EMAIL_HOST_USER, receivers, fail_silently=False)
        messages.success(request, f'Email Sent Successfully!')
        return redirect("contact")
    return render(request, 'blog/contact.html', {'title': 'Contact'})

def termsOfUse(request):
    return render(request, 'blog/terms.html', {'title': 'Terms'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # order of posts
    ordering = ['-rates']
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-rates')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        if Post.objects.all().filter(title=form.instance.title).exists() or Post.objects.all().filter(content=form.instance.content).exists():
             return HttpResponse("<script>alert('Post already exists!!');window.location.replace('../new')</script>")
        # print("Post title: {}".format(form.instance.title))
        # print(Post.objects.all().filter(title=form.instance.title).exists())
        return super().form_valid(form)

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return (self.request.user == post.author) or self.request.user.is_superuser

def about(request):
    return  render(request, 'blog/about.html', {'title': 'About'})

@login_required
def up_vote(request):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    if post.up_votes.filter(id=request.user.id).exists():
        post.up_votes.remove(request.user)
    else:
        if post.down_votes.filter(id=request.user.id).exists():
            post.up_votes.add(request.user)
            post.down_votes.remove(request.user)
        else:
            post.up_votes.add(request.user)
    # count number of upVoters and downVoters
    post.rates =  post.up_votes.count() - post.down_votes.count()
    post.save()
    context = {
        'post': post,
        'rates': post.rates
    }
    if request.is_ajax():
        html = render_to_string('blog/rates.html', context, request=request)
        return JsonResponse({'form': html})
    return HttpResponseRedirect(post.get_absolute_url())

@login_required
def down_vote(request):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    if post.down_votes.filter(id=request.user.id).exists():
        post.down_votes.remove(request.user)
    else:
        if post.up_votes.filter(id=request.user.id).exists():
            post.down_votes.add(request.user)
            post.up_votes.remove(request.user)
        else:
            post.down_votes.add(request.user)
    # count number of upVoters and downVoters
    post.rates =  post.up_votes.count() - post.down_votes.count()
    post.save()
    context = {
        'post': post,
        'rates': post.rates
    }
    if request.is_ajax():
        html = render_to_string('blog/rates.html', context, request=request)
        return JsonResponse({'form': html})
    return HttpResponseRedirect(post.get_absolute_url())


class sendWeekMails(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while 1:
            time.sleep(604800)
            users = User.objects.all()
            posts = Post.objects.all()
            max = -999999
            for post in posts:
                if post.rates > max:
                    max = post.rates
                    topPost = post
            subject = "Weekly Email by The Power !"
            for user in users:
                message = """Hello {}, we send you this email to let you know that the post that will be applied for next week is the post with\nTitle : {}.\nContent : {}\nWe Hope That everyone stick to the plan and do his part to make this thing possible.\nThe Power, We Make The Change !.""".format(user.username, topPost.title, topPost.content)
                send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
            print("Mails sent !")

th = sendWeekMails()
th.start()
