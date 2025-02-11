# Generated by Django 5.1.4 on 2025-01-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='parent',
            name='child_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='contact_number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_name',
            field=models.CharField(max_length=100),
        ),
    ]
