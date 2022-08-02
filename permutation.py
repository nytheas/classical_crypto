
class ClassicalPermutation:
    def __init__(self, input_text, key, mode='e'):
        self.input_text = input_text
        self.key = key
        self.result = ''

        self.permutation_order = []
        self.permutation_groups = 0
        self._prepare_key()

        self.mode = mode
        if self.mode == 'e':
            self.plaintext = input_text
            self.result = self.encrypt()
            self.ciphertext = self.result

        elif self.mode == 'd':
            self.ciphertext = input_text
            self.result = self.decrypt()
            self.plaintext = self.result


    def _prepare_key(self):
        key_values = []
        for k in self.key:
            new_char = ord(k)
            if new_char not in key_values:
                key_values.append(new_char)

        sorted_key_values = sorted(key_values)

        permutation_order = []
        for k in key_values:
            for s in range(len(sorted_key_values)):
                if k == sorted_key_values[s]:
                    permutation_order.append(s)

        self.permutation_order = permutation_order
        self.permutation_groups = len(permutation_order)

    def encrypt(self):
        tmp = {}
        for i in range(self.permutation_groups):
            tmp[i] = ''

        for t in range(len(self.input_text)):
            i = t % self.permutation_groups
            tmp[self.permutation_order[i]] += self.input_text[t]

        result = ''
        for i in range(self.permutation_groups):
            result += tmp[i]
        return result

    def decrypt(self):
        string_len = int(len(self.input_text) / self.permutation_groups)

        tmp = {}
        working_text = self.input_text
        for i in range(self.permutation_groups):
            tmp[i] = working_text[:string_len]
            working_text = working_text[string_len:]

        result = ''
        done = False
        while not done:
            for i in range(self.permutation_groups):
                if len(tmp[self.permutation_order[i]]) > 0:
                    result += tmp[self.permutation_order[i]][:1]
                    tmp[self.permutation_order[i]] = tmp[self.permutation_order[i]][1:]
                else:
                    done = True

        return result


password = 'efghabcd'

x = ClassicalPermutation('abcdefghijklmnopqrstuvwx', password, 'e')

print(x.result)

y = ClassicalPermutation(x.result, password, 'd')

print(y.result)
