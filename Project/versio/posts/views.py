from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Post
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.paginator import Paginator

# Create your views here.
def free_speech(request):
    return render(request, 'posts/free_speech.html')

def translation(request):
    return render(request, 'posts/translation.html')

class PostList(generic.ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all()
    
class MainPostList(generic.ListView):
    model = Post
    template_name ="posts/main_post_list.html"
    
class CreatePost(LoginRequiredMixin, generic.CreateView):
    fields = ('title','link', 'text', )
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
class UserPosts(generic.ListView):
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

class UpdatePost(generic.UpdateView):
    model = Post
    fields =['title','text']
    success_url = reverse_lazy('posts:all')

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
