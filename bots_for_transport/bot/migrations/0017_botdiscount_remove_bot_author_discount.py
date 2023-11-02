# Generated by Django 4.2.4 on 2023-11-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0016_bot_author_discount_delete_discountauthorbot'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotDiscount',
            fields=[
                ('bot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='discount', serialize=False, to='bot.bot')),
                ('author_discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Скидка автора')),
            ],
        ),
        migrations.RemoveField(
            model_name='bot',
            name='author_discount',
        ),
    ]
