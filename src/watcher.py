from src.execprocess import Exec
import logging, time
import subprocess

class Watcher(object):
    def __init__(self, commandlist, wait, interval):
        self.commandlist = commandlist
        self.wait = wait
        self.interval = interval

    def watch(self):
        while True:
            for command in self.commandlist:
                cmds = "ps -ef | grep '" + command +  "' | grep -v grep | awk '{print $2}'"
                ps = subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE)
                output = ps.stdout.read()
                ps.stdout.close()
                ps.wait()
                if output:
                    logging.info('Command ' + command + ' is running still, skipped by supervisor')
                else:
                    logging.info('Command ' + command + ' is not running, waiting for interval period ' + self.interval + ' seconds before restarting')
                    time.sleep(float(self.interval))
                    logging.info('Starting process ' + command + ' again...')
                    Exec(command).executeCommand()
            logging.info("Waiting for time " + str(self.wait) + " seconds to refresh the pid table")
            time.sleep(float(self.wait))


