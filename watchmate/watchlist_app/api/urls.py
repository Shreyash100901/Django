from django.urls import path,include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import *

router=DefaultRouter()
router.register('stream', StreamPlatformAV, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAPIView.as_view(), name='movie-list' ),  
    path('<int:pk>', WatchListDetailsAPIView.as_view(), name='movie-detail'),
    path('',include(router.urls)),
    # path('stream/',StreamPlatformVS.as_view({'get': 'list'}),name='platforms'),
    # path('stream/<int:pk>', StreamDetailsAPIView.as_view(), name='platform-detail'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('stream/<int:pk>/review',ReviewList.as_view(),name="review-list"),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name="review-details")
    
    
]
