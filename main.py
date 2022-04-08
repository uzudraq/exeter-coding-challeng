import tracemalloc
import pandas
import time

start = time.time()

tracemalloc.start()

word_li = list()

for i in open("find_words.txt"):
    word_li.append(i.strip().split('\n'))
french_dict = pandas.read_csv("french_dictionary.csv", header=None)

main_dict = dict(zip(french_dict[0].to_list(), french_dict[1].to_list()))

with open("t8.shakespeare.txt", "r") as f:
    txt_file = f.read()
replaced_words = []
frequency_words = []

for i in word_li:
    frequency_words.append(txt_file.count(i[0]))
    replaced_words.append(i[0])
    txt_file = txt_file.replace(i[0], main_dict[i[0]])

c = 0
l = len(frequency_words)
for i in range(l):
    if frequency_words[i] > 0:
        c += 1
print("number of words replaced: ", c)

text_file = open("t8.shakespeare.translated.txt", "w")
text_file.write(" %s " % txt_file)
text_file.close()

Dict = [{'English word': e, 'French word': f, 'Frequency': freq} for e, f, freq in
        zip(french_dict[0].to_list(), french_dict[1].to_list(), frequency_words)]

df = pandas.DataFrame(Dict, columns=['English word', 'French word', 'Frequency'])

df.to_csv("frequency.csv", index=None)

l = len(df)

unique_li = []
for i in range(l):
    if df['Frequency'][i] > 0:
        unique_li.append(df['English word'][i])
print(unique_li)

end = time.time()

total_time = round(end - start)

current, peak = tracemalloc.get_traced_memory()

current = round(current / 1024)

print("total time: ", total_time)

print("memory used: ", current / 1024, "kB")

s1 = "Time to process: " + str(total_time) + " seconds\n"

s2 = "Memory used: " + str(current) + " kB"

with open("performance.txt", "w") as f:
    f.write(s1)
    f.write(s2)
