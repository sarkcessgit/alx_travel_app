# add to alx_travel_app/urls.py
from django.urls import path
from listings.views import welcome

urlpatterns += [
    path('api/welcome/', welcome),
]
