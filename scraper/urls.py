from .views import ReviewViewSet, scrape
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register('reviews', ReviewViewSet)

urlpatterns = [
path('',include(router.urls)),
path('scrape/',scrape)
]
