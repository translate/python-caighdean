#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import json

import requests


class Translator(object):

    service_url = "http://borel.slu.edu/cgi-bin/seirbhis2.cgi"

    def __init__(self, src_lang="gd"):
        self.src_lang = src_lang
        self.target_lang = "ga"

    def request_params(self, phrase):
        return {
            "teacs": phrase,
            "foinse": self.src_lang}

    def make_request(self, params):
        return requests.post(self.service_url, params)
    
    def parse_response(self, msg):
        return " ".join([x[1] for x in json.loads(msg)])

    def translate(self, phrase):
        response = self.make_request(
            self.request_params(phrase))

        if not response.status_code == 200:
            raise TranslationError(
                "Unable to connect to translation service")
        return self.parse_response(response.content)
