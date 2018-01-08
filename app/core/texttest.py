#coding:utf-8

from textsimilarity import TextSimilarity


if __name__ == '__main__':
     
     textSimilarity = TextSimilarity()
     print textSimilarity.__dict__

     textSimilarity.compute("我要定机票","我要定车票")

