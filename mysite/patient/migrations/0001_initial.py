# Generated by Django 3.2.1 on 2022-03-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
