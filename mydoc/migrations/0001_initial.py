# Generated by Django 2.2.7 on 2019-12-11 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobilenumber', models.CharField(max_length=50)),
                ('fk_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydoc.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mobilenumber', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('optiming', models.CharField(max_length=50)),
                ('opaddress', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('image', models.ImageField(upload_to='profile_picture/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydoc.Department')),
                ('fk_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydoc.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydoc.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydoc.Patient')),
            ],
        ),
    ]
