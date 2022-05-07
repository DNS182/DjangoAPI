from . import views
from django.urls import path

urlpatterns = [
  path('list/' , views.snippet_list),
  path('list/<int:pk>' , views.snippet_detail)
]
