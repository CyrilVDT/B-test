SHIFT_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def process_data(input_string, mode_shift):
    """Processes the input string and returns transformed data. mode shift is either encode or decode."""
    try:   
        result = []

        for i, char in enumerate(input_string):
            if char.isalpha():
                if ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or ord(char) > 122:
                    raise ValueError(f"Invalid character '{char}' in input string.")
                shift = SHIFT_values[i % len(SHIFT_values)]
                ascii_offset = ord('a') if char.islower() else ord('A')
                if mode_shift == 'decode':
                    shift = -shift  # Reverse the shift for decoding
                transformed = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                result.append(transformed)
            else:
                result.append(char)

        return ''.join(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def generate_sample_data():
    """Generates sample data for testing. if enter is pressed, it will use the sample text."""
    sample_data = input("write a string to encode and decode, or press Enter to use a sample text:") #'The quick brown fox jumps over the lazy dog'
    if sample_data == '':
        sample_data = 'The quick brown fox jumps over the lazy dog'
    return sample_data 

def check_valid_encoding(original, encoded, decoded):
    '''Checks if the encoding and decoding are valid by comparing the original and decoded strings. and checks if the words are present in both. '''
    if original == decoded:
        print("Encoding and decoding are valid.")
    else:
        print("Encoding and decoding are not valid.")
        
    encoded_words = encoded.split()
    decoded_words = decoded.split()
 
    for word in encoded_words:
        if word in decoded_words:
            print(f"Word '{word}' is present in both encoded and decoded messages.")

    

def main():

    sample_data = generate_sample_data()
    processed = process_data(sample_data, None)
    print("Processed data:", processed)
    message = process_data(processed, 'decode')
    print("Decoded message:", message)
    
    check_valid_encoding(sample_data, processed, message)
    
if __name__ == "__main__":
    main()



