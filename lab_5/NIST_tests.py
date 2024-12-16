import math
import mpmath

from work_with_files import *

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


def nist_frequency_bit_test(bit_sequence: str, file_path: str, key: str) -> None:

    try:
        sequence_else = [1 if bit == "1" else -1 for bit in bit_sequence]
        s_n = sum(sequence_else) / math.sqrt(len(sequence_else))
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_text_to_file(file_path, f'{key} : {p_v}\n')
    except ZeroDivisionError:
        print("Frequency bit test. Error: Division by zero")
    except Exception as e:
        print("Frequency bit test. Error: ", e)


def nist_identical_serial_bits(bit_sequence: str, file_path: str, key: str) -> None:

    try:
        n = len(bit_sequence)
        ones_count = bit_sequence.count("1")
        share_of_unit = ones_count / n
        if abs(share_of_unit - 0.5) < (2 / math.sqrt(n)):
            v_n = len([i for i in range(n - 1) if bit_sequence[i] != bit_sequence[i + 1]])
            p_v = math.erfc(abs(v_n - 2 * n * share_of_unit * (1 - share_of_unit)) /
                (2 * math.sqrt(2 * n) * share_of_unit * (1 - share_of_unit)))
        else:
            p_v = 0
           
        write_text_to_file(file_path, f'{key} : {p_v}\n')
    except ZeroDivisionError:
        print("Identical serial bits test. Error: Division by zero")
    except Exception as e:
        print("Identical serial bits test. Error: ", e)


def nist_longest_sequence(bit_sequence: str, file_path: str, key: str) -> None:

    try:
        n = len(bit_sequence)
        m = 8
        blocks = [bit_sequence[i:i + m] for i in range(0, n, m)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_count = 0
            count = 0
            for bit in block:
                count = count + 1 if bit == "1" else 0
                max_count = max(max_count, count)
            match max_count:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        xi_square = 0
        for i in range(4):
            xi_square += pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        p_v = mpmath.gammainc(3 / 2, xi_square / 2)
        write_text_to_file(file_path, f'{key} : {p_v}\n')
    except Exception as e:
        print("Test for the longest sequence of ones in a block. Error: ", e)