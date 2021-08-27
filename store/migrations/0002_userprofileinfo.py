# Generated by Django 3.2.2 on 2021-07-03 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(default='store/images/people_default.png', upload_to='store/images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
