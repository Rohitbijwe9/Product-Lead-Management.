# Generated by Django 5.1.1 on 2024-09-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='interested_products',
            field=models.ManyToManyField(blank=True, related_name='leads', to='myapp.product'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
