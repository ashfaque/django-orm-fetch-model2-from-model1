# Generated by Django 4.1.7 on 2023-02-19 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'model1',
            },
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model2_name', models.CharField(blank=True, max_length=255, null=True)),
                ('model1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model2_rn', to='testapp.model1')),
            ],
            options={
                'db_table': 'model2',
            },
        ),
    ]
