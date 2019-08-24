from django.urls import path
from .views import (PostList, CreatePost, DeletePost, UserPosts, PostDetail,
                    UpdatePost, comment_write, comment_remove, post_like, PostTOL,
                    TransPostList, FreePostList, AskTransList)

app_name = 'posts'
urlpatterns = [
    path('', PostList.as_view(), name="all"),
    path("new/", CreatePost.as_view(), name="create"),
    path("delete/<int:pk>/", DeletePost.as_view(), name="delete"),
    path("by/<username>/", UserPosts.as_view(), name="for_user"),
    path("by/<username>/<int:pk>/", PostDetail.as_view(), name="single"),
    path("update/<int:pk>", UpdatePost.as_view(), name="update"),
    path('<int:pk>/comment/', comment_write, name='comment_write'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('like/', post_like, name='post_like'),
    path('tag/<tag>', PostTOL.as_view(), name='tagged_object_list'),
    path('translation', TransPostList.as_view(), name="translation"),
    path('free', FreePostList.as_view(), name="free_speech"),
    path('asktrans', AskTransList.as_view(), name="ask_trans"),
]
