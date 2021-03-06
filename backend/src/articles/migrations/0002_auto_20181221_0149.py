# Generated by Django 2.1.4 on 2018-12-21 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('communication_score', models.IntegerField()),
                ('coding_score', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fractal_index', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Company'),
        ),
    ]
