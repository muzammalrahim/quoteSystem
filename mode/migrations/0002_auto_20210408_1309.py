# Generated by Django 3.2 on 2021-04-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mode', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comodity',
            options={'verbose_name': 'Comoditie'},
        ),
        migrations.AddField(
            model_name='mode',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
