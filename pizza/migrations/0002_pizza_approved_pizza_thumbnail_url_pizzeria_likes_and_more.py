# Generated by Django 4.0.3 on 2022-03-14 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pizza',
            name='thumbnail_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Pizzeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.pizzeria'),
            preserve_default=False,
        ),
    ]
