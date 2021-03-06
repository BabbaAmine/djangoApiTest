# Generated by Django 2.0.5 on 2018-12-08 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0002_auto_20181206_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('picture', models.CharField(blank=True, max_length=255)),
                ('created', models.DateField(blank=True, default=django.utils.datetime_safe.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
