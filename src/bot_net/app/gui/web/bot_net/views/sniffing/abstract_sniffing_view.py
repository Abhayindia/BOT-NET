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
from bot_net.app.helpers.storage import check_folder
from bot_net.app.helpers.util import now
from bot_net.app.managers.sniffer import PcapSniffer
from bot_net.app.services import JsonSerializer, MultiTask

from bot_net.app.gui.web.bot_net.models import SniffingJobModel
from bot_net.app.gui.web.bot_net.views.abstract_job_view import AbstractJobView


class AbstractSniffingView(AbstractJobView):
    """
    Abstract Sniffing View
    """
    storage_out_dir = os.path.join(APP_STORAGE_OUT, 'sniffing')
    check_folder(storage_out_dir)
    model_class = SniffingJobModel

    if not os.access(storage_out_dir, os.X_OK):
        os.chmod(storage_out_dir, 0o0755)

    def _new_job(self, filters: str, pcap: str, interfaces: list) -> SniffingJobModel:
        job = SniffingJobModel()
        job.filters = filters
        job.pcap_file = pcap
        job.interfaces = interfaces
        job.json_file = os.path.join(self.storage_out_dir, now() + '_SNIFFING_.json')

        def _sniffer_callback(pkt: dict):
            """
            The callback function of packet sniffer.
            This method writes the sniffed packets in a json file
            :param pkt: The sniffed packet
            """
            JsonSerializer.add_item_to_dict(pkt['number'], pkt, job.json_file)

        pcap_sniffer = PcapSniffer(
            filters=job.filters,
            src_file=job.pcap_file,
            interfaces=job.interfaces,
            limit_length=10000,
            callback=_sniffer_callback
        )

        job.pid_file = MultiTask.multiprocess(pcap_sniffer.start, asynchronous=True, cpu=1)
        job.save()

        return job

    def _copy_job(self, job: SniffingJobModel) -> SniffingJobModel:
        return self._new_job(
            job.filters,
            job.pcap_file,
            job.interfaces,
        )
