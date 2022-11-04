
from django.contrib import admin
from django.urls import path
from myapp.views import (
    home,
    index,
    index_json
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('index/',index ,name='index'),
    path('index/json/',index_json ,name='index_json'),
]
