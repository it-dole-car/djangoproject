from django.urls import path
from . import views

urlpatterns = [
    path('addemployer/', views.addemployer, name='addemployer'),
    path('data_list/', views.data_list, name='data_list'),
    path('updates_emp/<str:id>', views.updates_emp, name='updates_emp'),
    path('deleteEmp/<str:id>', views.deleteEmp, name='deleteEmp'),
    path('ajax/load-municipalities/', views.load_municipalities, name='ajax_load_municipalities'),
    path('ajax/load-barangay/', views.load_barangay, name='ajax_load_barangay'),
    path('render_pdf_view/<str:id>', views.render_pdf_view, name='render_pdf_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_login/', views.user_login, name='user_login'),
    path('', views.user_login, name='user_login'),
]