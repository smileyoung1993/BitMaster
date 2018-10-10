# Generated by Django 2.0.6 on 2018-10-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='ADD_GBN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='AGE_GBN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='ASS_ETC',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='ASS_FIN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='ASS_REAL',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='CHUNG_Y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='DOUBLE_IN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='D_DAMBO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='D_JEONSEA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='D_JUTEAKDAMBO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='D_SHINYONG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='FOR_RETIRE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='INCOME_GBN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='JOB_GBN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='MARRY_Y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_CHUNG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_CRD_SPD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_FUND',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_FUND_STOCK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_JEOK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_SAVING_INSUR',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_STOCK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='M_TOT_SAVING',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='NUMCHILD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='RETIRE_NEED',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='SEX_GBN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_ASSET',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_CHUNG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_DEBT',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_ELS_ETE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_FUND',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_JEOK',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_SOBI',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='TOT_YEA',
            field=models.IntegerField(default=0),
        ),
    ]
