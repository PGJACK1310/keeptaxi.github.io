# Generated by Django 4.1.4 on 2022-12-31 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverRegisteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30, null=True)),
                ('badge_number', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxiDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_no', models.CharField(max_length=15, null=True)),
                ('source', models.CharField(max_length=40, null=True)),
                ('destination', models.CharField(max_length=40, null=True)),
                ('price', models.IntegerField(null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.driverregisteration')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiDetailsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.DateField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.driverregisteration')),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.taxidetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.registeration')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_time', models.DateField(auto_now_add=True, null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('taxi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.taxidetails')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.registeration')),
            ],
        ),
    ]
