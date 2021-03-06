# Generated by Django 2.1.5 on 2019-03-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(null=True)),
                ('business', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'claim',
                'verbose_name_plural': 'claims',
                'ordering': ('-created',),
            },
        ),
    ]
