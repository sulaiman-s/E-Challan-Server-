# Generated by Django 4.0.1 on 2022-01-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challan',
            fields=[
                ('challan_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=255)),
                ('vehicle_type', models.CharField(choices=[('Bike', 'Bike'), ('Car', 'Car'), ('Truck', 'Truck'), ('Bus', 'Bus')], default='Bike', max_length=255)),
                ('challan_amount', models.CharField(max_length=255)),
                ('challan_time', models.DateTimeField(auto_now=True)),
                ('challan_location', models.TextField()),
                ('challan_status', models.CharField(choices=[('Paid', 'Paid'), ('NotPaid', 'Not Paid')], default='NotPaid', max_length=255)),
            ],
        ),
    ]
