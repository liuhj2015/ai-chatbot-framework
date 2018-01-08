#coding:utf-8

import jieba
import jieba.posseg as psseg

class TextSimilarity():
	
	def posTager(self,text):
		text = [(token,pos) for token,pos in psseg.cut(text)]
		return text


	def compute(self,text1,text2):
		posText1 = set(self.posTager(text1))
		posText2 = set(self.posTager(text2))
		






if __name__ == '__main__':
	 
	 textSimilarity = TextSimilarity()

	 textSimilarity.compute("我要定机票","我要定车票")









