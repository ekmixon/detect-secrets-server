import argparse
import json
import os

import yaml


def is_valid_file(path, error_msg=None):
    if not os.path.exists(path):
        if not error_msg:
            error_msg = f'File does not exist: {path}'

        raise argparse.ArgumentTypeError(error_msg)

    return path


def is_git_url(url):
    if not url.startswith('git@') and not url.startswith('https://'):
        raise argparse.ArgumentTypeError(f'"{url}" is not a cloneable git URL.')


def config_file(path):
    """
    Custom type to enforce input is valid filepath, and if valid,
    extract file contents.
    """
    is_valid_file(path)

    with open(path) as f:
        return yaml.safe_load(f.read())


def json_file(path):
    is_valid_file(path)

    with open(path) as f:
        return json.load(f)
