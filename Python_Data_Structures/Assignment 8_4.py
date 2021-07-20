'''8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt'''

file_name = input("Enter file name: ")
file_handle = open(file_name)
list_words_in_text = list()
for line in file_handle:
    line = line.split()
    for word in line:
        if word not in list_words_in_text:
            list_words_in_text.append(word)
list_words_in_text.sort()
print(list_words_in_text)
