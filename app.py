import nltk

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
    result = model(text, min_length=60)
    print("BERT_Summarizer min_length=60")
    display(result)
    model = Summarizer()
    result = model(text, ratio=0.2)  # Specified with ratio
    print("BERT_Summarizer ratio=0.2")
    display(result)
    result = model(text, num_sentences=3)
    print("BERT_Summarizer num_sentences=3")
    display(result)
    # pip install -U sentence-transformers
    from summarizer.sbert import SBertSummarizer
    model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
    result = model(text, num_sentences=3)
    print("SBertSummarizer num_sentences=3")
    display(result)

def Rake_Summarizer(text):
    from rake_nltk import Metric, Rake
    r = Rake(language="russian")
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()[:15]
    print("Rake_Summarizer 0:15")
    display(keywords)

def Yake_Summarizer(text):
    import yake
    language = "ru"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    print("Yake_Summarizer")
    display(keywords)

def nltk_download():
    nltk.download('stopwords')
    nltk.download('punkt')

    
def get_KeyBERT(text):
    from keybert import KeyBERT
    kw_model = KeyBERT()
    # keywords = kw_model.extract_keywords(doc)
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 3), stop_words='english',
                            use_maxsum=True, nr_candidates=20, top_n=10)
    print("KeyBERT")
    display(keywords)


# def remove_stopwords():
#     str2 = ''
#     russian_stopwords = nltk.corpus.words("russian")
#     for word in data.split():
#         if word not in (russian_stopwords):
#             str2 = str2 + " " + word
#     data = str2

# As per Gensim’s Github changelog 188, 
# gensim.summarization module has been removed in versions Gensim 4.x
# from gensim.summarization import summarize 
# def TextRank_Summarizer(ttext):
#     # pip install gensim==3.8.3
#     return summarize(str(ttext))


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
    nltk_download()
    BERT_Summarizer(text)
    Rake_Summarizer(text)
    Yake_Summarizer(text)