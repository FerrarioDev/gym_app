# Generated by Django 4.2.7 on 2023-11-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='assistance_days',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='membership_expiry_date',
            field=models.DateField(blank=True, help_text="Date when the client's membership will expire", null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='membership_start_date',
            field=models.DateField(blank=True, help_text='Date when the client started their gym membership', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
