import re
import string

from nltk import word_tokenize, SnowballStemmer
from nltk.corpus import stopwords

RussianSnowball_ = SnowballStemmer(language="russian")
EnglishSnowball_ = SnowballStemmer(language="english")


def russian_tokenizer(sentence: str):
    sentence = sentence.strip().lower()
    sentence.replace("\t", " ")
    for i in string.punctuation:
        if i in sentence and i != " ":
            sentence = sentence.replace(i, '')
    tokens = word_tokenize(sentence, language="russian")
    tokens = [i for i in tokens if i not in stopwords.words("russian")]
    tokens = [RussianSnowball_.stem(i) for i in tokens]
    return " ".join(tokens)


def english_tokenizer(sentence: str):
    sentence = sentence.strip().lower()
    sentence.replace("\t", " ")
    for i in string.punctuation:
        if i in sentence and i != " ":
            sentence = sentence.replace(i, '')
    tokens = word_tokenize(sentence, language="english")
    tokens = [i for i in tokens if i not in stopwords.words("english")]
    tokens = [EnglishSnowball_.stem(i) for i in tokens]
    return " ".join(tokens)


def get_toxicity(string_: str = None, models: list = None, vectorizers: list = None):
    if string_ is None or models is None or vectorizers is None:
        raise AttributeError("Argument not entered!")
    if len(re.findall(r'[а-я]', string_)) / len(string_) >= 0.5:
        toxic_propabality = models[0].predict_proba(vectorizers[0].transform(
            [russian_tokenizer(string_)]))[0, 1]
        return 1 if toxic_propabality >= 0.5 else 0, toxic_propabality
    else:
        toxic_propabality = models[1].predict_proba(vectorizers[1].transform(
            [english_tokenizer(string_)]))[0, 1]
        return 1 if toxic_propabality >= 0.5 else 0, toxic_propabality
