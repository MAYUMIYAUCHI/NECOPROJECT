
from django.urls import path
from . import indexfunc,listfunc

urlpatterns = [
    path('index/',indexfunc ),
    path('list/'listfunc),

]