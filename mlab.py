import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds139890.mlab.com:39890/c4e21-blog

host = "ds139890.mlab.com"
port = 39890
db_name = "c4e21-blog"
user_name = "vukimoanh"
password = "oanh1234"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())