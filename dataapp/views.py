from django.shortcuts import render, redirect
from .models import Data_Alumni
from django.contrib import messages
from .forms import DataForm


def index(request):
    data= {
        'judul' : 'SELAMAT DATANG',
        'isi' : '',
    }
    return render(request, 'index.html', data)

def tabel(request):
    tabel_data = Data_Alumni.objects.all()
    data = {
        'judul' : 'Data Alumni Darumuyiddin',
        'isi' : tabel_data,
    }
    return render(request, 'dataapp/tabel_data.html', data)


def tambah(request):
    tambah_data = DataForm(request.POST or None)
    if request.method == 'POST':
        if tambah_data.is_valid():
            tambah_data.save()
            messages.success(request, "Data Berhasil Di Simpan")
        return redirect('tabel_data')
    data = {
        'judul' : 'Tambah Data Alumni',
        'isi' : tambah_data,
    }
    return render(request, 'dataapp/tambah.html', data)

def hapus(request, hapus_id):
    hapus_data = Data_Alumni.objects.filter(id=hapus_id)
    hapus_data.delete()
    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('tabel_data')


def ubah(request, ubah_id):
    ubah_data = Data_Alumni.objects.get(id=ubah_id)
    data_alumni ={
        'nama' : ubah_data.nama,
        'alamat' : ubah_data.alamat,
        'pekerjaan' : ubah_data.pekerjaan,
        'no_hp' : ubah_data.no_hp,
        'jenis_kelamin' : ubah_data.jenis_kelamin,
        'angkatan' : ubah_data.angkatan,
    }
    data_alumni_form = DataForm(request.POST or None, initial=data_alumni, instance=ubah_data)
    if request.method == 'POST':
        if data_alumni_form.is_valid():
            data_alumni_form.save()
            messages.success(request, "Data Berhasil Di Ubah")
        return redirect('tabel_data')
    data = {
        'judul' : 'Ubah Data Alumni',
        'isi' : data_alumni_form,
    }
    return render(request, 'dataapp/tambah.html', data)