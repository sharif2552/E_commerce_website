# Generated by Django 4.1.3 on 2023-08-22 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_customer_vendor_remove_customerpermission_users_and_more'),
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.vendor'),
        ),
    ]