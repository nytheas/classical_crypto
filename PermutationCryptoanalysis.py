import cryptoanalysis
import utils
import permutation

class PermutationCryptoanalysis:
    def __init__(self, ciphertext, analyze_all=False, key_lenghts=[]):
        self.ciphertext = ciphertext

        self.max_key_length = 11
        self.threshold = 0.6
        self.analyze_all = analyze_all

        self.threshold_score = self.compute_threshold_score()
        if len(key_lenghts) == 0:
            self.key_lengths = self.find_key_lengths()
        else:
            self.key_lengths = key_lenghts

        print("TS:", self.threshold_score)

    def find_key_lengths(self):
        kl_mod = []
        kl_not_mod = {}
        text_len = len(self.ciphertext)
        for k in range(3, self.max_key_length+1):
            tmp_klen = text_len % k
            if tmp_klen % k == 0:
                kl_mod.append(k)
            else:
                if tmp_klen not in kl_not_mod:
                    kl_not_mod[tmp_klen] = []
                kl_not_mod[tmp_klen].append(k)

        key_lengths = []
        for k in kl_mod:
            key_lengths.append((k, b'0' * k))

        for k in sorted(kl_not_mod):
            for l in kl_not_mod[k]:
                all_splits = self.get_possible_splits(l, k)
                for m in all_splits:
                    key_lengths.append((l, m))

        # TODO: properly sort, 1, n-1, 2, n-2 ...
        print('TEST', key_lengths)
        return key_lengths

    def get_possible_splits(self, keylength, reminder):
        splits = []

        for i in range(2**keylength):
            bitstring = utils.integer_to_bitstring(i)

            number_of_ones = 0
            for x in bytes.decode(bitstring, 'utf-8'):
                if x == '1':
                    number_of_ones += 1

            if number_of_ones == reminder:
                splits.append(utils.add_leading_zeroes(bitstring, keylength))

        return splits

    def analyze(self):
        results = {}
        best_guess_plaintext = ''
        best_guess_score = 0
        for k in self.key_lengths:
            print("testing:", k)
            round_result = PermutationRound(self.ciphertext, k)
            results[str(k)] = round_result.probable_plaintext_score

            if round_result.probable_plaintext_score > best_guess_score:
                best_guess_plaintext = round_result.probable_plaintext
                best_guess_score = round_result.probable_plaintext_score

            if not self.analyze_all and round_result.probable_plaintext_score > self.threshold_score:
                print(str(k))
                print(round_result.probable_plaintext)
                break

        if self.analyze_all:
            print(dict(sorted(results.items(), key=lambda x: x[1], reverse=True)))
            print("Best guess:")
            print(best_guess_plaintext)

    def compute_threshold_score(self):
        tmp_ciphertext = utils.transform_to_basic_alphabet(self.ciphertext)

        return self.threshold * len(tmp_ciphertext)




class PermutationRound:
    def __init__(self, ciphertext, expected_key_length):
        self.ciphertext = ciphertext
        self.keylength = expected_key_length[0]
        self.modulator = expected_key_length[1]

        self.columns = self.split_ciphertext()

        self.columns_relations = self.evaluate_columns_relations()

        self.probable_password = self.order_columns()

        self.probable_plaintext = permutation.ClassicalPermutation(self.ciphertext, self.probable_password, 'd').result
        self.probable_plaintext_score = self.score_possible_plaintext()


        print("PPS:", self.probable_plaintext_score)

    def split_ciphertext(self):
        columns = {}

        splits = self.get_ciphertext_splits()
        column_num = 0
        last = 0
        for s in range(len(splits)):
            columns[column_num] = self.ciphertext[last:splits[s]]
            column_num += 1
            last = splits[s]

        # print("c", columns)
        return columns

    def get_ciphertext_splits(self):

        splits = []

        split_length = int(len(self.ciphertext) / self.keylength)

        split_shift = 0
        tmp = 0
        for m in bytes.decode(self.modulator, 'utf-8'):
            tmp += split_length
            if m == '1':
                tmp += 1
            splits.append(tmp)

        # print('TEST', splits)
        return splits


    def evaluate_columns_relations(self):
        # TODO: split to primary and secondary columns

        results = {}
        for i in range(self.keylength):
            for j in range(self.keylength):
                if i != j:
                    score = cryptoanalysis.evaluate_columns(self.columns[i], self.columns[j])
                    results[str(i) + "," + str(j)] = score

        results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

        # print("TEST", results)
        return results

    def order_columns(self):
        return cryptoanalysis.order_columns(self.columns_relations, self.keylength)

    def score_possible_plaintext(self):
        words = utils.transform_to_basic_alphabet(self.probable_plaintext, keep_spaces=True)
        words = cryptoanalysis.find_words(words)
        score = cryptoanalysis.evaluate_words(words)

        return score


# text = '''Just as it has always been, when our memories of the ancient world fade into twilight, a new era dawns to fill the void; an unfamiliar path with a pulse of its own, a tempo not dictated by the labor of men, but accelerated by the rhythm of machines, launching the world into an age of bold innovation. From this cauldron of steel and sweat, a vision of prosperity emerged; harnessing the untold power of the elements, turning night into day, creating new designs that brought the world's stage to the masses and providing an experience that many had never imagined. The advent of mechanized warfare brought devastation like none the world had ever seen, providing a window of opportunity for some to dictate conformity as regimes spread their ideologies with a heavy hand, inciting the world to the brink of war. And yet, some chose a different path and, through their vision, brought unique prospectives to the world.'''
#
# print(len(text))
#
# x = PermutationCryptoanalysis(text)
# y = PermutationRound(text, (4, b'0000'))
# y.split_ciphertext()
#
# print(y.columns)


