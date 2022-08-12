import math


def transform_to_basic_alphabet(text, keep_spaces=False):
    result = ''
    text = text.upper()
    for i in text:
        if ord(i) in range(65, 91):
            result += i
        elif keep_spaces:
            if ord(i) == 32:
                result += i

    return result


def format_text_to_columns(text, columns):
    result = []
    counter = 0
    tmp_result = ''
    for t in text:
        counter += 1
        tmp_result += t
        if counter == columns:
            result.append(tmp_result)
            tmp_result=''
            counter = 0

    for r in result:
        print(r)


def integer_to_bitstring(a):
    """
    Transform integer to bitstring.
    :param a: input integer
    :return: bitstring output
    """
    result = b''

    if a == 0:
        bits = 0
    else:
        bits = int(math.log2(a)) + 1

    for i in range(bits):
        if a >= 2**(bits-1-i):
            a -= 2**(bits-1-i)
            result += b'1'
        else:
            result += b'0'

    return result

def add_leading_zeroes(a, length):
    """
    Add leading zeroes to input if length of input is less than parametr "length".
    :param a: input bitstring
    :param length: expected minimal length of output
    :return: updated bitstring
    """
    if len(a) >= length:
        return a
    else:
        return b'0'*(length-len(a)) + a

