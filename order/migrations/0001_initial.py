# Generated by Django 3.2.8 on 2021-10-10 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0)),
                ('minimal_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('price_per_km', models.DecimalField(decimal_places=2, max_digits=100)),
                ('status', models.CharField(choices=[('processing', 'В обработке'), ('shipped', 'Отправлен'), ('delivered', 'Доставлен'), ('declined', 'Отменен')], max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oreders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
