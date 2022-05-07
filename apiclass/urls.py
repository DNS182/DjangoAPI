from . import views
from django.urls import path

urlpatterns = [
  path('list/' , views.SnippetList.as_view()),
  path('list/<int:pk>' , views.SnippetDetail.as_view())
]
