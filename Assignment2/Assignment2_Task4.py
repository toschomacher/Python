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
    myString = "Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh hvwg kcfzr kog" \
               " pswbu kohqvsr yssbzm obr qzcgszm pm wbhszzwusbqsg ufsohsf hvob aob'g obr msh og acfhoz og vwg" \
               " ckb; hvoh og asb pigwsr hvsagszjsg opcih hvswf jofwcig qcbqsfbg hvsm ksfs gqfihwbwgsr obr ghirwsr," \
               " dsfvodg ozacgh og boffckzm og o aob kwhv o awqfcgqcds awuvh gqfihwbwgs hvs hfobgwsbh qfsohifsg" \
               " hvoh gkofa obr aizhwdzm wb o rfcd ct kohsf. Kwhv wbtwbwhs qcadzoqsbqm asb ksbh hc obr tfc cjsf" \
               " hvwg uzcps opcih hvswf zwhhzs ottowfg, gsfsbs wb hvswf oggifobqs ct hvswf sadwfs cjsf aohhsf." \
               " Wh wg dcggwpzs hvoh hvs wbtigcfwo ibrsf hvs awqfcgqcds rc hvs goas. Bc cbs uojs o hvciuvh hc" \
               " hvs czrsf kcfzrg ct gdoqs og gcifqsg ct viaob robusf, cf hvciuvh ct hvsa cbzm hc rwgawgg hvs" \
               " wrso ct zwts idcb hvsa og wadcggwpzs cf wadfcpopzs. Wh wg qifwcig hc fsqozz gcas ct hvs asbhoz" \
               " vopwhg ct hvcgs rsdofhsr romg. Oh acgh hsffsghfwoz asb tobqwsr hvsfs awuvh ps chvsf asb idcb" \
               " Aofg, dsfvodg wbtsfwcf hc hvsagszjsg obr fsorm hc kszqcas o awggwcbofm sbhsfdfwgs. Msh oqfcgg" \
               " hvs uizt ct gdoqs, awbrg hvoh ofs hc cif awbrg og cifg ofs hc hvcgs ct hvs psoghg hvoh dsfwgv," \
               " wbhszzsqhg jogh obr qccz obr ibgmadohvshwq, fsuofrsr hvwg sofhv kwhv sbjwcig smsg, obr gzckzm" \
               " obr gifszm rfsk hvswf dzobg ouowbgh ig. Obr sofzm wb hvs hksbhwshv qsbhifm qoas hvs ufsoh" \
               " rwgwzzigwcbasbh."

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
                    'was', 'been', 'is', 'are', 'fire', 'future', 'wrong', 'involve', 'defense', 'anyone',
                    'increase', 'security', 'bank', 'myself', 'certainly', 'sport', 'board', 'seek', 'per',
                    'subject', 'officer', 'private', 'rest', 'behaviour', 'deal', 'performance', 'fight',
                    'throw', 'top', 'quickly', 'past', 'goal', 'bed', 'order', 'author', 'fill', 'represent',
                    'focus', 'foreign', 'drop', 'plan', 'blood', 'upon', 'agency', 'push', 'nature', 'recently',
                    'store', 'reduce', 'sound', 'note', 'fine', 'before', 'near', 'movement', 'page', 'enter',
                    'share', 'common', 'poor', 'natural', 'race', 'concern', 'series', 'significant', 'similar',
                    'hot', 'language', 'usually', 'response', 'dead', 'rise', 'factor', 'decade', 'article',
                    'save', 'artist', 'scene', 'stock', 'career', 'despite', 'central', 'thus', 'treatment',
                    'beyond', 'happy', 'exactly', 'protect', 'approach', 'lie', 'size', 'fund', 'serious', 'occur',
                    'media', 'ready', 'sign', 'thought', 'list', 'individual', 'simple', 'quality', 'pressure',
                    'accept', 'decline', 'answer', 'resource', 'identify', 'meeting', 'left', 'determine',
                    'prepare', 'disease', 'whatever', 'success', 'argue', 'cup', 'particularly', 'amount',
                    'ability', 'staff', 'recognize', 'indicate', 'character', 'growth', 'loss', 'degree',
                    'wonder', 'attack', 'herself', 'region', 'television', 'box', 'tv', 'training', 'pretty',
                    'trade', 'deal', 'election', 'everybody', 'physical', 'lay', 'general', 'feeling',
                    'standard', 'bill', 'message', 'fail', 'outside', 'inside', 'arrive', 'analysis', 'benefit',
                    'sex', 'forward', 'backward', 'lawyer', 'present', 'section', 'environmental', 'glass',
                    'answer', 'skill', 'professor', 'operation', 'financial', 'crime', 'stage', 'ok', 'compare',
                    'authority', 'miss', 'design', 'sort', 'act', 'knowledge', 'station', 'state', 'strategy',
                    'clearly', 'discuss', 'indeed', 'force', 'truth', 'lie', 'song', 'example', 'check', 'leg',
                    'foot', 'finger', 'toe', 'nail', 'sharp', 'fragile', 'soft', 'dark', 'various', 'rather',
                    'laugh', 'guess', 'executive', 'prove', 'hang', 'entire', 'rock', 'design', 'enough', 'forget',
                    'claim', 'remove', 'copy', 'paste', 'delete', 'manager', 'boss', 'supervisor', 'client',
                    'enjoy', 'network', 'legal', 'religious', 'cold', 'warm', 'form', 'final', 'main', 'science',
                    'memory', 'card', 'above', 'seat', 'cell', 'sea', 'ocean', 'salt', 'bit', 'establish', 'nice',
                    'trial', 'expert', 'firm', 'radio', 'visit', 'management', 'care', 'avoid', 'imagine',
                    'tonight', 'huge', 'ball', 'stall', 'limp', 'finish', 'yourself', 'talk', 'theory', 'impact',
                    'respond', 'statement', 'maintain', 'charge', 'popular', 'traditional', 'onto', 'reveal',
                    'direction', 'weapon', 'employee', 'employer', 'cultural', 'contain', 'peace', 'head', 'control',
                    'base', 'pain', 'apply', 'cancel', 'cancellation', 'play', 'wide', 'narrow', 'shake', 'fly',
                    'gear', 'gears', 'shaft', 'interview', 'chair', 'fish', 'particular', 'camera', 'structure',
                    'perform', 'weight', 'suddenly', 'discover', 'candidate', 'bottom', 'grater', 'smaller', }
    # company is number 189 in the list

    success = 0
    for n in range(1, 27):
        counter = 0
        encryptedString = caesar(myString, n)
        compare_list = re.sub("[^\w]", " ", encryptedString).split()
        total_number_words = len(compare_list)
        for word in compare_list:
            if word.lower() in set_of_words:
                counter += 1
        if (counter/total_number_words*100) > 50:
            print(encryptedString)
            print(format(counter/total_number_words*100, '.2f'), '% match')
            success = 1
    if success == 0:
        print('Cannot decrypt. Most likely not a Caesar Cypher at work here.')
