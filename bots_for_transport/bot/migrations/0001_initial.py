# Generated by Django 4.2.4 on 2023-11-07 14:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=0, default=0, help_text='Введите скидку от автора в процентах (от 0 до 100).', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Скидку на категорию ботов',
                'verbose_name_plural': 'Скидки на категории ботов',
            },
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('main_photo', models.ImageField(upload_to='uploads/main/%Y/%m/%d/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Цена')),
                ('is_special_offer', models.BooleanField(default=False, verbose_name='Спецпредложение')),
            ],
            options={
                'verbose_name': 'Бот',
                'verbose_name_plural': 'Боты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_examples', models.ImageField(upload_to='uploads/examples/%Y/%m/%d/', verbose_name='Фото(образцы)')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_examples', to='bot.bot', verbose_name='Бот')),
            ],
            options={
                'verbose_name': 'Фото(образцы)',
                'verbose_name_plural': 'Фото(образцы)',
                'ordering': ('bot',),
            },
        ),
        migrations.CreateModel(
            name='CategoryBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.bot', verbose_name='Бот')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категории бота',
                'verbose_name_plural': 'Категории ботов',
            },
        ),
        migrations.CreateModel(
            name='BotDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=0, default=0, help_text='Введите скидку от автора в процентах (от 0 до 100).', max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
                ('bot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='discounts_author', to='bot.bot', verbose_name='Бот')),
            ],
            options={
                'verbose_name': 'Скидка на бота от автора',
                'verbose_name_plural': 'Скидки на ботов от авторов',
            },
        ),
    ]
