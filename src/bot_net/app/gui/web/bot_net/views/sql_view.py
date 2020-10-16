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

from django.shortcuts import render, redirect

from bot_net.app.services import Log

from .abstract_view import AbstractView


class Sql:
    """
    SQL injection Container View
    """
    class SettingsView(AbstractView):
        """
        SQL View
        """
        name = 'sql-injection'
        # template_name = 'sql/settings.html'
        template_name = 'error/not_implemented.html'

        def get(self, request, *args, **kwargs):
            """
            :type request: django.core.handlers.wsgi.WSGIRequest
            :return: django.http.HttpResponse
            """
            # TODO: get current sql injection jobs
            view_params = dict()
            return render(request, self.template_name, view_params)

        def post(self, request):
            """
            :type request: django.core.handlers.wsgi.WSGIRequest
            :return: django.http.HttpResponseRedirect
            """
            # TODO: create new SQL injection job
            job_id = 0
            return redirect('sql/inject?job_id=' + str(job_id))

    class InjectView(AbstractView):
        """
        Injection View
        """
        name = 'sniffing'
        # template_name = 'sql/inject.html'
        template_name = 'error/not_implemented.html'

        def get(self, request, *args, **kwargs):
            """
            :type request: django.core.handlers.wsgi.WSGIRequest
            :return: django.http.HttpResponse
            """
            request_params: dict = request.GET.dict()
            job_id = request_params.get('job_id')
            Log.info("Showing job #" + str(job_id))
            return render(request, self.template_name)
