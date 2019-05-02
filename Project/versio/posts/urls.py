from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("delete/<int:pk>/", views.DeletePost.as_view(), name="delete"),
    path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    path("update/<int:pk>",views.UpdatePost.as_view(),name="update"),
    path('<int:pk>/comment/', views.comment_write, name='comment_write'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('like/', views.post_like, name='post_like'),
    path('tag/<tag>',views.PostTOL.as_view(), name='tagged_object_list'),


    path('free_speech', views.free_speech, name='free_speech'),
    path('translation', views.translation, name='translation')
]