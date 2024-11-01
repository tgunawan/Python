def search_words(sentence, word_array):
    sentence_words = sentence.split()  # Split the sentence into individual words
    for word in sentence_words:
        if word in word_array:
            return True
    return False

# Example usage

words = ["apple", "banana", "orange", "grape", "pear"]
for word in words:
  print(word)
  
sentence = input("Enter a sentence: ")
if search_words(sentence, words):
    print("The sentence contains a word from the array.")
else:
    print("The sentence does not contain any word from the array.")
