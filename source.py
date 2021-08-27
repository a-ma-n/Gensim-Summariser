import gensim
from gensim.summarization import summarize

#TODO:not working for integers
def no_words(text,no):
    # print(text)
    n=no
    summary2=summarize(text,word_count=n)
    print(summarize(text,word_count=no))
    print(summarize(text,word_count=n))
    print(summarize(text,word_count=int(no)))

    # print(summarize(text, ratio=0.5))
    print("\n")
    # print(summarize(text, word_count=50))
    return summary2


def shorten(text):
    summary=summarize(text)
    return summary

def ratio(text,rat):
    summary3=summarize(text,ratio=rat)
    return summary3
