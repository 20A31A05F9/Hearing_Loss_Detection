# Generated by Django 4.2.5 on 2023-10-09 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0004_alter_userhearingdetectionmodels_user_dates_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'prediction',
            },
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]