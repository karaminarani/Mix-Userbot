################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || PART OF ULTROID
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
import json
################################################################
import os
import random
import sys
from glob import glob
from typing import Any, Dict, List, Union

import requests
from team.nandev.class_log import LOGGER
from team.nandev.database import udB
from yaml import safe_load

from Mix.core.http import http

cek_bahasa = udB.get_bahasa()
from urllib.parse import quote, unquote

bahasa_ = {}
loc_lang = "langs/strings/{}.yml"


def load(file):
    if not file.endswith(".yml"):
        return
    elif not os.path.exists(file):
        file = loc_lang.format("en")
    code = file.split("/")[-1].split("\\")[-1][:-4]
    try:
        bahasa_[code] = safe_load(
            open(file, encoding="UTF-8"),
        )
    except Exception as er:
        LOGGER.info(f"Error in {file[:-4]}\n\n{er} language file")


load(loc_lang.format(cek_bahasa))


def cgr(key, _res: bool = True):
    lang = cek_bahasa
    try:
        return bahasa_[lang]
    except KeyError:
        try:
            en_ = bahasa_["en"]
            tr = en_
            if bahasa_.get(lang):
                bahasa_[lang] = tr
            else:
                bahasa_.update({lang: {tr}})
            return tr
        except KeyError:
            if not _res:
                LOGGER.info(f"Warning: could not load any string with the key ")
                return
        except Exception as er:
            LOGGER.info(f"Warning: could not load any string with the key `{er}`")
        if not _res:
            return None
        return bahasa_["en"] or LOGGER.info(f"Failed to load language string")


def get_cgr(key):
    doc = cgr(f"cgr_{key}", _res=False)
    if doc:
        return cgr("cmds") + doc


def get_bahasa_():
    for file in glob("langs/strings/*yml"):
        load(file)
    return {
        code: {
            "nama": bahasa_[code]["nama"],
            "penulis": bahasa_[code]["penulis"],
        }
        for code in bahasa_
    }
