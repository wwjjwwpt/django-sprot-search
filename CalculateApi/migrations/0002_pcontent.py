# Generated by Django 2.0 on 2020-05-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculateApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pcontent',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('Porder_id', models.CharField(max_length=10)),
                ('P_username', models.CharField(max_length=30)),
                ('P_userid', models.CharField(max_length=100)),
                ('C_content', models.CharField(max_length=30)),
                ('C_createdatetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('content_id',),
            },
        ),
    ]
