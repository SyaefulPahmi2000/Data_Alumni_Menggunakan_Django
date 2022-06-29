from django.db import models

class Data_Alumni(models.Model):
    jk = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    )
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    jenis_kelamin = models.CharField(max_length=10, choices=jk)
    angkatan = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.id, self.nama)