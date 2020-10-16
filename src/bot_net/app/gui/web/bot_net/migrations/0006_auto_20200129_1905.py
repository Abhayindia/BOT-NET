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


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('black_widow', '0005_auto_20200129_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webparsingjobmodel',
            old_name='parsing_tags',
            new_name='_parsing_tags',
        ),
        migrations.RenameField(
            model_name='webparsingjobmodel',
            old_name='parsing_type',
            new_name='_parsing_type',
        ),
    ]
