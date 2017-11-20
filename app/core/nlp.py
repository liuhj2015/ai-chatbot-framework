#coding:utf-8
from nltk.tag.perceptron import PerceptronTagger
from nltk import word_tokenize
import jieba
import jieba.posseg
from app.commons.logger import logger
from app import app

# Load and initialize Perceptron tagger
tagger = PerceptronTagger()


Chinese = app.config["CHINESE"]

def posTaggerEnglish(sentence):
    tokenizedSentence = word_tokenize(sentence)
    posTaggedSentence = tagger.tag(tokenizedSentence)
    return posTaggedSentence


def posTagger(sentence):

    if Chinese:
    
    #return posTaggerEnglish(sentence)
        return posTaggerChinese(sentence)
    else:
        return posTaggerEnglish(sentence)

def posTaggerChinese(sentence):
    tokenizedSentence = jieba.posseg.cut(sentence)
    posTaggedSentence = [(token,postag) for token, postag in tokenizedSentence]
    return posTaggedSentence
    

def posTagAndLabelEnglish(sentence):
    taggedSentence = posTagger(sentence)
    taggedSentenceJson = []
    for token, postag in taggedSentence:
        taggedSentenceJson.append([token, postag, "O"])
    return taggedSentenceJson

def posTagAndLabel(sentence):
    
    if Chinese:
        return posTagAndLabelChinese(sentence)
    else:
        return posTagAndLabelEnglish(sentence)

def posTagAndLabelChinese(sentence):
    taggedSentence = posTaggerChinese(sentence)
    taggedSentenceJson = []
    for token,postag in taggedSentence:
        taggedSentenceJson.append([token, postag, "0"])
    return taggedSentenceJson

def sentenceTokenize(sentences):
    if Chinese:
        return sentenceTokenizeChinese(sentences)
    else:
        return sentenceTokenizeEnglish(sentences)

def sentenceTokenizeEnglish(sentences):
    tokenizedSentences = word_tokenize(sentences)
    tokenizedSentencesPlainText = ""
    for t in tokenizedSentences:
        tokenizedSentencesPlainText += " " + t
    return tokenizedSentencesPlainText

def sentenceTokenizeChinese(sentences):
    tokenizedSentences = jieba.cut(sentences)
    tokenizedSentencesPlainText = ""
    for t in tokenizedSentences:
        tokenizedSentencesPlainText += " " + t
    return tokenizedSentencesPlainText
