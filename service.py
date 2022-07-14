import pandas as pd
import json
from datetime import datetime, timedelta
datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

keys = ["id","date","text", "views"]

def create_end_dict(raw_dict):
    if checking(raw_dict):
        try:
            post_type = "text"
            if raw_dict.get("text") is None:
                if raw_dict.get("caption") is None:
                    raw_dict["text"] = raw_dict["poll"]["question"]
                    post_type = "poll"
                else:    
                    raw_dict["text"] = raw_dict["caption"]
                    post_type = "image"
        except:
            print(raw_dict["id"])   
        d1 = {key: raw_dict[key] for key in keys}
        d2 = {react["emoji"]: react["count"] for react in raw_dict["reactions"]}
        d3 = {"type" : post_type}
        #d1.a
        return {**d1, **d2,**d3}
        
    else:
        return None


def checking(dict):
    if dict.get("reactions") is None:
        return False    
    return True

def get_datestring(date):
    res_date = date
    if type(date)== int:
        res_date =  datetime.today() - timedelta(days = date)      
    return res_date.strftime("%x")        
