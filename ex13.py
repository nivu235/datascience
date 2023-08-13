import string

def calculate_word_frequency(text):
   
    
    
    words = text.split()
    
   
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

def main():
  
    file_path = 'nive.txt'
    with open(file_path, 'r') as file:
        text = file.read()
    
    word_frequency = calculate_word_frequency(text)
    
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

main()
