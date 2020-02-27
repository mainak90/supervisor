from src.parser import Parser
from src.watcher import Watcher
import src.logger
import argparse
import logging
import sys


def main(args=None):
    src.logger.setLevel()
    parser = argparse.ArgumentParser(description='Listed arguments --jsonpath')
    parser.add_argument("-p", "--jsonpath", help="[ OPTIONAL ] path to the supervisor json file")
    args = parser.parse_args()
    jsonpath = args.jsonpath
    logging.info('Starting program...')
    if jsonpath:
        commandlist, wait, interval = Parser(jsonpath=jsonpath).parseJson
    else:
        commandlist, wait, interval = Parser().parseJson
    logging.info('Starting watching the supervisable commands')
    try:
        Watcher(commandlist, wait, interval).watch()
    except Exception as e:
        logging.error('Error encountered while watching processes : ' + str(e))


if __name__ == '__main__':
    sys.exit(main())
