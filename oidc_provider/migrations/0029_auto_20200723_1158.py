# Generated by Django 2.2.14 on 2020-07-23 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oidc_provider', '0028_client_backchannel_logout_uri'),
    ]

    operations = [
        migrations.RunSQL(
            sql='DELETE FROM oidc_provider_token;',
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires_at', models.DateTimeField(verbose_name='Expiration Date')),
                ('_scope', models.TextField(default='', verbose_name='Scopes')),
                ('refresh_token', models.CharField(max_length=255, unique=True, verbose_name='Refresh Token')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.Client', verbose_name='Client')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Refresh Token',
                'verbose_name_plural': 'Refresh Tokens',
            },
        ),
        migrations.RemoveField(
            model_name='token',
            name='refresh_token_expire_at',
        ),
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oidc_provider.RefreshToken', verbose_name='RefreshToken'),
        ),
    ]