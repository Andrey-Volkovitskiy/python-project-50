import json


def format(difference):
    '''Outputs a difference tree in JSON format

    Agruments:
        difference - tree of differences between two data structures

    Returns:
        ready to print JSON string
    '''
    prepared_dif = difference or None
    return json.dumps(prepared_dif, sort_keys=False, indent=4)
