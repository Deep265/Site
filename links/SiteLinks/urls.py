from django.urls import path
from . import views

app_name = 'site_links'


urlpatterns = [
    path('list/',views.LinkList.as_view(),name='all'),
    path('list/detail/<int:pk>/',views.LinkDetail.as_view(),name='detail'),
    path('new/',views.LinkCreate.as_view(),name='create'),
    path('delete/<int:pk>/',views.LinkDelete.as_view(),name='delete'),
    path('list/detail/update/<int:pk>/',views.LinkUpdateView.as_view(),name='update')
]