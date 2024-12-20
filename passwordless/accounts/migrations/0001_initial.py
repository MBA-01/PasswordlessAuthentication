# Generated by Django 5.0.6 on 2024-05-27 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encrypted_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('USERCODE', models.CharField(max_length=200, unique=True)),
                ('First_Name', models.TextField(max_length=128)),
                ('Last_Name', models.TextField(max_length=128)),
                ('Address', models.TextField(max_length=128)),
                ('Phone', models.TextField(max_length=128)),
                ('National_Identity_Code', models.TextField(max_length=128)),
                ('BirthDate', models.TextField(max_length=128)),
                ('Country', models.TextField(max_length=128)),
                ('City', models.TextField(max_length=128)),
                ('Zip_Code', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Encryption_Keys',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Encryption_Code', models.CharField(max_length=128)),
                ('Generation_DateTime', models.DateTimeField()),
                ('Expiering_DateTime', models.DateTimeField()),
                ('USERCODE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.encrypted_data', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=55)),
                ('Phone_MAC_Address', models.CharField(max_length=23)),
                ('PC_MAC_Address', models.CharField(max_length=23)),
                ('Affiliation', models.TextField()),
                ('Inscription_Year', models.DateField()),
                ('Phone', models.CharField(max_length=14)),
                ('USERCODE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.encrypted_data', unique=True)),
            ],
        ),
    ]
