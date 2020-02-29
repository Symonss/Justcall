# Generated by Django 3.0.3 on 2020-02-13 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='department',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Department'),
        ),
    ]
