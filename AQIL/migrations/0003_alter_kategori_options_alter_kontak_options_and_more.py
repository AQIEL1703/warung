# Generated by Django 4.2.7 on 2023-12-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQIL', '0002_alter_produk_gambar_dua_alter_produk_gambar_empat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Data kategori'},
        ),
        migrations.AlterModelOptions(
            name='kontak',
            options={'verbose_name_plural': 'Data Kontak'},
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Data Profil'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name_plural': 'Data Slide'},
        ),
        migrations.AlterModelOptions(
            name='statis',
            options={'verbose_name_plural': 'Data Static'},
        ),
        migrations.AddField(
            model_name='produk',
            name='aktif',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='banner_satu',
            field=models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar',
            field=models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (575 x 200pixel)'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='gambar',
            field=models.ImageField(null=True, upload_to='gambar/profil', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='gambar_slide',
            field=models.ImageField(null=True, upload_to='gambar/slide', verbose_name='Gambar (575 x 200 pixel)'),
        ),
    ]
