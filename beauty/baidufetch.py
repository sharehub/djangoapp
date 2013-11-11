import sys
import urllib
import json

from sample.models import SearchKey, SearchData

def getjsondata(bdurl):
    if not bdurl:
        print("URL must prsent")
    bdict = json.load(urllib.urlopen(bdurl))
    bdimg = bdict.pop("data", None)
    searchkey = SearchKey(**bdict)
    searchkey.save()

    for img in bdimg:
        bdtemp = dict(img)
        if not bdtemp.has_key("is"):
            break
        bdtemp["bis"] = bdtemp.pop("is", None)
        searchdata = SearchData(**bdtemp)
        searchdata.key = searchkey
        searchdata.save()

