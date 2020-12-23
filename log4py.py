#https://www.toptal.com/python/in-depth-python-logging
#https://www.programcreek.com/python/example/192/logging.Formatter
#https://programmer.help/blogs/python-logging-duplicate-log-problem.html

import logging
import logging.config
import io
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import tempfile

def get_tempfile_name(some_id = '0'):
    filename = os.path.join(tempfile.gettempdir(), next(tempfile._get_candidate_names()) + "_" + some_id + ".log")
    return filename;

class log4py:

    def __init__(   self, 
                    name = 'unknown', 
                    config_file = '', 
                    format_string='%(asctime)s - %(levelname)s - %(message)s', 
                    level = logging.DEBUG, 
                    filename = get_tempfile_name()):
        self.name = name;
        self.formatter = logging.Formatter(format_string);
        self.level = level;
        self.filename = filename;

    def __get_console_handler(self):
       console_handler = logging.StreamHandler(sys.stdout)
       console_handler.setFormatter(self.formatter)
       return console_handler

    def __get_file_handler(self):
       file_handler = TimedRotatingFileHandler(self.filename)
       file_handler.setFormatter(self.formatter)
       return file_handler

    def __get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.level) 
        self.console_handler = self.__get_console_handler()
        logger.addHandler(self.console_handler)
        self.file_handler = self.__get_file_handler()
        logger.addHandler(self.file_handler)
        return logger

    def DEBUG(self, text, function='', line='', file=''):
        self.logger = self.__get_logger(logger_name = self.name);
        self.logger.debug('%s - [file: %s - name: %s - line: %s]', text, file, function, line);
        self.logger.removeHandler(self.console_handler);
        self.logger.removeHandler(self.file_handler);

    def INFO(self, text, function='', line='', file=''):
        self.logger = self.__get_logger(logger_name = self.name);
        self.logger.info(' %s - [file: %s - name: %s - line: %s]', text, file, function, line);
        self.logger.removeHandler(self.console_handler);
        self.logger.removeHandler(self.file_handler);

    def ERROR(self, text, function='', line='', file=''):
        self.logger = self.__get_logger(logger_name = self.name);
        self.logger.error('%s - [file: %s - name: %s - line: %s]', text, file, function, line);
        self.logger.removeHandler(self.console_handler);
        self.logger.removeHandler(self.file_handler);

    def CRITICAL(self, text, function='', line='', file=''):
        self.logger = self.__get_logger(logger_name = self.name);
        self.logger.critical('%s - [file: %s - name: %s - line: %s]', text, file, function, line);
        self.logger.removeHandler(self.console_handler);
        self.logger.removeHandler(self.file_handler);

    def WARNING(self, text, function='', line='', file=''):
        self.logger = self.__get_logger(logger_name = self.name);
        self.logger.warning('%s - [file: %s - name: %s - line: %s]', text, file, function, line);
        self.logger.removeHandler(self.console_handler);
        self.logger.removeHandler(self.file_handler);

    def fileparts(self, inputFilepath):
        filename_w_ext = os.path.basename(inputFilepath)
        filename, file_extension = os.path.splitext(filename_w_ext)
        path, dummy = os.path.split(inputFilepath)
        return (path, filename, file_extension)
