import fitz
import pandas as pd

doc = fitz.open("example_w9.pdf")

page1 = doc[0]

words = page1.get_text("words")

print(words)

first_annots = []

rec = page1.first_annot.rect

# Information of words in first object is stored in mywords

mywords = [w for w in words if fitz.Rect(w[:4]) in rec]

ann = make_text(mywords)

first_annots.append(ann)


def make_text(words):

    line_dict = {}

    words.sort(key=lambda w: w[0])

    for w in words:

        y1 = round(w[3], 1)

        word = w[4]

        line = line_dict.get(y1, [])

        line.append(word)

        line_dict[y1] = line

    lines = list(line_dict.items())

    lines.sort()

    return "n".join([" ".join(line[1]) for line in lines])


for pageno in range(0, len(doc) - 1):

    page = doc[pageno]

    words = page.get_text("words")

    for annot in page.annots():

        if annot != None:

            rec = annot.rect

            mywords = [w for w in words if fitz.Rect(w[:4]) in rec]

            ann = make_text(mywords)

            all_annots.append(ann)

cont = []

for i in range(0, len(all_annots)):

    cont.append(all_annots[i].split("n", 1))

liss = []

for i in range(0, len(cont)):

    lis = []

    for j in cont[i]:

        j = j.replace("*", "")

        j = j.replace("#", "")

        j = j.replace(":", "")

        j = j.strip()

        # print(j)

        lis.append(j)

    liss.append(lis)

keys = []

values = []

for i in liss:

    keys.append(i[0])

    values.append(i[1])

for i in range(0, len(values)):

    for j in range(0, len(values[i])):

        if values[i][j] >= "A" and values[i][j] <= "Z":

            break

    if j == len(values[i]) - 1:
        values[i] = values[i].replace(" ", "")

report = dict(zip(keys, values))

dic = [
    report["NAME"],
    report["BUSINESS NAME"],
    report["SOCIAL SECURITY NUMBER"],
    report["EMPLOYER IDENTIFICATION NUMBER"],
]

l = 0

val_after = []

for local in dic:

    li = []

    lii = []

    k = ""

    extract = ""

    l = 0

    for i in range(0, len(local) - 1):

        if local[i + 1] >= "0" and local[i + 1] <= "9":

            li.append(local[l : i + 1])

            l = i + 1

    li.append(local[l:])

    print(li)

    for i in li:

        if i[0] in lii:

            k = i[0]

            break

        lii.append(i[0])

    for i in li:

        if i[0] == k:

            val_after.append(extract)
            break

    report["NAME"] = val_after[0]
    report["BUSINESS NAME"] = val_after[1]
    report["SOCIAL SECURITY NUMBER"] = val_after[2]

data = pd.DataFrame.from_dict(report)

data.to_csv("final.csv", index=False)
