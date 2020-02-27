import subprocess, logging

class Exec(object):
    def __init__(self, command):
        self.command = command

    def executeCommand(self):
        logging.info("Triggering command " + self.command)
        try:
            subprocess.Popen(self.command, shell=True)
        except Exception as e:
            logging.error('Error encountered while starting process ' + self.command + ' error: ' + str(e))
        logging.info("Launched command " + self.command + " check linux process tree to verify...")

