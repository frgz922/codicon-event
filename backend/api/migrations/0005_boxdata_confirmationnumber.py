# Generated by Django 4.1.7 on 2023-03-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_packages_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxdata',
            name='confirmationNumber',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
