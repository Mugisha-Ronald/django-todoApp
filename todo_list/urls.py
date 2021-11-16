from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name= 'home'),
    path('delete/<list_id>', views.delete, name= 'delete'),
    path('cros_off/<list_id>', views.cros_off, name= 'cros_off'),
    path('uncross/<list_id>', views.uncross, name= 'uncross'),
    path('edit/<list_id>', views.edit, name= 'edit'),
]
