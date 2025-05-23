# Generated by Django 4.2.17 on 2024-12-11 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('breed_id', models.AutoField(primary_key=True, serialize=False)),
                ('breed_name', models.CharField(max_length=100, unique=True)),
                ('links', models.URLField(max_length=500)),
                ('image_url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TraitDescription',
            fields=[
                ('trait_id', models.AutoField(primary_key=True, serialize=False)),
                ('trait', models.CharField(max_length=100, unique=True)),
                ('trait_1', models.CharField(max_length=100)),
                ('trait_5', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('affectionate_with_family', models.PositiveIntegerField()),
                ('good_with_young_children', models.PositiveIntegerField()),
                ('good_with_other_dogs', models.PositiveIntegerField()),
                ('shedding_level', models.PositiveIntegerField()),
                ('coat_grooming_frequency', models.PositiveIntegerField()),
                ('drooling_level', models.PositiveIntegerField()),
                ('coat_type', models.CharField(max_length=50)),
                ('coat_length', models.CharField(max_length=50)),
                ('openness_to_strangers', models.PositiveIntegerField()),
                ('playfullness_level', models.PositiveIntegerField()),
                ('watchdog_protective_nature', models.PositiveIntegerField()),
                ('adaptability_level', models.PositiveIntegerField()),
                ('trainability_level', models.PositiveIntegerField()),
                ('energy_level', models.PositiveIntegerField()),
                ('barking_level', models.PositiveIntegerField()),
                ('mental_stimulation', models.PositiveIntegerField()),
                ('breed_id', models.ForeignKey(db_column='breed_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_preferences', to='dog_breed_preference.breed')),
            ],
        ),
        migrations.CreateModel(
            name='BreedTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affectionate_with_family', models.PositiveIntegerField()),
                ('good_with_young_children', models.PositiveIntegerField()),
                ('good_with_other_dogs', models.PositiveIntegerField()),
                ('shedding_level', models.PositiveIntegerField()),
                ('coat_grooming_frequency', models.PositiveIntegerField()),
                ('drooling_level', models.PositiveIntegerField()),
                ('coat_type', models.CharField(max_length=50)),
                ('coat_length', models.CharField(max_length=50)),
                ('openness_to_strangers', models.PositiveIntegerField()),
                ('playfullness_level', models.PositiveIntegerField()),
                ('watchdog_protective_nature', models.PositiveIntegerField()),
                ('adaptability_level', models.PositiveIntegerField()),
                ('trainability_level', models.PositiveIntegerField()),
                ('energy_level', models.PositiveIntegerField()),
                ('barking_level', models.PositiveIntegerField()),
                ('mental_stimulation', models.PositiveIntegerField()),
                ('breed_name', models.OneToOneField(db_column='breed_name', on_delete=django.db.models.deletion.CASCADE, related_name='traits', to='dog_breed_preference.breed', to_field='breed_name')),
            ],
        ),
        migrations.CreateModel(
            name='BreedRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_2013', models.PositiveIntegerField()),
                ('rank_2014', models.PositiveIntegerField()),
                ('rank_2015', models.PositiveIntegerField()),
                ('rank_2016', models.PositiveIntegerField()),
                ('rank_2017', models.PositiveIntegerField()),
                ('rank_2018', models.PositiveIntegerField()),
                ('rank_2019', models.PositiveIntegerField()),
                ('rank_2020', models.PositiveIntegerField()),
                #('breed_name', models.OneToOneField(db_column='breed_name', on_delete=django.db.models.deletion.CASCADE, related_name='rank', to='dog_breed_preference.breed', to_field='breed_name')),
            ],
        ),
    ]
