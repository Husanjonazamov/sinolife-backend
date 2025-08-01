# Generated by Django 5.1.3 on 2025-07-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_rename_first_anme_messagesmodel_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'To‘landi'), ('unpaid', 'To‘lanmadi')], default='unpaid', max_length=200, verbose_name='Tolov statusi'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('pending', 'Kutilmoqda'), ('accepted', 'Qabul qilindi'), ('rejected', 'Rad etildi'), ('completed', 'Yakunlandi')], default='pending', max_length=200, verbose_name='Status'),
        ),
    ]
