blacklist = [
    'be', 'is', 'are', 'was', 'were',  # forms of "be"
    'have', 'has', 'had',  # forms of "have"
    'do', 'does', 'did',  # forms of "do"
    'go', 'goes', 'went', 'gone', 'going',  # forms of "go"
    'make', 'makes', 'made', 'making',  # forms of "make"
    'take', 'takes', 'took', 'taken', 'taking',  # forms of "take"
    'get', 'gets', 'got', 'gotten', 'getting',  # forms of "get"
    'use', 'uses', 'used', 'using',  # forms of "use"
    'want', 'wants', 'wanted', 'wanting',  # forms of "want"
    'need', 'needs', 'needed', 'needing',  # forms of "need"
    'like', 'likes', 'liked', 'liking',  # forms of "like"
    'go', 'goes', 'went', 'going', 'gone',  # forms of "go"
    'see', 'sees', 'saw', 'seeing',  # forms of "see"
    'say', 'says', 'said', 'saying',  # forms of "say"
    'think', 'thinks', 'thought', 'thinking',  # forms of "think"
    'know', 'knows', 'knew', 'known', 'knowing',  # forms of "know"
    'come', 'comes', 'came', 'coming',  # forms of "come"
    'give', 'gives', 'gave', 'given', 'giving',  # forms of "give"
    'find', 'finds', 'found', 'finding',  # forms of "find"
    'tell', 'tells', 'told', 'telling',  # forms of "tell"
    'ask', 'asks', 'asked', 'asking',  # forms of "ask"
    'work', 'works', 'worked', 'working',  # forms of "work"
    'try', 'tries', 'tried', 'trying',  # forms of "try"
    'take', 'takes', 'took', 'taken', 'taking',  # forms of "take"
    'call', 'calls', 'called', 'calling',  # forms of "call"
    'can', 'could',  # forms of "can"
    'will', 'would',  # forms of "will"
    'may', 'might',  # forms of "may"
    'shall', 'should',  # forms of "shall"
    'must',  # form of "must"
    'good', 'better', 'best',  # forms of "good"
    'bad', 'worse', 'worst',  # forms of "bad"
    'high', 'higher', 'highest',  # forms of "high"
    'low', 'lower', 'lowest',  # forms of "low"
    'big', 'bigger', 'biggest',  # forms of "big"
    'small', 'smaller', 'smallest',  # forms of "small"
    'long', 'longer', 'longest',  # forms of "long"
    'short', 'shorter', 'shortest',  # forms of "short"
    'much', 'more', 'most',  # forms of "much"
    'few', 'fewer', 'fewest',  # forms of "few"
    'many', 'more', 'most',  # forms of "many"
    'some', 'any',  # forms of "some" and "any"
    'every', 'each',  # forms of "every" and "each"
    'all', 'whole',  # forms of "all" and "whole"
    'no', 'not', 'none',  # forms of "no" and "not"
    'other', 'another', 'else',  # forms of "other" and "else"
    'also', 'too',  # forms of "also" and "too"
    'then', 'there',  # forms of "then" and "there"
    'this', 'that', 'these', 'those',  # forms of "this" and "that"
    'which', 'who', 'whom',  # forms of "which", "who", and "whom"
    'where', 'when', 'why', 'how',  # forms of "where", "when", "why", and "how"
    "people",     "the", "and", "is", "in", "of", "to", "a", "on", "with", "for",
    "at", "by", "an", "it", "as", "from", "or", "that", "this", "which",
    "these", "those", "but", "not", "have", "has", "had", "do", "does",
    "did", "can", "could", "will", "would", "should", "must", "might", "may",
    "am", "are", "was", "were", "be", "been", "being", "i", "you", "he", "she",
    "it", "we", "they", "my", "your", "his", "her", "its", "our", "their",
    "me", "him", "her", "us", "them", "myself", "yourself", "himself", "herself",
    "itself", "ourselves", "themselves", "what", "who", "whom", "whose", "which",
    "how", "why", "where", "when", "while", "whoever", "whomever", "whatever",
    "whichever", "however", "whyever", "wherever", "whenever", "whatsoever",
    "a", "about", "above", "across", "after", "against", "all", "along", "among",
    "an", "and", "around", "as", "at", "back", "be", "because", "before", "behind",
    "below", "between", "both", "but", "by", "can", "cannot", "could", "did", "do",
    "does", "doing", "down", "during", "each", "either", "enough", "etc", "even",
    "ever", "every", "for", "from", "further", "get", "go", "had", "has", "have",
    "having", "he", "hence", "her", "here", "hers", "herself", "him", "himself",
    "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "itself",
    "just", "least", "less", "like", "may", "me", "might", "mine", "more", "most",
    "much", "must", "my", "myself", "neither", "no", "none", "nor", "not", "nothing",
    "now", "of", "off", "often", "on", "only", "or", "other", "our", "ours", "ourselves",
    "out", "over", "own", "per", "quite", "rather", "really", "same", "should", "so",
    "some", "somehow", "someone", "something", "somewhere", "still", "such", "than",
    "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these",
    "they", "this", "those", "through", "throughout", "thus", "to", "too", "under",
    "until", "up", "upon", "us", "very", "was", "we", "were", "what", "whatever",
    "when", "whence", "whenever", "where", "whereas", "wherever", "whether",
    "which", "while", "who", "whoever", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "you", "your", "yours", "yourself",
    "yourselves",
    "from", "as", "hey", "more", "either", "in", "and", "on", "an", "when", "too", "to", "i", "do", "can", "be",
     "that", "or", "the", "a", "of", "for", "is", "was", "the", "-PRON-", "actually", "likely", "possibly", "want",
     "make", "my", "someone", "sometimes_people", "sometimes", "would", "want_to",
     "one", "something", "sometimes", "everybody", "somebody", "could", "could_be", "mine", "us", "em",
     "0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "A", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst",
     "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af",
     "affected", "affecting", "after", "afterwards", "ag", "again", "against", "ah", "ain", "aj", "al", "all", "allow",
     "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst",
     "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone",
     "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appreciate", "approximately", "ar", "are",
     "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "au", "auth", "av", "available", "aw",
     "away", "awfully", "ax", "ay", "az", "b", "B", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "been",
     "before", "beforehand", "beginnings", "behind", "below", "beside", "besides", "best", "between", "beyond", "bi",
     "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but",
     "bx", "by", "c", "C", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "cc", "cd", "ce", "certain",
     "certainly", "cf", "cg", "ch", "ci", "cit", "cj", "cl", "clearly", "cm", "cn", "co", "com", "come", "comes", "con",
     "concerning", "consequently", "consider", "considering", "could", "couldn", "couldnt", "course", "cp", "cq", "cr",
     "cry", "cs", "ct", "cu", "cv", "cx", "cy", "cz", "d", "D", "d2", "da", "date", "dc", "dd", "de", "definitely",
     "describe", "described", "despite", "detail", "df", "di", "did", "didn", "dj", "dk", "dl", "do", "does", "doesn",
     "doing", "don", "done", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "E",
     "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "eg", "ei", "eight", "eighty", "either", "ej", "el",
     "eleven", "else", "elsewhere", "em", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es",
     "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone",
     "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "F", "f2", "fa", "far", "fc", "few",
     "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "five", "fix", "fj", "fl", "fn", "fo", "followed",
     "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front",
     "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "G", "ga", "gave", "ge", "get", "gets", "getting",
     "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr",
     "greetings", "gs", "gy", "h", "H", "h2", "h3", "had", "hadn", "happens", "hardly", "has", "hasn", "hasnt", "have",
     "haven", "having", "he", "hed", "hello", "help", "hence", "here", "hereafter", "hereby", "herein", "heres",
     "hereupon", "hes", "hh", "hi", "hid", "hither", "hj", "ho", "hopefully", "how", "howbeit", "however", "hr", "hs",
     "http", "hu", "hundred", "hy", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "ie", "if",
     "ig", "ignored", "ih", "ii", "ij", "il", "im", "immediately", "in", "inasmuch", "inc", "indeed", "index",
     "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "inward",
     "io", "ip", "iq", "ir", "is", "isn", "it", "itd", "its", "iv", "ix", "iy", "iz", "j", "J", "jj", "jr", "js", "jt",
     "ju", "just", "k", "K", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "ko", "l", "L", "l2", "la", "largely",
     "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets",
     "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr",
     "ls", "lt", "ltd", "m", "M", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me",
     "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mill", "million", "mine", "miss", "ml", "mn", "mo",
     "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "my",
     "n", "N", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "neither",
     "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none",
     "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "novel", "now", "nowhere", "nr", "ns", "nt",
     "ny", "o", "O", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi",
     "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq",
     "or", "ord", "os", "ot", "otherwise", "ou", "ought", "our", "out", "outside", "over", "overall", "ow", "owing",
     "own", "ox", "oz", "p", "P", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular",
     "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed",
     "please", "plus", "pm", "pn", "po", "poorly", "pp", "pq", "pr", "predominantly", "presumably", "previously",
     "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "Q", "qj", "qu",
     "que", "quickly", "quite", "qv", "r", "R", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really",
     "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively",
     "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm",
     "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "S", "s2", "sa", "said", "saw", "say", "saying",
     "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "seem", "seemed", "seeming", "seems", "seen",
     "sent", "seven", "several", "sf", "shall", "shan", "shed", "shes", "show", "showed", "shown", "showns", "shows",
     "si", "side", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somehow",
     "somethan", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified",
     "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially",
     "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "sz", "t", "T", "t1", "t2", "t3", "take",
     "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx",
     "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter",
     "thereby", "thered", "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these",
     "they", "theyd", "theyre", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou",
     "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip",
     "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried",
     "tries", "truly", "try", "trying", "ts", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "U", "u201d",
     "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto",
     "uo", "up", "upon", "ups", "ur", "us", "used", "useful", "usefully", "usefulness", "using", "usually", "ut", "v",
     "V", "va", "various", "vd", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt",
     "vu", "w", "W", "wa", "was", "wasn", "wasnt", "way", "we", "wed", "welcome", "well", "well-b", "went", "were",
     "weren", "werent", "what", "whatever", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas",
     "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who",
     "whod", "whoever", "whole", "whom", "whomever", "whos", "whose", "why", "wi", "widely", "with", "within",
     "without", "wo", "won", "wonder", "wont", "would", "wouldn", "wouldnt", "www", "x", "X", "x1", "x2", "x3", "xf",
     "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "Y", "y2", "yes", "yet", "yj", "yl", "you",
     "youd", "your", "youre", "yours", "yr", "ys", "yt", "z", "Z", "zero", "zi", "zz",
     "be", "have", "do", "say", "get", "make", "go", "know",
     "see", "come", "think", "look", "take", "use", "want",
     "give", "use", "tell", "ask", "work", "seem", "feel",
     "try", "leave", "call", "need", "help", "remember",
     "put", "set", "show", "move", "play", "turn", "start",
     "stop", "hold", "run", "bring", "write", "provide",
     "sit", "stand", "lose", "pay", "meet", "include",
     "continue", "set", "learn", "change", "lead", "understand"
]