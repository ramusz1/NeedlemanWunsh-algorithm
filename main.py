import argparse
from solver import NeedlemanWunshSolver
import configparser
from collections import namedtuple


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


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run Needleman Wunsh algorithm on provided DNA sequences.')
    parser.add_argument('-a', dest='seq_a', type=str, nargs=1, help='first input sequence path')
    parser.add_argument('-b', dest='seq_b', type=str, nargs=1, help='second input sequence path')
    parser.add_argument('-c', dest='config', type=str, nargs=1, help='config path')
    parser.add_argument('-o', dest='output_path', type=str, nargs=1, help='output path')

    args = parser.parse_args()
    
    try:
        config = parse_config(args.config)
        seq_a = read_sequence(args.seq_a[0], config['MAX_SEQ_LENGTH'])
        seq_b = read_sequence(args.seq_b[0], config['MAX_SEQ_LENGTH'])    
        solver = NeedlemanWunshSolver(config['SAME'], config['DIFF'], config['GAP_PENALTY'], config['MAX_NUMBER_PATHS'], args.output_path[0])
        score_mat, directions = solver.find_score_matrix_with_directions(seq_a, seq_b)
        solver.find_possible_alignments(directions, seq_a, seq_b)
    
    except (KeyError, ValueError) as e:
        print(e)



