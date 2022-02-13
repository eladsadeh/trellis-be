# Generated by Django 4.0.2 on 2022-02-13 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trellis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varieties', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planting',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planting',
            name='variety',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantings', to='trellis.variety'),
        ),
        migrations.AddField(
            model_name='crop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crops', to=settings.AUTH_USER_MODEL),
        ),
    ]