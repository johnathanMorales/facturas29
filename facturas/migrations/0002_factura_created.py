# Generated by Django 4.0.1 on 2022-02-24 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]