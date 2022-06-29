from django.contrib import admin
from django.urls import path
from dataapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dataapp/ubah/<int:ubah_id>', ubah, name='ubah'),
    path('dataapp/hapus/<int:hapus_id>', hapus, name="hapus"),
    path('dataapp/tambah/', tambah, name='tambah'),
    path('dataapp/tabel_data/', tabel, name='tabel_data'),
    path('', index, name='index',),
]
