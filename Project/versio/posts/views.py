from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from hitcount.views import HitCountDetailView
from .forms import CommentForm
from .models import Post, Comment, Category
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

class PostList(ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all()
    
class MainPostList(ListView):
    model = Post
    template_name ="posts/main_post_list.html"
    queryset = Post.objects.exclude(category_id=4).order_by("-hit_count_generic__hits") #번역요청은 제외하고 출력, 조회수 순으로

class TransPostList(ListView):
    model = Post
    template_name = "posts/post_list.html"
    queryset = Post.objects.filter(category_id=1) #번역

class FreePostList(ListView):
    model = Post
    template_name = "posts/post_list.html"
    queryset = Post.objects.filter(category_id=2) #자유
    
class AskTransList(ListView):
    model = Post
    template_name = "posts/post_list.html"
    queryset = Post.objects.filter(category_id=4) #번역요청

class CreatePost(LoginRequiredMixin, CreateView):
    fields = ('title','link', 'text', 'tag', 'category')
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
class UserPosts(ListView):
    model = Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

class PostDetail(HitCountDetailView):
    model = Post
    count_hit = True

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class UpdatePost(UpdateView):
    model = Post
    fields =['title','text','tag','link','category']
    success_url = reverse_lazy('posts:all')

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'posts/tagging_post_list.html'

@login_required
def comment_write(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_writer = request.user
            comment.post = post
            comment.save()
            return redirect('posts:all')
    else:
        form = CommentForm()
    return render(request, 'posts/comment_form.html', {'form':form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('posts:all')

@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
    else:
        pass

    context = {'like_count': post.like_count}
    return HttpResponse(json.dumps(context), content_type="application/json")
   
