import re

Score = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20,
         'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200,
         'ש': 300, 'ת': 400, 'ך': 100, 'ם': 40, 'ן': 50,  'ף': 80, 'ץ': 90}

interesting_nums = [61, 26, 55]  ## add your own numbers to the list, script will highlight these in the output

def decompose(num):
    sum = num
    while len(str(sum)) > 1:
        new_sum = 0
        for char in str(sum):
            new_sum += int(char)
        sum = new_sum
    return sum

importfile = open(r'/Users/Path/To/feed.txt')  # change this so will work on your machine

text = str(importfile.read())
importfile.close()

s = re.sub(r'[^a-zA-Z0-9\.\[\]],', ' ', text)
result = ''.join(i for i in s if not i.isdigit()) ###remove all numbers from string so word count isn't off
result = result.strip()
result = re.sub(' +', ' ', result)
result = result.replace('\n', '')
sentences = [sentence.strip('\n') for sentence in re.split('[\.!\?]\s*', result) if sentence.strip('\n') != '']  # changed the regex in this line
print("You have %d sentences" % len(sentences))
clean_sentences = []
print()

for sentence in sentences:
    clean_sentence = ""
    for char in sentence:
        if char.isalpha() or char.isspace():
            clean_sentence += char
    clean_sentences.append(clean_sentence)

for sentence in clean_sentences:
    words = sentence.split(' ')
    print(sentence)
    char_count = [len(word) for word in words]
    print("There are {0} words and a total of {1} letters".format(len(words), sum(char_count)))
    print("Char count: " + str(char_count))

    word_scores = []
    for word in words:
        word_score = [Score.get(char.lower()) for char in word]
        word_scores.append(sum(word_score))

    print("Sentence total: " + str(sum(word_scores)))
    decomposed_word_scores = [decompose(score) for score in word_scores]
    print("Reduced word scores: " + str(decomposed_word_scores))
    print("Sum of Reduced word scores: " + str(sum(decomposed_word_scores)))
    print("Word scores: " + str(word_scores))
    ###attempting to iterate over interesting_nums:
    x = 0
    for num in interesting_nums:
        y = interesting_nums[x]
        if x == len(interesting_nums):
            break
        x += 1
    ###Checking for input in words:
        singles = (sentence.split())
        if y in word_scores:
            ind = (word_scores.index(y))
            print(singles[ind]+' '+str(y))

    ###Check for pairs with unique totals:
    b = len(word_scores)
    if b >= 2:
        x = 0
        e = 0
        d = 2
        pairs = []
        for word in word_scores:
            a = (sum(word_scores[e:d]))
            pairs.append(a)
            if d == b:
                x = 0
                break
            else:
                e += 1
                d += 1
        print('Pairs: '+str(pairs))
        for num in interesting_nums:
            y = interesting_nums[x]
            if x == len(interesting_nums):
                break
            x += 1
            if y in pairs:
                ind = (pairs.index(y))
                splist = (sentence.split())
                g = ind+2
                print(str(splist[ind:g])+' '+str(y))

    ###Check for triples with unique totals:
    b = len(word_scores)
    if b >= 3:
        x = 0
        e = 0
        d = 3
        triples = []
        for word in word_scores:
            a = (sum(word_scores[e:d]))
            triples.append(a)
            if d == b:
                break
            e += 1
            d += 1
        print('Triples: '+ str(triples))
        for num in interesting_nums:
            y = interesting_nums[x]
            if x == len(interesting_nums):
                break
            x += 1
            if y in triples:
                ind = (triples.index(y))
                splist = (sentence.split())
                g = ind+3
                print(str(splist[ind:g])+' '+str(y))
    else:
        pass

    #####Checking for quadruples with unique totals:
    b = len(word_scores)
    if b >= 4:
        x = 0
        e = 0
        d = 4
        quadruples = []
        for word in word_scores:
            a = (sum(word_scores[e:d]))
            quadruples.append(a)
            if d == b:
                break
            e += 1
            d += 1
        print('Quadruples: '+ str(quadruples))
        for num in interesting_nums:
            y = interesting_nums[x]
            if x == len(interesting_nums):
                break
            x += 1
            if y in quadruples:
                ind = (quadruples.index(y))
                splist = (sentence.split())
                g = ind+4
                print(str(splist[ind:g])+' '+str(y))
    else:
        pass

    ###Checking for quintuples with unique totals:
    b = len(word_scores)
    if b >= 5:
        x = 0
        e = 0
        d = 5
        quintuples = []
        b = len(word_scores)
        for word in word_scores:
            a = (sum(word_scores[e:d]))
            quintuples.append(a)
            if d == b:
                break
            e += 1
            d += 1
        print('Quintuples: '+str(quintuples))
        for num in interesting_nums:
            y = interesting_nums[x]
            if x == len(interesting_nums):
                break
            x += 1
            if y in quintuples:
                ind = (quintuples.index(y))
                splist = (sentence.split())
                g = ind+5
                print(str(splist[ind:g])+' '+str(y))
    else:
        pass

    ###Checking for sextuples with unique totals:
    b = len(word_scores)
    if b >= 6:
        x = 0
        e = 0
        d = 6
        sextuples = []
        b = len(word_scores)
        for word in word_scores:
            a = (sum(word_scores[e:d]))
            sextuples.append(a)
            if d == b:
                break
            e += 1
            d += 1
        print('Sextuples: '+ str(sextuples))
        for num in interesting_nums:
            y = interesting_nums[x]
            if x == len(interesting_nums):
                break
            x += 1
            if y in sextuples:
                ind = (sextuples.index(y))
                splist = (sentence.split())
                g = ind+6
                print(str(splist[ind:g])+' '+str(y))
    else:
        pass
    ###Checking for septuples with unique totals:
    b = len(word_scores)
    if b >= 7:
        x = 0
        e = 0
        d = 7
        septuples = []
        b = len(word_scores)
        for word in word_scores:
            a = (sum(word_scores[e:d]))
            septuples.append(a)
            if d == b:
                break
            e += 1
            d += 1
        print('Septuples: '+str(septuples))
        for num in interesting_nums:
            y = interesting_nums[x]
            if x == len(interesting_nums):
                break
            x += 1
            if y in septuples:
                ind = (septuples.index(y))
                splist = (sentence.split())
                g = ind+7
                print(str(splist[ind:g])+' '+str(y))
    else:
        pass

    print('\n'*3)
