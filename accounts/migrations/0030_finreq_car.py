# Generated by Django 3.1.7 on 2021-03-16 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20210312_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='finreq',
            name='car',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='car_id', to='accounts.sellcar'),
        ),
    ]