from django.urls import path
from .views import Review

urlpatterns = [
    path('review/',Review,name='review'),
    path('review/<int:post_id>/',Review,name='review'),
]