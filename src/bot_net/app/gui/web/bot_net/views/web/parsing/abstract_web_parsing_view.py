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

import os

from bot_net.app.env import APP_STORAGE_OUT
from bot_net.app.gui.web.bot_net.models import WebParsingJobModel
from bot_net.app.helpers.storage import check_folder
from bot_net.app.helpers.util import now
from bot_net.app.managers.parser import HtmlParser
from bot_net.app.services import JsonSerializer, MultiTask

from bot_net.app.gui.web.bot_net.views.abstract_job_view import AbstractJobView


class AbstractWebParsingView(AbstractJobView):
    """
    Abstract Web Parsing View
    """
    storage_out_dir = os.path.join(APP_STORAGE_OUT, 'web_parsing')
    check_folder(storage_out_dir)
    model_class = WebParsingJobModel

    if not os.access(storage_out_dir, os.X_OK):
        os.chmod(storage_out_dir, 0o0755)

    def _new_job(
            self,
            url: str,
            parsing_type: str,
            depth: int or str,
            tags: str,
            cookies: str
    ) -> WebParsingJobModel:
        if parsing_type == WebParsingJobModel.TYPE_SINGLE_PAGE:
            depth = 0
        else:
            depth = int(depth)

        job = WebParsingJobModel()
        job.url = url
        job.parsing_type = parsing_type
        job.parsing_tags = tags
        job.depth = depth
        job.json_file = os.path.join(self.storage_out_dir, now() + '_WEB_PARSING_.json')
        job.cookies = cookies

        def _web_parsing_callback(parsed_page: dict):
            """
            The callback function of crawler.
            This method writes the parsed pages in a json file
            :param parsed_page: The parsed page
            """
            JsonSerializer.add_item_to_dict(parsed_page.get('url'), parsed_page, job.json_file)

        job.pid_file = MultiTask.multiprocess(
            HtmlParser.crawl,
            (
                url,
                tags,
                _web_parsing_callback,
                depth,
                cookies,
            ),
            asynchronous=True,
            cpu=1
        )

        job.save()
        return job

    def _copy_job(self, job: WebParsingJobModel) -> WebParsingJobModel:
        return self._new_job(
            job.url,
            job.parsing_type_key(),
            job.depth,
            job.parsing_tags_key(),
            job.cookies
        )
