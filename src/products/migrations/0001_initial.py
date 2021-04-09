# Generated by Django 2.0.7 on 2021-04-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('discription', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('summary', models.TextField()),
            ],
        ),
    ]
