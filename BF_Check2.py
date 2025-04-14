import enchant
import itertools

# Initialize the English dictionary
d = enchant.Dict("en_US")

# Your original ciphered text
#cipher_text = "isir RtvcRtvcSvSTTFL WCSD TUEVMA"#decoded, too many variants
#cipher_text = 'RSTTFLWCSDTUEVMA' #decoded, nothing
cipher_text = "TWiiC Spattc Dtubui"


SHIFT_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Caesar cipher shift function
def caesar_shift(text, shifts):
    result = ""
    shifts_len = len(shifts)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = shifts[i % shifts_len]
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            
        else:
            result += char
    return result

# Generate shift patterns from [0,0,...,0] to [9,9,...,9]
for shifts in itertools.product(range(10), repeat=5):#len(SHIFT_values)):
    #print(shifts)
    shifted_text = caesar_shift(cipher_text, shifts)
    #print(shifted_text)
     #words = 'aaawhelloworld'
    # Check if shifted text contains at least two valid English words
    words = shifted_text.split()
    valid_words_count = sum(1 for word in words if d.check(word))
    if valid_words_count >= 2:
        print(f"Shifts: {shifts}, Shifted text: {shifted_text}and words found: {words}")