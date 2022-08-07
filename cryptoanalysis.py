import utils
import permutation

def frequency_analysis(text, char_len=1, ngram=1, excluded_chars=[], verbose=False):
    result = {}
    char_count = 0
    for c in excluded_chars:
        text = text.replace(c, "")

    while len(text) > 0:
        character = text[:char_len*ngram]
        text = text[char_len:]
        char_count += 1
        if len(character) == char_len*ngram:
            if character not in result:
                result[character] = 0
            result[character] += 1

    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    # print("Total of %s unique characters" % len(result))
    if verbose:
        for c in result:
            print(c, result[c], round(result[c]/char_count*100, 2))
    else:
        # print(result)
        return result



def index_of_coincidence(text, ngram=1):
    distribution = frequency_analysis(utils.transform_to_basic_alphabet(text), ngram=ngram)

    subtotal = 0
    char_count = 0
    for d in distribution:
        subtotal += distribution[d] * (distribution[d]+1)
        char_count += distribution[d]
    total = subtotal / (char_count * (char_count+1))

    print(total)
    return total


def ngram_score(text, ngram=2):
    ngrams = {}
    file = open("bigrams.txt", 'r')
    for i in file:
        x = i.split(";")
        ngrams[x[0]] = int(x[1])

    distribution = frequency_analysis(utils.transform_to_basic_alphabet(text), ngram=ngram)

    subscore = 0
    for d in distribution:
        subscore += ngrams[d] * distribution[d]

    return subscore


def permutation_cryptoanalysis(text, password_length):
    columns = {}
    column_length = int(len(text) / password_length)
    for i in range(password_length):
        columns[i] = text[column_length * i: column_length * (i+1)]

    results = {}
    for i in range(password_length):
        for j in range(password_length):
            if i != j:
                score = evaluate_columns(columns[i], columns[j])
                results[str(i) + "," + str(j)] = score

    results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    # print(results)
    expected_password = order_columns(results, password_length)
    print("x", expected_password)

    exp_pass = []
    for i in expected_password:
        exp_pass.append(int(i))


    resulted_text = permutation.ClassicalPermutation(text, exp_pass, 'd').result
    score = ngram_score(resulted_text, ngram=2)
    return exp_pass, score
    print(resulted_text)


def evaluate_columns(a, b):
    bigrams = []
    for i in range(len(a)):
        bigrams.append(a[i] + b[i])

    result = ''

    for b in bigrams:
        bigram = utils.transform_to_basic_alphabet(b)
        if len(b) == 2:
            result += b

    score = ngram_score(result, ngram=2)
    return score


def order_columns(scored_columns, columns_count):
    ordered = {}
    checked_columns = []

    for s in scored_columns:
        c = s.split(',')

        if c[0] not in checked_columns and c[1] not in checked_columns:
            ordered[len(ordered)+1] = [c[0], c[1]]
            checked_columns.append(c[0])
            checked_columns.append(c[1])
        elif c[0] not in checked_columns:
            for o in ordered:
                if ordered[o][0] == c[1]:
                    ordered[o].insert(0, c[0])
                    checked_columns.append(c[0])

        elif c[1] not in checked_columns:
            for o in ordered:
                if ordered[o][-1] == c[0]:
                    ordered[o].append(c[1])
                    checked_columns.append(c[1])
        else:
            index1 = 0
            index2 = 0
            for o in ordered:
                if len(ordered[o]) > 0:
                    if ordered[o][0] == c[1]:
                        index1 = o
                    if ordered[o][-1] == c[0]:
                        index2 = o

            if index1 == 0 or index2 == 0:
                continue
            elif index1 != index2:
                ordered[index2] += ordered[index1]
                ordered[index1] = [-1]

        for o in ordered:
            if len(ordered[o]) == columns_count:
                print(ordered[o])
                return ordered[o]


