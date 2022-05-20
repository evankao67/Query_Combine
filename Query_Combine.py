from cmath import log
from numpy import character
import json, requests, pg8000
import requests, base64
import re
import logging
from logging.handlers import TimedRotatingFileHandler
APITOKEN = "q4e/8vNE4XsYhmmp86dTIREUpCruDm4PJlx+rWfQ4oY="
SERVICE = "https://api.cresclab.com/openapi/v1/member/"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + APITOKEN
}
logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger()
filehandler = TimedRotatingFileHandler('./log/logging.log', 'D', 1, 60)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
try:
    with open('config.json', 'r') as f:
        DB_CONFIG = json.loads(f.read())
except Exception as e: 
    logging.exception("filename or db config error", e)
    

conn = pg8000.connect(database=DB_CONFIG["database"], user=DB_CONFIG["user"], password=DB_CONFIG["password"], host=DB_CONFIG["host"], port=DB_CONFIG["port"])

try:
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    sql = """SELECT clid,retuid FROM macc_clid_retuid_mapping_table"""
    cursor1.execute(sql)
    rowcount = cursor1.rowcount
    for num in range (0, rowcount):
        row = cursor1.fetchone()
        clid = row[0]
        Url = requests.utils.unquote(clid)
        tmp = base64.b64decode(Url + '=' * (-len(Url) % 4))
        ans = ""
        for i in range(len(tmp)):
            if tmp[i] > 47 and tmp[i] < 58:
                ans+=chr(tmp[i]) 
        print(ans)
        sql = """INSERT INTO macc_clid_decode_result(clid, memberid, created_time) VALUES (%(clid)s, %(memberid)s, current_timestamp)"""
        params = {
            'clid':clid,
            'memberid':ans
        }
        cursor2.execute(sql, params)
    cursor3 = conn.cursor()
    cursor4 = conn.cursor()
    sql = """SELECT memberid FROM macc_clid_decode_result"""
    cursor3.execute(sql)
    rowcount = cursor3.rowcount
    for num in range (0, rowcount):
        row = cursor3.fetchone()
        memberid = row[0]
        print(memberid)

        tag_list=""
        res = requests.get(SERVICE + "?member_id=" + memberid, headers = HEADERS).json()
        print(res)
        if len(res["results"]) == 0:
                continue
        for result in res["results"][0]["tags"]:
            tag_list = tag_list+result+", "
        
        sql = """INSERT INTO macc_query_by_member_id_tags (member_id, line_uid, tags,created_time) VALUES (%(lm)s, %(line_id)s, %(tags)s, current_timestamp)"""
        params = {
             'lm':memberid,
             'line_id':res["results"][0]["line_uid"],
             'tags':tag_list
        }
        cursor4.execute(sql, params)
except Exception as e:
    logging.exception(e)
finally:
    conn.commit()
    conn.close()
    exit()
    


