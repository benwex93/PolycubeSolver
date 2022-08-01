import string

quick_str = "The quick brown fox jumps over the lazy dog"
quick_braille = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
quick_braille_ls = [quick_braille[i:i+6] for i in range(0, len(quick_braille) - 1, 6)]

braille_trans = {}
braille_trans[' '] = '000000'

for i, letter in enumerate(quick_str):
	# +1 to skip capitalization mark
	braille_trans[letter] = quick_braille_ls[i + 1]

CAP_MARK = quick_braille_ls[0]
for letter in string.ascii_uppercase:
	braille_trans[letter] = CAP_MARK + braille_trans[letter.lower()]

def solution(text):
	translation = ''
	for letter in text:
		translation += braille_trans[letter]
	print (translation)

