from keybert import KeyBERT

doc = """
    Завтра в "Папа Джонс" самый черный пятничный праздник!🖤
    Мы знаем, что ты так же обожаешь скидки, поэтому держи подарок от нас - 100% начисления Black CashBack за все заказы 24.11.2023. 
    Успей воспользоваться Black CashBack, потому что он действует всего 3 дня!

    Такая возможность выпадает раз в году – съесть пиццу и получить такой огромный Black CashBack!

    Время тикает!

    """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)

str1 = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 3), stop_words='english',
                        use_maxsum=True, nr_candidates=20, top_n=10)
print(str1)