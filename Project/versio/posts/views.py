from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from braces.views import SelectRelatedMixin
from django.views import generic
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView

from .import forms, models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def free_speech(request):
    return render(request, 'posts/free_speech.html')

def translation(request):
    return render(request, 'posts/translation.html')

class PostList(generic.ListView):
    model = models.Post
    
class MainPostList(generic.ListView):
    model = models.Post
    template_name ="posts/main_post_list.html"
    
class CreatePost(LoginRequiredMixin, generic.CreateView):
    fields = ('title', 'text')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

class PostDetail(HitCountDetailView):
    model = models.Post
    count_hit = True

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class UpdatePost(generic.UpdateView):
    model = models.Post
    fields =['title','text']
    success_url = reverse_lazy('posts:all')

 