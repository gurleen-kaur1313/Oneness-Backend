# Generated by Django 3.1.3 on 2020-12-19 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protestId', '0004_calendar_date'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='protest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='protestId.protest'),
        ),
    ]