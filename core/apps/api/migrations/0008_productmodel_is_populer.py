# Generated by Django 5.1.3 on 2025-07-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_bannermodel_subtitle_ru_bannermodel_subtitle_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='is_populer',
            field=models.BooleanField(default=False, verbose_name='Mashhurmi ?'),
        ),
    ]
