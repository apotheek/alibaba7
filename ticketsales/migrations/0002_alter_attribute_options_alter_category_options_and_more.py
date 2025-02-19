# Generated by Django 5.0.6 on 2024-07-04 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': 'جزئیات', 'verbose_name_plural': 'جزئیات '},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته ها ', 'verbose_name_plural': 'دسته ها'},
        ),
        migrations.AlterModelOptions(
            name='categoryattribute',
            options={'verbose_name': 'جزئیات/دسته', 'verbose_name_plural': 'جزئیات/دسته '},
        ),
        migrations.AlterModelOptions(
            name='factor',
            options={'verbose_name': 'فاکتور', 'verbose_name_plural': 'فاکتور'},
        ),
        migrations.AlterModelOptions(
            name='login_admin',
            options={'verbose_name': 'ورود ادمین ', 'verbose_name_plural': 'ورود ادمین'},
        ),
        migrations.AlterModelOptions(
            name='login_user',
            options={'verbose_name': 'ورود کاربر ', 'verbose_name_plural': 'ورود کاربر'},
        ),
        migrations.AlterModelOptions(
            name='passenger',
            options={'verbose_name': 'مسافر', 'verbose_name_plural': 'مسافر'},
        ),
        migrations.AlterModelOptions(
            name='price_alibaba',
            options={'verbose_name': 'ورود ادمین ', 'verbose_name_plural': 'ورود ادمین'},
        ),
        migrations.AlterModelOptions(
            name='tiket',
            options={'verbose_name': 'بلیط', 'verbose_name_plural': 'بلیط'},
        ),
        migrations.AlterModelOptions(
            name='trip',
            options={'verbose_name': 'سفر', 'verbose_name_plural': 'سفر'},
        ),
        migrations.AlterModelOptions(
            name='tripattribute',
            options={'verbose_name': 'جزئیات سفر', 'verbose_name_plural': 'جزئیات سفر'},
        ),
        migrations.AlterField(
            model_name='attribute',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='نام  '),
        ),
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(max_length=100, verbose_name=' نام دسته'),
        ),
        migrations.AlterField(
            model_name='categoryattribute',
            name='AttributeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsales.attribute', verbose_name='نام جزئیات'),
        ),
        migrations.AlterField(
            model_name='categoryattribute',
            name='CategoryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Attribute', to='ticketsales.category', verbose_name='نام دسته  '),
        ),
        migrations.AlterField(
            model_name='factor',
            name='Passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsales.passenger', verbose_name='نام مسافر'),
        ),
        migrations.AlterField(
            model_name='factor',
            name='TotalPraice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='factor',
            name='TripAttribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsales.tripattribute', verbose_name='جزئیات سفر'),
        ),
        migrations.AlterField(
            model_name='login_admin',
            name='Email_user_Admin',
            field=models.EmailField(max_length=100, verbose_name='ایمیل '),
        ),
        migrations.AlterField(
            model_name='login_admin',
            name='First_name_Admin',
            field=models.CharField(max_length=100, verbose_name='نام '),
        ),
        migrations.AlterField(
            model_name='login_admin',
            name='Last_name_Admin',
            field=models.CharField(max_length=100, verbose_name=' نام خانوادگی '),
        ),
        migrations.AlterField(
            model_name='login_admin',
            name='Passwoord_user_Admin',
            field=models.CharField(max_length=50, verbose_name='پسورد '),
        ),
        migrations.AlterField(
            model_name='login_admin',
            name='Phone_number_Admin',
            field=models.CharField(max_length=11, verbose_name='تلفن '),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='Email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل '),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='First_name',
            field=models.CharField(max_length=100, verbose_name='نام '),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='Last_name',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی '),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='Passwoord',
            field=models.CharField(max_length=50, verbose_name='پسورد '),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='Phone_number',
            field=models.CharField(max_length=11, verbose_name='تلفن '),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='Email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='FirstName',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='LastName',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='price_alibaba',
            name='Price',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='قیمت '),
        ),
        migrations.AlterField(
            model_name='price_alibaba',
            name='Price_discount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True, verbose_name='قیمت تخفیف '),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='Passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsales.passenger', verbose_name='نام مسافر'),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='SeatNumber',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='شماره صندلی'),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='Attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsales.attribute', verbose_name='جزئیات'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='Name',
            field=models.CharField(max_length=100, verbose_name=' نام'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='Poster',
            field=models.ImageField(null=True, upload_to='TripImages/', verbose_name='پوستر'),
        ),
        migrations.AlterField(
            model_name='tripattribute',
            name='Value',
            field=models.CharField(max_length=255, verbose_name='مقدار'),
        ),
    ]
