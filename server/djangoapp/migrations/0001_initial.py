from django.db import migrations, models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('car_type', models.CharField(choices=[('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon'), ('HATCHBACK', 'Hatchback'), ('COUPE', 'Coupe'), ('CONVERTIBLE', 'Convertible'), ('TRUCK', 'Truck'), ('VAN', 'Van')], max_length=20)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2025)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='djangoapp.carmake')),
            ],
            options={
                'ordering': ['-year', 'name'],
            },
        ),
    ] 