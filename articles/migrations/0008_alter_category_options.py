# Generated by Django 3.2.8 on 2021-11-22 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',)},
        ),
    ]
