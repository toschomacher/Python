#!/usr/bin/env python3

import string
import re


def caesar(input_string: str, rotation: int = 1) -> str:
    key = {}
    for ch in string.ascii_lowercase:
        key[ch] = chr((ord(ch) - ord('a') + rotation) % 26 + ord('a'))
    translation_table_low = str.maketrans(key)

    rot = {}
    for cap in string.ascii_uppercase:
        rot[cap] = chr((ord(cap) - ord('A') + rotation) % 26 + ord('A'))
    translation_table_up = str.maketrans(rot)

    translation_table = translation_table_low | translation_table_up
    return input_string.translate(translation_table)


if __name__ == "__main__":
    myString = "Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh hvwg kcfzr kog pswbu"

    set_of_words = {'be', 'and', 'of', 'a', 'in', 'to', 'have', 'too', 'it', 'I', 'that', 'for', 'you',
                    'he', 'with', 'on', 'do', 'say', 'this', 'they', 'at', 'but', 'we', 'his', 'from',
                    'that', 'not', "can't", "won't", 'by', 'she', 'or', 'as', 'what', 'go', 'their', 'can',
                    'who', 'get', 'if', 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will', 'as',
                    'up', 'one', 'time', 'there', 'year', 'so', 'think', 'when', 'which', 'them', 'some',
                    'me', 'people', 'take', 'out', 'into', 'just', 'see', 'him', 'your', 'come', 'could',
                    'now', 'that', 'like', 'other', 'how', 'then', 'its', 'our', 'two', 'more', 'these',
                    'want', 'way', 'look', 'first', 'also', 'new', 'because', 'day', 'more', 'use', 'no',
                    'man', 'find', 'here', 'thing', 'give', 'many', 'well', 'only', 'those', 'tell', 'one',
                    'very', 'her', 'even', 'back', 'any', 'good', 'woman', 'though', 'us', 'life', 'child',
                    'there', 'work', 'down', 'may', 'after', 'should', 'call', 'world', 'over', 'school',
                    'still', 'try', 'in', 'last', 'ask', 'need', 'too', 'feel', 'three', 'when', 'state',
                    'never', 'become', 'between', 'high', 'really', 'something', 'most', 'another', 'much',
                    'family', 'own', 'out', 'leave', 'put', 'old', 'while', 'mean', 'student', 'keep', 'why',
                    'let', 'great', 'same', 'big', 'group', 'begin', 'seem', 'country', 'help', 'talk',
                    'where', 'turn', 'problem', 'every', 'start', 'hand', 'might', 'american', 'show', 'part',
                    'about', 'against', 'place', 'over', 'such', 'again', 'few', 'case', 'most', 'week',
                    'company', 'where', 'system', 'each', 'right', 'program', 'hear', 'so', 'question', 'during',
                    'work', 'play', 'government', 'run', 'small', 'number', 'off', 'always', 'move', 'like',
                    'night', 'live', 'mr.', 'point', 'believe', 'hold', 'today', 'bring', 'happen', 'next',
                    'without', 'before', 'large', 'million', 'must', 'home', 'under', 'water', 'room', 'write',
                    'mother', 'area', 'national', 'money', 'story', 'young', 'fact', 'month', 'different',
                    'lot', 'study', 'right', 'book', 'eye', 'job', 'word', 'though', 'business', 'issue', 'side',
                    'kind', 'four', 'head', 'far', 'black', 'long', 'both', 'little', 'house', 'yes', 'after',
                    'since', 'long', 'provide', 'service', 'around', 'friend', 'important', 'father', 'sit',
                    'away', 'until', 'power', 'hour', 'game', 'often', 'yet', 'line', 'political', 'end', 'among',
                    'ever', 'stand', 'bad', 'lose', 'however', 'member', 'pay', 'law', 'meet', 'car', 'city',
                    'almost', 'include', 'continue', 'set', 'later', 'community', 'much', 'name', 'five', 'once',
                    'while', 'least', 'president', 'learn', 'real', 'change', 'team', 'minute', 'best', 'several',
                    'idea', 'kid', 'body', 'information', 'nothing', 'ago', 'right', 'lead', 'social',
                    'understand', 'whether', 'back', 'watch', 'together', 'follow', 'around', 'parent', 'only',
                    'stop', 'face', 'anything', 'create', 'public', 'already', 'speak', 'others', 'read', 'level',
                    'allow', 'add', 'office', 'spend', 'door', 'health', 'person', 'art', 'sure', 'such',
                    'war', 'history', 'party', 'within', 'grow', 'result', 'open', 'change', 'morning', 'walk',
                    'reason', 'low', 'win', 'research', 'girl', 'guy', 'early', 'food', 'before', 'moment',
                    'himself', 'air', 'teacher', 'force', 'offer', 'enough', 'both', 'education', 'across',
                    'although', 'remember', 'foot', 'second', 'boy', 'maybe', 'toward', 'able', 'age', 'policy',
                    'everything', 'love', 'process', 'music', 'including', 'consider', 'appear', 'actually', 'buy',
                    'probably', 'human', 'wait', 'serve', 'market', 'die', 'send', 'expect', 'home', 'sense',
                    'build', 'stay', 'fall', 'oh', 'nation', 'plan', 'cut', 'college', 'interest', 'death',
                    'course', 'someone', 'experience', 'behind', 'reach', 'local', 'kill', 'siz', 'remain',
                    'effect', 'use', 'yeah', 'suggest', 'class', 'control', 'raise', 'care', 'perhaps', 'little',
                    'late', 'hard', 'field', 'else', 'pass', 'former', 'sell', 'major', 'sometimes', 'require',
                    'along', 'development', 'themselves', 'report', 'role', 'better', 'economic', 'effort', 'up',
                    'decide', 'rate', 'strong', 'possible', 'heart', 'drug', 'show', 'leader', 'light', 'voice',
                    'wife', 'whole', 'police', 'mind', 'finally', 'pull', 'return', 'free', 'military', 'price',
                    'report', 'less', 'according', 'decision', 'explain', 'son', 'hope', 'even', 'develop', 'view',
                    'relationship', 'cary', 'town', 'road', 'drive', 'arm', 'true', 'federal', 'break', 'better',
                    'difference', 'thank', 'receive', 'value', 'international', 'building', 'action', 'full',
                    'model', 'join', 'season', 'society', 'tax', 'director', 'early', 'position', 'player',
                    'agree', 'especially', 'record', 'pick', 'wear', 'paper', 'special', 'space', 'ground',
                    'form', 'support', 'event', 'official', 'whose', 'matter', 'everyone', 'center', 'couple',
                    'site', 'project', 'hit', 'base', 'activity', 'star', 'table', 'court', 'produce', 'eat',
                    'american', 'britain', 'british', 'english', 'england', 'europe', 'european', 'century',
                    'unless', 'teach', 'oil', 'gas', 'half', 'situation', 'easy', 'difficult', 'cost', 'industry',
                    'figure', 'animal', 'dog', 'cat', 'and', 'bear', 'snake', 'python', 'giraf', 'spider', 'web',
                    'address', 'color', 'colour', 'red', 'green', 'blue', 'white', 'black', 'yellow', 'orange',
                    'purple', 'violet', 'amber', 'gray', 'horse', 'donkey', 'knight', 'sword', 'gun', 'machine',
                    'tyre', 'tire', 'thread', 'circle', 'square', 'triangle', 'rectangle', 'side', 'years',
                    'stone', 'rock', 'sand', 'dust', 'paper', 'scissors', 'wheel', 'keyboard', 'mouse', 'cable',
                    'lip', 'lips', 'street', 'image', 'itself', 'phone', 'either', 'data', 'cover', 'quite',
                    'picture', 'photo', 'shot', 'screen', 'clear', 'practice', 'piece', 'land', 'recent', 'wall',
                    'describe', 'product', 'doctor', 'patient', 'worker', 'news', 'test', 'movie', 'certain',
                    'north', 'south', 'east', 'west', 'diagonal', 'opened', 'closed', 'close', 'supported',
                    'simply', 'simple', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                    'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'technology', 'catch', 'step', 'baby',
                    'computer', 'type', 'attention', 'draw', 'film', 'tree', 'branch', 'grass', 'source', 'skin',
                    'nearly', 'organisation', 'choose', 'cause', 'hair', 'look', 'point', 'evidence', 'window',
                    'operation', 'system', 'difficult', 'listen', 'soon', 'culture', 'billion', 'chance', 'brother',
                    'sister', 'energy', 'period', 'course', 'summer', 'autumn', 'winter', 'spring', 'less',
                    'realise', 'hundred', 'available', 'plant', 'likely', 'opportunity', 'term', 'short', 'letter',
                    'glue', 'silicon', 'tape', 'measure', 'measuring', 'hole', 'tiny', 'giant', 'tale',
                    'condition', 'choice', 'place', 'single', 'double', 'triple', 'rule', 'rules', 'ruler',
                    'basket', 'bag', 'carrier', 'bolt', 'nut', 'pressure', 'spread', 'daughter', 'son', 'admin',
                    'administration', 'husband', 'floor', 'campaign', 'material', 'population', 'earth', 'well',
                    'call', 'economy', 'medical', 'doctor', 'nurse', 'eleventh', 'twelfth', 'thirteenth',
                    'fourteenth', 'fifteenth', 'sixteenth ', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth',
                    'was', 'been', 'is', 'are', '', '', '', '', '', '', '', '', '', '', '', }
    # company is number 189 in the list
    print("one" in set_of_words)
    print(set_of_words)
    print(type(set_of_words))
    for n in range(1, 27):
        counter = 0
        encryptedString = caesar(myString, n)
        compare_list = re.sub("[^\w]", " ", encryptedString).split()
        total_number_words = len(compare_list)
        for word in compare_list:
            if word.lower() in set_of_words:
                counter += 1
        if (counter/total_number_words*100) > 60:
            print(encryptedString)
            print(counter/total_number_words*100)
