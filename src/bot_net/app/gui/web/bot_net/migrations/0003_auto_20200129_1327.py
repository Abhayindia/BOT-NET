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
        ('black_widow', '0002_webparsingjobmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='webparsingjobmodel',
            name='parsing_tags',
            field=models.CharField(choices=[('ALL_TAGS', 'All Tags'), ('RELEVANT_TAGS', 'Relevant Tags ()'), ('FORM_TAGS', 'Form Tags (form, input, textarea, select, option)')], default='ALL_TAGS', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webparsingjobmodel',
            name='parsing_type',
            field=models.CharField(choices=[('SINGLE_PAGE', 'Single Page'), ('WEBSITE_CRAWLING', 'Website Crawling')], max_length=50),
        ),
    ]
