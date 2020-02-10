# Generated by Django 3.0.3 on 2020-02-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GhostPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isBoast', models.BooleanField()),
                ('content', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
