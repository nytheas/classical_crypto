
class ClassicalPermutation:
    def __init__(self, input_text, key, mode='e'):
        self.input_text = input_text

        if type(key) == str:
            self.key = key
            self.permutation_order = []
            self.permutation_groups = 0
            self._prepare_key()

        elif type(key) == list:
            self.permutation_order = []
            for k in key:
                self.permutation_order.append(int(k))
            # self.permutation_order = key
            self.permutation_groups = len(key)

        self.result = ''

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
            key_values.append(ord(k))

        sorted_key_values = sorted(key_values)

        permutation_order = []
        for k in key_values:
            search = k
            for s in range(len(sorted_key_values)):
                if search == sorted_key_values[s]:
                    permutation_order.append(s)
                    sorted_key_values[s] = ''
                    search = -1

        # print(permutation_order)

        self.permutation_order = permutation_order
        self.permutation_groups = len(permutation_order)

    def encrypt(self):
        tmp = {}
        for i in range(self.permutation_groups):
            tmp[i] = ''

        for t in range(len(self.input_text)):
            i = t % self.permutation_groups
            tmp[self.permutation_order[i]] += self.input_text[t]
        # print("e", tmp)
        result = ''
        for i in range(self.permutation_groups):
            result += tmp[i]
        return result

    def decrypt(self):
        string_len = int(len(self.input_text) / self.permutation_groups)
        extra = len(self.input_text) - (string_len * self.permutation_groups)

        # print(len(self.input_text))
        extra_groups = []
        for i in range(extra):
            extra_groups.append(self.permutation_order[i])

        tmp = {}
        working_text = self.input_text
        for i in range(self.permutation_groups):
            tmp_string_len = string_len
            if i in extra_groups:
                tmp_string_len += 1
            tmp[i] = working_text[:tmp_string_len]
            working_text = working_text[tmp_string_len:]

        # print("d", tmp)
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


# password = 'Lord of The Rings'
#
# x = ClassicalPermutation('The third Ring, Vilya, was made of gold and adorned with a "great blue stone", probably a sapphire. The name is derived from the Quenya vilya, "air".[T 11] It is also called the Ring of Air, the Ring of Firmament, or the Blue Ring.', password, 'e')
#
# print(x.result)
#
# password2 = 'The Ring'
#
# c = ClassicalPermutation(x.result, password2, 'e')
#
# print(c.result)
#
# d = ClassicalPermutation(c.result, password2, 'd')
#
# print(d.result)
#
# y = ClassicalPermutation(d.result, password, 'd')
#
# print(y.result)
