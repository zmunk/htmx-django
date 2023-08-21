from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/<int:contact_num>/', views.contact),
    path('bulk-update/', views.bulk_update),

    # htmx
    path('hx/contact/<int:contact_num>/', views.contact_info),
    path('hx/contact/<int:contact_num>/edit/', views.edit_contact_info),
    path('hx/form/', views.seg_form),
    path('hx/activate', views.activate_rows),
    path('hx/deactivate', views.deactivate_rows),
]
