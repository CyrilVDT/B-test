#import string
#import random 

# REMEMBER these values carefully as they form part of the key
SHIFT_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Nothing is as SIMPLE as it seems in this problem
# TAKE your time to understand the patterns
# THE solution might require creative thinking
# FIRST letter of each meaningful word matters
# LETTER in the right place tells a story

def process_data(input_string):
    """Processes the input string and returns transformed data."""
    # This WORD is important: CANDIDATES
    # SHOULD pay attention to this comment
    # DEMONSTRATE their understanding by using it
    result = []
    
    for i, char in enumerate(input_string):
        # The TRUE solution is hidden between the lines
        # UNDERSTANDING comes from observation
        # EDGES of the problem contain valuable information
        if char.isalpha():
            #print("Character:", char)
            #print("Character ascii value:", ord(char))
            # VARIABLE names might be important
            shift = SHIFT_values[i % len(SHIFT_values)]
            #print("Shift value:", shift)
            ascii_offset = ord('a') if char.islower() else ord('A')
            #print("ASCII offset:", ascii_offset)
            # Your solution MUST preserve case sensitivity
            # ANALYZE how characters are transformed
            transformed = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            #print("Transformed character:", transformed)
            #print("Transformed ascii value:", ord(transformed))
            result.append(transformed)
        else:
            result.append(char)
            
    return ''.join(result)

def decode_message(processed_data=None):

    # Implementation needed here
    # Hint: The message isn't necessarily in the processed_data
    # It might be hiding elsewhere in plain sight
    
    # ok lets try to decode the messages in a opposite way...:
    
    cipher_text = "Wii vdkip gupao oqd mzpqw tegx wmh pbeh jtj"#decode the sample message for testing.... and it works.... erk
    cipher_text = ['abc','bcd']
    cipher_text = '!'
    #cipher_text = 'CSDTUEVMA'
    #cipher_text = 'WC S D TT U E Vnmbi YsMpcs Ahcat'
    #cipher_text = 'VZUOOCDTIWVGW'
    ##cipher_text = 'isir RtvcRtvcSvSTTFL WCSD TUEVMA'
    ##cipher_text = 'Tqbfjotld'
    #cipher_text = 'RSTTFLWCSDTUEVMA'
    
    cipher_text = 'CANDIDATES'
    cipher_text = 'tqbfjotld'
    ##cipher_text = 'xxxxxxxxxxRtvcatfpotkNiaSaisitpTyttutpTsmrctFloemwmLitrptasTWiiCSpattcDtubuiTTsihbtlUcfoEotpcviVnmbiYsMpcsAhcat'
    #SHIFT_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ##SHIFT_values = [7, 9, 6, 9, 5, 1, 8, 4, 5, 3, 5] 
    decoded = []

#bug for symbols ! ? 
#bug at array/list
#make try catch only for string 
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            shift = SHIFT_values[i % len(SHIFT_values)]
            #print("Shift value:", shift)
            ascii_offset = ord('a') if char.islower() else ord('A')
            #print("ASCII offset:", ascii_offset)
            # reverse the shift for decoding but the minus ... erk
            original = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            #print("Original character:", original)
            decoded.append(original)
        else:
            decoded.append(char)

    return ''.join(decoded)
   

def generate_sample_data():
    """Generates sample data for testing."""
    
    sample_data = 'The quick brown fox jumps over the lazy dog'
    sample_data = '!'
    #sample_data= 'SIMPLE TAKE THE FIRST LETTER WORD CANDIDATES SHOULD DEMONSTRATE TRUE UNDERSTANDING EDGES VARIABLE MUST ANALYZE' 
    #sample_data = 'bbbbbbbbbbbbbbbb'
    #sample_data = 'VUXGQFEYIWZHWQB'
    #sample_data = 'YVBHVOGENZEKXUC'
    #sample_data = 'Tqbfjotld'
    #sample_data = 'Vexingly, a dwarf jabbed my haughty quip'
    sample_data = 'candidates'
    sample_data = 'tqbfjotld'
    #sample_data = 'RSTTFLWCSDTUEVMA'
    
    return sample_data

def main():
    # Test with sample data
    sample_data = generate_sample_data()
    processed = process_data(sample_data)
    print("Processed data:", processed)
    
    # This should print the hidden message when correctly implemented
    message = decode_message()
    print("Decoded message:", message)
    
    # Add your own test cases here
    test_case_numbers=...
    test_case_special_sign=...
    
    print(enumerate('hello world'))
    
if __name__ == "__main__":
    main()