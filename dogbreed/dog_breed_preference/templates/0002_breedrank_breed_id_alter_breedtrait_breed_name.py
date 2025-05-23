# Generated by Django 4.2.17 on 2024-12-12 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog_breed_preference', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breedrank',
            name='breed_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rank', to='dog_breed_preference.breed'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='breedtrait',
            name='breed_name',
            field=models.OneToOneField(db_column='breed_name', on_delete=django.db.models.deletion.CASCADE, related_name='traits', to='dog_breed_preference.breed'),
        ),
    ]
