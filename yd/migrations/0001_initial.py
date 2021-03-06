# Generated by Django 3.1 on 2020-08-25 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fxd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(blank=True, default='Null', max_length=30)),
                ('date', models.DateField(blank=True)),
                ('acc_title', models.CharField(blank=True, default='Null', max_length=30)),
                ('toa', models.CharField(blank=True, default='Null', max_length=30)),
                ('cusocc', models.CharField(blank=True, default='Null', max_length=30)),
                ('cuspro', models.CharField(blank=True, default='Null', max_length=30)),
                ('sof', models.CharField(blank=True, default='Null', max_length=30)),
                ('doccol1', models.CharField(blank=True, default='Null', max_length=30)),
                ('doccol2', models.CharField(blank=True, default='Null', max_length=30)),
                ('doccol3', models.CharField(blank=True, default='Null', max_length=30)),
                ('coldocver', models.CharField(blank=True, default='Null', max_length=30)),
                ('addaccver', models.CharField(blank=True, default='Null', max_length=30)),
                ('benownacc', models.CharField(blank=True, default='Null', max_length=30)),
                ('passno', models.FloatField(blank=True)),
                ('passnorc', models.CharField(blank=True, default='Null', max_length=30)),
                ('passnover', models.CharField(blank=True, default='Null', max_length=30)),
                ('nid', models.FloatField(blank=True)),
                ('nidrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('nidver', models.CharField(blank=True, default='Null', max_length=30)),
                ('etin', models.FloatField(blank=True)),
                ('etinrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('etinver', models.CharField(blank=True, default='Null', max_length=30)),
                ('bcer', models.FloatField(blank=True)),
                ('bcerrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('bcerver', models.CharField(blank=True, default='Null', max_length=30)),
                ('vatreg', models.FloatField(blank=True)),
                ('vatregrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('vatregver', models.CharField(blank=True, default='Null', max_length=30)),
                ('comreg', models.FloatField(blank=True)),
                ('comregrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('comregver', models.CharField(blank=True, default='Null', max_length=30)),
                ('dl', models.FloatField(blank=True)),
                ('dlrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('dlver', models.CharField(blank=True, default='Null', max_length=30)),
                ('od', models.FloatField(blank=True)),
                ('odrc', models.CharField(blank=True, default='Null', max_length=30)),
                ('odver', models.CharField(blank=True, default='Null', max_length=30)),
                ('rfacf', models.CharField(blank=True, default='Null', max_length=30)),
                ('tv', models.CharField(blank=True, default='Null', max_length=30)),
                ('expdt', models.DateField(blank=True)),
                ('wpoa', models.CharField(blank=True, default='Null', max_length=30)),
                ('cpep', models.CharField(blank=True, default='Null', max_length=30)),
                ('abtsm', models.CharField(blank=True, default='Null', max_length=30)),
                ('cbif', models.CharField(blank=True, default='Null', max_length=30)),
                ('terr', models.CharField(blank=True, default='Null', max_length=30)),
                ('iyterr', models.CharField(blank=True, default='Null', max_length=30)),
                ('rg', models.CharField(blank=True, default='Null', max_length=30)),
                ('cmnt', models.CharField(blank=True, default='Null', max_length=30)),
            ],
        ),
    ]
