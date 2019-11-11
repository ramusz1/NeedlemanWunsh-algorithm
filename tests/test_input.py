import pytest

from input import *

def test_succes_read_seq():
    seq_a = read_sequence('tests/seq_a.txt', 5)
    assert seq_a == 'SAM'

def test_failed_read_seq():
    with pytest.raises(ValueError) as e:
        read_sequence('tests/seq_a.txt', 2)
    
def test_succesfull_config():
    config = parse_config('tests/good_config.txt')
    assert config['GAP_PENALTY'] == -2
    assert config['SAME'] == 5
    assert config['DIFF'] == -5
    assert config['MAX_SEQ_LENGTH'] == 1000
    assert config['MAX_NUMBER_PATHS'] == 5

def test_missing_values_in_config():
    with pytest.raises(KeyError) as e:
        parse_config('tests/missing_config.txt')

def test_wrong_type_values_in_config():
    with pytest.raises(ValueError) as e:
        parse_config('tests/wrong_type_config.txt')
