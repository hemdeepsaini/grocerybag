from django.urls import path
from . import views

app_name='appweb'

urlpatterns = [
    path('', views.homepage.as_view(), name='homepage'),
    path('add', views.add, name='add'),
    path('redirect-to-updateform/<int:item_id>', views.update_redirection, name='update'),
    path('update/<int:item_id>', views.delete_add, name='delete_add'),
    path('delete/<int:pk>', views.ItemsDeleteView.as_view(), name='delete'),
    path('filter', views.filter, name='filter'),
]