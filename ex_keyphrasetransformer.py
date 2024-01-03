from keyphrasetransformer import KeyPhraseTransformer
#https://github.com/Shivanandroy/KeyPhraseTransformer

kp = KeyPhraseTransformer()

doc = """
Завтра в "Папа Джонс" самый черный пятничный праздник!🖤
Мы знаем, что ты так же обожаешь скидки, поэтому держи подарок от нас - 100% начисления Black CashBack за все заказы 24.11.2023. 
Успей воспользоваться Black CashBack, потому что он действует всего 3 дня!

Такая возможность выпадает раз в году – съесть пиццу и получить такой огромный Black CashBack!

Время тикает!

"""

str1=kp.get_key_phrases(doc)

print(str1)