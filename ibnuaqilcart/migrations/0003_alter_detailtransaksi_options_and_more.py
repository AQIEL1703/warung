# Generated by Django 4.2.7 on 2024-01-16 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibnuaqilcart', '0002_remove_transaksi_alamat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailtransaksi',
            options={'verbose_name_plural': 'Data Detail Transaksi'},
        ),
        migrations.AlterModelOptions(
            name='transaksi',
            options={'verbose_name_plural': 'Data Transaksi'},
        ),
        migrations.AddField(
            model_name='transaksi',
            name='alamat',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='kabupaten',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='kecamatan',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='kode_post',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='nama_belakang',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='nama_depan',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='no_transaksi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='provinsi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='status',
            field=models.CharField(blank=True, choices=[('Baru', 'Baru'), ('Lunas', 'Lunas')], default='Baru', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='tanggal_kirim',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='total_transaksi',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='whatsapp',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
