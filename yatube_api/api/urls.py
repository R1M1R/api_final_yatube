from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

jwt_patterns = [
    path('jwt/create/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/verify/',
         jwt_views.TokenVerifyView.as_view(),
         name='token_verify'),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(jwt_patterns)),
]
