from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/<int:contact_num>', views.contact),

    # htmx
    path('hx/contact/<int:contact_num>', views.contact_info),
    path('hx/contact/<int:contact_num>/edit', views.edit_contact_info),
]
