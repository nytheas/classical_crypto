
def transform_to_basic_alphabet(text):
    result = ''
    text = text.upper()
    for i in text:
        if ord(i) in range(65, 91):
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