# Generated by Django 4.0.2 on 2022-02-13 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('selected', models.BooleanField(default=False)),
                ('spacing', models.IntegerField(blank=True, default=0, null=True)),
                ('row_spacing', models.IntegerField(blank=True, default=0, null=True)),
                ('start_to_tp', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('tp_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('method', models.CharField(choices=[('DS', 'Direct Seeding'), ('TP', 'Transplanting')], max_length=2)),
                ('dtm', models.IntegerField()),
                ('seeds_oz', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='varieties', to='trellis.crop')),
            ],
        ),
    ]
