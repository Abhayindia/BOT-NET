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


class Migration(migrations.Migration):

    dependencies = [
        ('black_widow', '0003_auto_20200129_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='webparsingjobmodel',
            name='json_file',
            field=models.CharField(default='---', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webparsingjobmodel',
            name='url',
            field=models.CharField(default='---', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webparsingjobmodel',
            name='parsing_tags',
            field=models.CharField(choices=[('all_parse', 'All Tags'), ('relevant_parse', 'Relevant Tags (a, script, link, Form Tags)'), ('form_parse', 'Form Tags (form, input, textarea, select, option)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='webparsingjobmodel',
            name='parsing_type',
            field=models.CharField(choices=[('single_page', 'Single Page'), ('website_crawling', 'Website Crawling')], max_length=50),
        ),
    ]
