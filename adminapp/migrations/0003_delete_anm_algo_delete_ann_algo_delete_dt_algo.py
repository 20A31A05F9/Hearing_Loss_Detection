# Generated by Django 4.2.5 on 2023-10-07 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_logistic_randomforest_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ANM_ALGO',
        ),
        migrations.DeleteModel(
            name='ANN_ALGO',
        ),
        migrations.DeleteModel(
            name='DT_ALGO',
        ),
    ]
