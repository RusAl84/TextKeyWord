# from gensim.summarization import summarize
from summarizer import Summarizer
from rake_nltk import Metric, Rake

def load_data(filename='data.txt'):
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read()
    return data

def remove_from_patterns(text, pattern):
    str2 = ''
    for c in text:
        if c not in pattern:
            str2 = str2 + c
    return str2

def display(text):
    print(text) 
    print("--------------------------------")

def remove_paragraf_and_toLower(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = ' '.join([k for k in text.split(" ") if k])
    return text

def BERT_Summarizer(text):
    # https://github.com/dmmiller612/bert-extractive-summarizer
    # pip install bert-extractive-summarizer
    # pip install ...etc
    from summarizer import Summarizer
    model = Summarizer()
    result = model(text, min_length=20)
    model = Summarizer()
    # result = model(text, ratio=0.2)  # Specified with ratio
    result = model(text, num_sentences=3)
    # full = ''.join(result)
    return result

# def TextRank_Summarizer(ttext):
#     # pip install gensim==3.8.3
#     # As per Gensim’s Github changelog 188, 
#     # gensim.summarization module has been removed in versions Gensim 4.x
#     return summarize(str(ttext))

def Rake_Summarizer(text):
    
    r = Rake(language="russian")
    r.extract_keywords_from_text(text)
    mas = r.get_ranked_phrases()
    set2 = set()
    for item in mas:
        if not "nan" in str(item).replace(" nan ", " "):
            set2.add(str(item).replace(" nan ", " "))
    mas = list(set2)
    return str(mas)

# def remove_stopwords(self):
#     str2 = ''
#     russian_stopwords = stopwords.words("russian")
#     for word in self.data.split():
#         if word not in (russian_stopwords):
#             str2 = str2 + " " + word
#     self.data = str2

# def remove_short_words(self, length=1):
#     str2 = ''
#     for line in self.data.split("\n"):
#         str3 = ""
#         for word in line.split():
#             if len(word) > length:
#                 str3 += " " + word
#         str2 = str2 + "\n" + str3
#     self.data = str2

if __name__ == '__main__':
    text=load_data()
    display(text)
    # digit=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # import string
    # punctuation = list(string.punctuation)
    # punctuation_extend=['«', '»', '–', "-", "—", "\""]
    # patern = digit + punctuation_extend + punctuation
    # text = remove_from_patterns(text, patern)
    # display(text)
    # display(punctuation)
    # text = remove_paragraf_and_toLower(text)
    # display(text)
    keyWords = BERT_Summarizer(text)
    display(keyWords)
    # keyWords = TextRank_Summarizer(text)
    # display(keyWords)
    keyWords = Rake_Summarizer(text)
    display(keyWords)