def permutation_cryptoanalysis_without_length(text):
    computed_results = {}
    for i in range(2, 12):
        if len(text) % i == 0:
            print("TRYING length %s" % str(i))
            result = permutation_cryptoanalysis(text, i)
            print(result)
            computed_results[str(result[0])] = result[1]
        else:
            print("length %s not aplicable" % str(i))

    computed_results = dict(sorted(computed_results.items(), key=lambda x: x[1], reverse=True))
    exp_pass = []
    for i in computed_results:
        tmp = i.replace("[", "").replace("]", "").split(",")
        for t in tmp:
            exp_pass.append(int(t))
        print(permutation.ClassicalPermutation(text, exp_pass, 'd').result)
        break


def compute_expected_index_of_coincidence(text):
    text = utils.transform_to_basic_alphabet(text)
    ngrams = {}
    text_length = len(text)
    file = open("bigrams.txt", 'r')
    total = 0
    for i in file:
        x = i.split(";")
        ngrams[x[0]] = int(x[1])
        total += int(x[1])

    rand_ngram = text_length / (26**2)

    rand_score = 0
    for i in range(26**2):
        rand_score += rand_ngram * (rand_ngram+1)

    rand_score = rand_score / (text_length * (text_length + 1))

    total_in_ngrams = 0
    for n in ngrams:
        total_in_ngrams += ngrams[n]

    # total_in_ngrams = text_length  ## is this for better or for worse?


    expected_score = 0
    for n in ngrams:
        recomputed_n = ngrams[n] * text_length / total_in_ngrams
        if recomputed_n < 1:
            recomputed_n = 0
        expected_score += recomputed_n * (recomputed_n + 1)

    expected_score = expected_score / (text_length * (text_length + 1))

    real_score = index_of_coincidence(text, ngram=2)

    evaluation = (real_score - rand_score) / (expected_score - rand_score)

    print(rand_score, expected_score, real_score, evaluation)
    print(ngrams)


def find_bigram_continuation(column_a, column_b, columns):
    bigrams = []
    for i in range(len(column_a)):
        bigrams.append(column_a[i] + column_b[i])

    trigrams_score = {}
    ident = 0
    for c in columns:
        trigrams = ''
        for i in range(len(bigrams)):
            t = bigrams[i] + c[i]
            t = utils.transform_to_basic_alphabet(t)
            if len(t) == 3:
                trigrams += t

        trig_score = ngram_score(t, ngram=3)
        trigrams_score[ident] = trig_score
        ident += 1

    print(trigrams_score)


def find_words(text):
    used_words = {}

    words = text.split(' ')

    for w in words:
        formated_word = utils.transform_to_basic_alphabet(w)
        if formated_word not in used_words:
            used_words[formated_word] = 0
        used_words[formated_word] += 1


    used_words = dict(sorted(used_words.items(), key=lambda x: x[1], reverse=True))
    return used_words


def evaluate_words(words):
    found = []
    found_score = 0
    not_found = []
    not_found_score = 0

    wordlist = []
    file = open("words_100000.txt", "r")
    for row in file:
        wordlist.append(row.replace("\n", ""))

    for w in words:
        if w in wordlist:
            found.append(w)
            found_score += words[w]
        else:
            not_found.append(w)
            not_found_score += words[w]

    print(found)
    print(not_found)
    print(found_score, not_found_score)


text = '''
Just as it has always been, when our memories of the ancient world fade into twilight, a new era dawns to fill the void; an unfamiliar path with a pulse of its own, a tempo not dictated by the labor of men, but accelerated by the rhythm of machines, launching the world into an age of bold innovation. From this cauldron of steel and sweat, a vision of prosperity emerged; harnessing the untold power of the elements, turning night into day, creating new designs that brought the world's stage to the masses and providing an experience that many had never imagined. The advent of mechanized warfare brought devastation like none the world had ever seen, providing a window of opportunity for some to dictate conformity as regimes spread their ideologies with a heavy hand, inciting the world to the brink of war. And yet, some chose a different path and, through their vision, brought unique prospectives to the world.
'''

evaluate_words(find_words(text))

#
#
#
# # frequency_analysis(text, ngram=2, excluded_chars=[' ', "\n"])
#
# compute_expected_index_of_coincidence(text)
# index_of_coincidence(text, ngram=2)



# x = frequency_analysis(utils.transform_to_basic_alphabet(text), ngram=2)
#
# for i in x:
#     print(i, x[i])