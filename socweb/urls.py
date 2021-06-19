from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import PostViewSet



router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.include_format_suffixes = False

# urlpatterns = router.urls
# print(urlpatterns)
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetails.as_view()),
    # path('posts/', views.PostList.as_view()),
    router.urls[0],
    router.urls[1],
    router.urls[2],
    router.urls[3],
    router.urls[4],
    router.urls[5],
    # path('posts/<int:pk>', views.PostDetail.as_view({'get': 'retrieve'})),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
