import os
import sys

import ntpath
import pickle
import configparser
from shlex import quote

def flush_print(item):
    """ Force prints the item to stdout """
    sys.stdout.write(str(item))
    sys.stdout.flush()

def make_dir(path):
    """ Ensures a given path name is a valid directory. Creates if needed """
    if not os.path.isdir(path):
        os.makedirs(path)

def file_exists(filename):
    """ Returns true if filename exists """
    return os.path.isfile(filename)

def dir_exists(directory):
    """ Retuns true if directory exists """
    return os.path.isdir(directory)

def files_exist(filelist):
    """ Given a list of files, returns true if all exist """
    for f in filelist:
        if not file_exists(f):
            return False
    return True

def ttt_files_exist(train_files, tune_files, test_files):
    """ Given 3 lists containing filenames, returns true if any exist """
    for ls in [train_files, tune_files, test_files]:
        if not files_exist(ls):
            return False
    return True

def strip_filename_from_path(filename):
    """ Removes any directory information from a string and returns only
    the filename information """
    return ntpath.basename(filename)

def wipe_file(filename):
    """ Removes the contents of file """
    open(filename, 'w').close()

def wipe_files(files):
    """ Wipes contents of the files in the list files """
    for f in files:
        wipe_file(f)

def ttt_wipe_files(train_files, tune_files, test_files):
    """ Wipes contents from three lists containing filenames"""
    for ls in [train_files, tune_files, test_files]:
        wipe_files(ls)

def isabsolute(path):
    """ Returns true if path is absolute """
    return os.path.isabs(path)

def config_file_reader():
    """ Creates a configparser and returns a dict containing config details """
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

def safe_string(s):
    """ Returns a shell safe quoted version of the provided string """
    return quote(s)

def same_until_char(s1, s2, symbol):
    """
    Returns True if strings s1 and s2 are the same up until a given symbol,
    after which they must be different.
    """
    index = 0
    while index < len(s1) and index < len(s2) and s1[index] == s2[index]:
        index += 1

    if index == 0:
        print("index 0")
        return False
    if index == max(len(s1), len(s2)):
        print("max len", index)
        return False

    symbol_pos = s1[:index].rfind(symbol)
    if symbol_pos == -1:
        print("no symbol")
        return False

    return True

def validate_config():
    """
    Creates a config parser object out of the config.ini file. Error
    checks the file for any mistakes
    """
    cf = config_file_reader()
    validate_splits(cf)

def valid_splits():
    return

    """
    Checks the user supplied valid train, test split values. The
    two values are valid if their sum is no more than 1
    """
    """
    train = config.getfloat("Iteration Settings", "train_split")
    test = config.getfloat("Iteration Settings", "test_split")
    valid = train + test <= 1.0

    if not valid:
        except ConfigError(f"Train and Test split values of {train}, {test} "
            "are invalid")
    """
