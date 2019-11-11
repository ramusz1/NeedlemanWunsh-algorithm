import argparse
import configparser

def parse_config(path):
    config = configparser.ConfigParser(delimiters=[' '])
    config.read(path)

    keys = ['GAP_PENALTY', 'SAME', 'DIFF', 'MAX_SEQ_LENGTH', 'MAX_NUMBER_PATHS']
    parsed_config = {}
    for key in keys:
        if not key in config['DEFAULT']:
            raise KeyError(f"key: {key} not found in config")
        try:
            parsed_config[key] = config.getint('DEFAULT', key)
        except ValueError as e:
            raise ValueError(f'could not parse value of key: {key} as an integer')

    return parsed_config


def read_sequence(path, max_seq_length):
    with open(path, 'r') as f:
        lines = f.readlines()
        no_header = lines[1:]
        sequence = ''.join(no_header)
        sequence = sequence.replace('\n','')
        if len(sequence) > max_seq_length:
            raise ValueError('input sequence from file {path} is too long')

        return sequence


def parse_args():
    parser = argparse.ArgumentParser(description='Run Needleman Wunsh algorithm on provided sequences.')
    parser.add_argument('-a', dest='seq_a', type=str, help='first input sequence path')
    parser.add_argument('-b', dest='seq_b', type=str, help='second input sequence path')
    parser.add_argument('-c', dest='config', type=str, help='config path')
    parser.add_argument('-o', dest='output_path', type=str, help='output path')

    return parser.parse_args()