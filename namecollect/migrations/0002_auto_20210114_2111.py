# Generated by Django 3.1.5 on 2021-01-14 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('namecollect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='namecollect.gender'),
        ),
    ]
