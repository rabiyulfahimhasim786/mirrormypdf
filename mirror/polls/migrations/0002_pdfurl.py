# Generated by Django 3.2.5 on 2023-02-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdfurl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentname', models.CharField(max_length=255)),
                ('documenturl', models.URLField(max_length=255)),
                ('documenttype', models.CharField(max_length=255)),
            ],
        ),
    ]
