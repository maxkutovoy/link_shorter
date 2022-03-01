from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='short_link'),
    path('<slug:link_slug>/', views.short_url_redirect, name='link_for_redirect')
    # path('<int:place_id>/', views.about_place)
]