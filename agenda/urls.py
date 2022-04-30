from django.urls import path
from .views import list_addresses, list_contact, create_contact, update_contact, delete_contact

urlpatterns = [
    path('', list_contact, name='list_contact'),
    path('new', create_contact, name='create_contact'),
    path('update/<int:id>/', update_contact, name='update_contact'),
    path('delete/<int:id>/', delete_contact, name='delete_contact'),
    path('<int:id>/addresses', list_addresses, name='list_addresses')
]


# CRUD - CREATE, READ, UPDATE, DELETE