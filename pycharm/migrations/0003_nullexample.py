# Generated by Django 4.0.4 on 2022-05-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycharm', '0002_dateexample'),
    ]

    operations = [
        migrations.CreateModel(
            name='NullExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
