import re


schema = [ ['WORD',      '14', 'VARCHAR'],
           ['FREQ',       '6', 'NUM'],
           ['HISTOGRAM', '46', 'VARCHAR'] ]

collect = {}


def parse(filename, ex):

    global collect

    global schema


    words = []

    try:

        with open(filename, 'r') as file:

            for line in file: words += re.findall(ex, line);

    except FileNotFoundError:

        return -1


    for i in range(len(words)): words[i] = words[i].upper()


    for i in range(len(words)):

        if not words[i] in collect:

            word = words[i]

            if len(word) > int(schema[0][1]):
                word = word[:int(schema[0][1]) - 3] + '...'

            rec = { schema[0][0]: word, schema[1][0]: '1' }


            collect[words[i]] = rec;

        else:

             freq = int(collect[words[i]][schema[1][0]])

             collect[words[i]][schema[1][0]] = str(freq + 1)


    for key in collect.keys():

        freq = int(collect[key][schema[1][0]])

        hist = ''

        for i in range(freq): hist += '\u25A0'

        if len(hist) > int(schema[2][1]):
            hist = hist[:int(schema[2][1]) - 1] + '+'

        collect[key][schema[2][0]] = hist;
