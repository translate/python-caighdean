# -*- coding: utf-8 -*-

import json

import pytest

import requests_mock

from caighdean import Translator
from caighdean.exceptions import TranslationError


def test_translator(mocker):
    translator = Translator()
    phrase = "asdf"
    assert translator.src_lang == "gd"
    assert translator.target_lang == "ga"
    assert (
        translator.request_params(phrase)
        == dict(teacs=phrase,
                foinse=translator.src_lang))

    with requests_mock.mock() as m:
        m.post(translator.service_url, text='[["bingo", "bingo"]]')
        result = translator.translate(phrase)
        assert result == "bingo"
        assert (
            m.request_history[0].text
            == (u'teacs=%s&foinse=%s'
                % (phrase, translator.src_lang)))

    with requests_mock.mock() as m:
        m.post(translator.service_url, status_code=403)
        with pytest.raises(TranslationError):
            translator.translate(phrase)


def test_translator_src_lang(mocker):
    translator = Translator("ga-IE")
    phrase = "asdf"
    assert translator.src_lang == "ga-IE"
    assert translator.target_lang == "ga"
    assert (
        translator.request_params(phrase)
        == dict(teacs=phrase,
                foinse=translator.src_lang))


def test_translator_detokenizer(mocker):
    translator = Translator()
    # phrase = 'Agus thubhairt e, \n "Iongantach!" an dèidh sin.'
    response = [
        [u'Agus', u'Agus'],
        [u'thubhairt', u'd\xfairt'],
        [u'e', u's\xe9'],
        [u',', u','],
        [u'\\n', u'\\n'],
        [u'"', u'"'],
        [u'Iongantach', u'Iontach'],
        [u'!', u'!'],
        [u'"', u'"'],
        [u'an d\xe8idh sin', u'ina dhiaidh sin'],
        [u'.', u'.']]
    result = translator.parse_response(json.dumps(response))
    assert (
        result
        == u'Agus d\xfairt s\xe9, \n "Iontach!" ina dhiaidh sin.')
