# Generated by Django 4.1.7 on 2023-03-11 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_images_boxdata_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='boxdata',
            name='finalDestination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.destinations'),
        ),
        migrations.AlterField(
            model_name='boxdata',
            name='packageType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.packages'),
        ),
    ]
