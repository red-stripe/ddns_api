# Generated by Django 3.1.4 on 2020-12-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodename', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('ip4', models.CharField(max_length=13)),
                ('location', models.CharField(blank=True, max_length=80)),
            ],
        ),
    ]
