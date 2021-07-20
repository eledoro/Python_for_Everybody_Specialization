'''10.2 Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

file_name = input("Enter file:")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
file_handle = open(file_name)
emails_by_hour_dict = dict()
for line in file_handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        emails_by_hour_dict[hour] = emails_by_hour_dict.get(hour, 0) + 1

emais_by_hour_list = list()
for hour, count in emails_by_hour_dict.items():
    emais_by_hour_list.append((hour, count))

emais_by_hour_list = sorted(emais_by_hour_list)
for hour,emails_count in emais_by_hour_list:
    print(hour, emails_count)
