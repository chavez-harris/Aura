# Generated by Django 3.0.5 on 2020-11-20 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201102_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bls_url', models.CharField(max_length=100)),
                ('va', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Va')),
            ],
        ),
    ]
