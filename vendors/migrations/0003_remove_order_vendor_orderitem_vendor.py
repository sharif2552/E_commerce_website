# Generated by Django 4.1.3 on 2023-08-19 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_vendorproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='vendor',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
            preserve_default=False,
        ),
    ]
