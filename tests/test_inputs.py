from test.support import captured_stdin
import datetime
import sys, os
path = os.path.join(os.path.dirname(__file__), '../src')
sys.path.append(path)

from inputs import (input_data, input_str, input_date, input_integer,
                    input_natural_number, input_positive_number, convert_str_date,
                    convert_str_natural_number, convert_str_positive_number, convert_str_y,
                    loop_input, input_yes_no, is_date, is_natural_number,
                    is_positive_number, convert_str_integer, is_integer)

def test_input_data():
    with captured_stdin() as stdin:
        stdin.write('q\n')
        stdin.seek(0)
        assert input_data('') is None
    with captured_stdin() as stdin:
        stdin.write('a\n')
        stdin.seek(0)
        assert input_data('') == 'a'

def test_input_str():
    with captured_stdin() as stdin:
        stdin.write('a\n')
        stdin.seek(0)
        assert input_str() == 'a'

def test_input_date():
    with captured_stdin() as stdin:
        stdin.write('2020-11-11\n')
        stdin.seek(0)
        assert input_date() == datetime.date(2020, 11, 11)

def test_input_integer():
    with captured_stdin() as stdin:
        stdin.write('10\n')
        stdin.seek(0)
        assert input_integer() == 10
    with captured_stdin() as stdin:
        stdin.write('0\n')
        stdin.seek(0)
        assert input_integer() == 0

def test_input_natural_number():
    with captured_stdin() as stdin:
        stdin.write('10\n')
        stdin.seek(0)
        assert input_natural_number() == 10

def test_input_positive_number():
    with captured_stdin() as stdin:
        stdin.write('10.5\n')
        stdin.seek(0)
        assert input_positive_number() == 10.5

def test_input_yes_no():
    with captured_stdin() as stdin:
        stdin.write('Y\n')
        stdin.seek(0)
        assert input_yes_no() == True

def test_convert_str_date():
    assert convert_str_date('2020-11-11') == datetime.date(2020, 11, 11)
    assert convert_str_date('a') == False

def test_convert_str_integer():
    assert convert_str_integer('10') == 10
    assert convert_str_integer('a') == False

def test_convert_str_natural_number():
    assert convert_str_natural_number('1') == 1
    assert convert_str_natural_number('a') == False

def test_convert_str_positive_number():
    assert convert_str_positive_number('1.5') == 1.5
    assert convert_str_positive_number('a') == False

def test_convert_str_y():
    assert convert_str_y('Y') == True
    assert convert_str_y('N') == None
    assert convert_str_y('a') == False

def test_loop_input():
    with captured_stdin() as stdin:
        stdin.write('q')
        stdin.seek(0)
        assert loop_input('', (lambda x: x)) is None
    with captured_stdin() as stdin:
        stdin.write('a')
        stdin.seek(0)
        assert loop_input('', (lambda x: x)) == 'a'
    with captured_stdin() as stdin:
        stdin.write('0')
        stdin.seek(0)
        assert loop_input('', (lambda x: int(x))) == 0

def test_is_date():
    assert is_date('2020-11-20') == True
    assert is_date('2020-13-20') == False
    assert is_date('a') == False

def test_is_natural_number():
    assert is_natural_number('10') == True
    assert is_natural_number('1') == True
    assert is_natural_number('0') == False
    assert is_natural_number('0.5') == False
    assert is_natural_number('-5') == False
    assert is_natural_number('a') == False

def test_is_integer():
    assert is_integer('10') == True
    assert is_integer('-10') == True
    assert is_integer('5.5') == False
    assert is_integer('a') == False

def test_is_positive_number():
    assert is_positive_number('5.5') == True
    assert is_positive_number('0') == False
    assert is_positive_number('-5.5') == False
    assert is_positive_number('a') == False
