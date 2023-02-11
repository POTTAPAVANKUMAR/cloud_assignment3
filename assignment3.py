import os
import re
import socket
from collections import Counter

#script to read the two files from the location of a docket container
with open("/Users/pavankumarpotta/UC/cloudcomputing/assignment3/IF.txt") as file:
    if_content = file.read()

with open("/Users/pavankumarpotta/UC/cloudcomputing/assignment3/Limerick-1.txt") as file:
    limerick_content = file.read()

print("Contents of IF.txt:")
print(if_content)
print("\nContents of Limerick-1.txt:")
print(limerick_content)

# Get the list of all text files in the "/Users/pavankumarpotta/UC/cloudcomputing/assignment3" directory
text_files = [f for f in os.listdir("/Users/pavankumarpotta/UC/cloudcomputing/assignment3") if f.endswith(".txt")]
print("Text files in /Users/pavankumarpotta/UC/cloudcomputing/assignment3:", text_files)

# Read the contents of the two text files and count the number of words
word_counts = {}
for filename in text_files:
    with open(os.path.join("/Users/pavankumarpotta/UC/cloudcomputing/assignment3", filename)) as file:
        contents = file.read()
        words = re.findall(r'\b\w+\b', contents)
        word_counts[filename] = len(words)
print("Number of words in each text file:", word_counts)

# Calculate the grand total of words
grand_total = sum(word_counts.values())
print("Grand total of words:", grand_total)

# Find the top 3 words with maximum count in the "IF.txt" file
if_words = re.findall(r'\b\w+\b', word_counts.get("IF.txt", ""))
if_word_counts = Counter(if_words)
top_3_words = if_word_counts.most_common(3)
print("Top 3 words in IF.txt:", top_3_words)

# Find the IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())
print("IP address of the machine:", ip_address)

# Write the output to a text file
output_filename = "/Users/pavankumarpotta/UC/cloudcomputing/assignment3/output/result.txt"
with open(output_filename, "w") as file:
    file.write("Text files in /Users/pavankumarpotta/UC/cloudcomputing/assignment3: " + str(text_files) + "\n")
    file.write("Number of words in each text file: " + str(word_counts) + "\n")
    file.write("Grand total of words: " + str(grand_total) + "\n")
    file.write("Top 3 words in IF.txt: " + str(top_3_words) + "\n")
    file.write("IP address of the machine: " + str(ip_address) + "\n")

# Read the contents of the result file and print it
with open(output_filename) as file:
    result = file.read()
print(result)
