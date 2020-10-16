"""
*********************************************************************************
*                                                                               *
* input_arguments.py -- Methods to parse the user input arguments.              *
*                                                                               *
********************** IMPORTANT Bot-net LICENSE TERMS **************************
*                                                                               *
* This file is part of Bot-net.                                                 *
*                                                                               *
* Bot-net is free software: you can redistribute it and/or modify               *
* it under the terms of the GNU General Public License as published by          *
* the Free Software Foundation, either version 3 of the License, or             *
* (at your option) any later version.                                           *
*                                                                               *
* Bot-net is distributed in the hope that it will be useful,                    *
* but WITHOUT ANY WARRANTY; without even the implied warranty of                *
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 *
* GNU General Public License for more details.                                  *
*                                                                               *
* You should have received a copy of the GNU General Public License             *
* along with Bot-net.  If not, see <http://www.gnu.org/licenses/>.              *
*                                                                               *
*********************************************************************************
"""


from django.db import migrations, models
import django.utils.timezone
import signal


class Migration(migrations.Migration):

    dependencies = [
        ('black_widow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebParsingJobModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.PositiveIntegerField(default=signal.Signals['SIGCONT'])),
                ('pid', models.PositiveIntegerField()),
                ('_pid_file', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('parsing_type', models.CharField(choices=[('1', 'Single Page'), ('2', 'Website Crawling')], max_length=50)),
                ('depth', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
