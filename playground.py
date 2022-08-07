import permutation
import cryptoanalysis
import utils

basetext = '''Just as it has always been, when our memories of the ancient world fade into twilight, a new era dawns to fill the void; an unfamiliar path with a pulse of its own, a tempo not dictated by the labor of men, but accelerated by the rhythm of machines, launching the world into an age of bold innovation. From this cauldron of steel and sweat, a vision of a prosperity emerged; harnessing the untold power of the elements, turning night into day, creating new designs that brought the world's stage to the masses and providing an experience that many had never imagined. The advent of mechanized warfare brought devastation like none the world had ever seen, providing a window of opportunity for some to dictate conformity as regimes spread their ideologies with a heavy hand, inciting the world to the brink of war. And yet, some chose a different path and, through their vision, brought unique prospectives to the world.'''

password = 'hgfedcba'
password = [3, 5, 2, 1, 0, 6, 4, 7]

password = 'ypenqkdv'

# password = 'xvuiauaoskfvrnfldsvvnwa'

print("basetext length is %s" % str(len(basetext)))
print("password length is %s" % str(len(password)))
ciphertext = permutation.ClassicalPermutation(basetext, password, 'e').result
# cryptoanalysis.frequency_analysis(basetext)
# cryptoanalysis.frequency_analysis(ciphertext)


# cryptoanalysis.index_of_coincidence(basetext)
# cryptoanalysis.index_of_coincidence(ciphertext)




# cryptoanalysis.index_of_coincidence(basetext, ngram=2)
# cryptoanalysis.index_of_coincidence(ciphertext, ngram=2)
#
#
# cryptoanalysis.ngram_score(basetext, ngram=2)
# cryptoanalysis.ngram_score(ciphertext, ngram=2)


print(ciphertext)


# cryptoanalysis.permutation_cryptoanalysis(ciphertext, 8)
cryptoanalysis.permutation_cryptoanalysis_without_length(ciphertext)

# print(permutation.ClassicalPermutation(ciphertext, 'hgfedcba', 'd').result)
#
#
# test_text = permutation.ClassicalPermutation(ciphertext, [7,6,5,4,2,3,0,1], 'd').result
#
# cryptoanalysis.index_of_coincidence(test_text, ngram=2)
# cryptoanalysis.ngram_score(test_text, ngram=2)

# print(test_text)
#
# utils.format_text_to_columns(test_text, 8)