'''9.4 Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
 The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
 they appear in the file. After the dictionary is produced,
 the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

file_name = input("Enter file:")
if len(file_name) < 1:
    name = "mbox-short.txt"
file_handle = open(file_name)
emails_dict = dict()
for line in file_handle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        emails_dict[email] = emails_dict.get(email, 0) + 1
max_email_count = 0
email_with_max_count = ''
for email, count in emails_dict.items():
    if count > max_email_count or max_email_count == 0:
        max_email_count = count
        email_with_max_count = email

print(email_with_max_count, max_email_count)
