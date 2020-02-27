import json, os, logging

class Parser(object):

    def __init__(self, jsonpath=None):
        self.jsonpath = jsonpath

    @property
    def parseJson(self):
        if self.jsonpath != None:
            _jsonpath = self.jsonpath
        elif os.path.exists("/etc/supervisor/supervisor.json"):
            _jsonpath = "/etc/supervisor/supervisor.json"
        elif "SUPERVISOR_CONFIG" in os.environ:
            _jsonpath = os.environ("SUPERVISOR_CONFIG")
        else:
            logging.info('Error setting config json path, exiting...')

        jsonfile = open(_jsonpath).read()
        jsondata = json.loads(jsonfile)
        return jsondata['commands'], jsondata['wait'], jsondata['interval']

