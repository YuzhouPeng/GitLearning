# Generated by Django 2.0.1 on 2018-01-31 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_name', models.CharField(max_length=200)),
            ],
        ),
    ]