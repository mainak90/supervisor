from src.execprocess import Exec
import logging, time
import subprocess

class Watcher(object):
    def __init__(self, commandlist, wait, interval, retry):
        self.commandlist = commandlist
        self.wait = wait
        self.interval = interval
        self.retry = retry

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
                    try:
                        Exec(command).executeCommand()
                    except Exception as e:
                        for i in range(int(self.retry) - 1):
                            try:
                                Exec(command).executeCommand()
                                time.sleep(float(self.interval))
                                break
                            except Exception as e:
                                logging.info('Failed to start the process ' +  command)
                                if i == int(self.retry) - 2:
                                    self.commandlist.remove(command)
                                    logging.error('Command ' + command + ' removed from commandlist as the it exceeded the number of configured retries')
            logging.info("Waiting for time " + str(self.wait) + " seconds to refresh the pid table")
            time.sleep(float(self.wait))


