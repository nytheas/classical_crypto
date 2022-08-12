import permutation
import cryptoanalysis
import utils
import PermutationCryptoanalysis

basetext = '''Just as it has always been, when our memories of the ancient world fade into twilight, a new era dawns to fill the void; an unfamiliar path with a pulse of its own, a tempo not dictated by the labor of men, but accelerated by the rhythm of machines, launching the world into an age of bold innovation. From this cauldron of steel and sweat, a vision of a prosperity emerged; harnessing the untold power of the elements, turning night into day, creating new designs that brought the world's stage to the masses and providing an experience that many had never imagined. The advent of mechanized warfare brought devastation like none the world had ever seen, providing a window of opportunity for some to dictate conformity as regimes spread their ideologies with a heavy hand, inciting the world to the brink of war. And yet, some chose a different path and, through their vision, brought unique prospectives to the world.'''

basetext = '''Just as it has always been, when memories of the ancient world fade into twilight, new era dawns to fill the void; an unfamiliar path with a pulse of its own, a tempo not dictated by the labor of men, but accelerated by the rhythm of machines, launching the world into an age of bold innovation. From this cauldron of steel and sweat, a vision of a prosperity emerged; harnessing the untold power of the elements, turning night into day, creating new designs that brought the world's stage to the masses and providing an experience that many had never imagined. The advent of mechanized warfare brought devastation like none the world had ever seen, providing a window of opportunity for some to dictate conformity as regimes spread their ideologies with a heavy hand, inciting the world to the brink of war. And yet, some chose a different path and, through their vision, brought unique prospectives to the world.'''


password = 'hgfedcba'
password = [3, 5, 2, 1, 0, 6, 4, 7]

password = 'aypenqckdkv'
password = 'abcdefghijk'
# password = 'xvuiauaoskfrfdsvvnwa'

print("basetext length is %s" % str(len(basetext)))
print("password length is %s" % str(len(password)))
print("password offset is %s" % str(len(basetext) % len(password)))

x = permutation.ClassicalPermutation(basetext, password, 'e')
ciphertext = x.result

print(x.permutation_groups)
print(ciphertext)
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

 # print(ciphertext)


# cryptoanalysis.permutation_cryptoanalysis(ciphertext, 8)
# cryptoanalysis.permutation_cryptoanalysis_without_length(ciphertext)

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

x = PermutationCryptoanalysis.PermutationCryptoanalysis(ciphertext, analyze_all=True, key_lenghts=[(11, b'10000000000')])
# x = PermutationCryptoanalysis.PermutationCryptoanalysis(ciphertext, analyze_all=True)
x.analyze()

# y = PermutationCryptoanalysis.PermutationRound(ciphertext, (8, b'00000000'))
# y.split_ciphertext()
#
# print(y.probable_plaintext)


e = {0: 'Jhbm teir oahlootlnlto, i nruteosrsn minedthsed nnr  z vie  a ytcasrsan h eorn o so.', 1: 'uaeet  gafim sw ea,ehf tnoooleanpgstoentae et  acy Toebak ep o oosp  vcwewtsedtnup ', 2: 'ssemhwih idiwenndb re lhtfvmdet eeiofngotsb ampne ihfdrsewvrwpf n riwyio a,en,h,net', 3: 't noeontdl;li ,o oba maeo a rl,ordnl t  iirwgar  hme  ot oeoipodfredi trbr  t e ich', 4: ' a,r rt,al ito tbrutrau  btto  fi;gdtsndngooesoetaa mwuanrrvnorioeaethilr.sa tibqte', 5: 'al ialo w aahfa y tehcnwaoihnaa t   h,iagnur svxhdgaeagtol idr crgdohandi o phrrui ', 6: 'swwend nntnr   d o dyhconloi n ayhtpe gy sglteipa idcrhindsdotstmi l ng nAmdar oevw', 7: ' ahsc tesh  aititfa tihr dnsodv  aho th,n hdosdetnnvhftoe eiwuoaimtoad tkneitovu eo', 8: "iye ifww eup tech cbhnila . f ipereweut ett'  ir eeeaa n hen nmttehg ,to d fhuigpsr", 9: 'tsnoeai t napsmtemcymendgi c ssrmn elr cwh stanimvdnnrd tangoieeyseih h o cf gshr l', 10: '   fndleovftu pa ee  sg enFaswioeeurenir at hngeae.tieelhd, ft    ieeietfyheahitotd'}
c = {0: 'Jhbm teir oahlootlnlto, i nruteosrsn minedthsed nnr  z vie  a ytcasrsan h eorn o so.', 1: 'uaeet  gafim sw ea,ehf tnoooleanpgstoentae et  acy Toebak ep o oosp  vcwewtsedtnup ', 2: 'ssemhwih idiwenndb re lhtfvmdet eeiofngotsb ampne ihfdrsewvrwpf n riwyio a,en,h,net', 3: 't noeontdl;li ,o oba maeo a rl,ordnl t  iirwgar  hme  ot oeoipodfredi trbr  t e ich', 4: ' a,r rt,al ito tbrutrau  btto  fi;gdtsndngooesoetaa mwuanrrvnorioeaethilr.sa tibqte', 5: 'al ialo w aahfa y tehcnwaoihnaa t   h,iagnur svxhdgaeagtol idr crgdohandi o phrrui ', 6: 'swwend nntnr   d o dyhconloi n ayhtpe gy sglteipa idcrhindsdotstmi l ng nAmdar oevw', 7: ' ahsc tesh  aititfa tihr dnsodv  aho th,n hdosdetnnvhftoe eiwuoaimtoad tkneitovu eo', 8: "iye ifww eup tech cbhnila . f ipereweut ett'  ir eeeaa n hen nmttehg ,to d fhuigpsr", 9: 'tsnoeai t napsmtemcymendgi c ssrmn elr cwh stanimvdnnrd tangoieeyseih h o cf gshr l', 10: '   fndleovftu pa ee  sg enFaswioeeurenir at hngeae.tieelhd, ft    ieeietfyheahitotd'}

textlen_e = 0
for i in e:
    # print(len(e[i]))
    textlen_e += len(e[i])

# print("-")
textlen_c = 0
for i in c:
    # print(len(c[i]))
    textlen_c += len(c[i])

# print( textlen_e, textlen_c)

