from django.urls import path
from app.views import ImageView


urlpatterns = [
    path('api/v1/', ImageView.as_view())
]