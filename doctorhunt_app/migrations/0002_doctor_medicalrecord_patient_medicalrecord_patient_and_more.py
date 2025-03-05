# Generated by Django 5.1.6 on 2025-02-08 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorhunt_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('career', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('speciality', models.CharField(max_length=255)),
                ('stories', models.JSONField(default=dict)),
                ('rating', models.FloatField(default=0)),
                ('is_favourite', models.BooleanField(default=False)),
                ('reviews', models.IntegerField(default=0)),
                ('hour_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_slot', models.JSONField(default=dict)),
                ('details', models.JSONField(default=dict)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_info', models.JSONField(default=dict)),
                ('status', models.CharField(default='Active', max_length=50)),
                ('doctors', models.ManyToManyField(related_name='patients', to='doctorhunt_app.doctor')),
                ('medical_history', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='doctorhunt_app.medicalrecord')),
            ],
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorhunt_app.patient'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('location', models.JSONField(default=dict)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctorhunt_app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='doctorhunt_app.patient')),
            ],
        ),
    ]
