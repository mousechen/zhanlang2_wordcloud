#-*- coding:gbk -*-
import codecs
from os import path

import jieba
from scipy.misc import imread
from wordcloud import WordCloud
import pandas as pd

# ���������ʱû���õ�
def get_all_keywords(file_name):
    word_lists = []  # �ؼ����б�
    jieba.enable_parallel(8)
    with codecs.open(file_name, 'r', encoding='utf-8') as f:
        Lists = f.readlines()  # �ı��б�
        for List in Lists:
            cut_list = list(jieba.cut(List))
            for word in cut_list:
                word_lists.append(word)
    word_lists_set = set(word_lists)  # ȥ���ظ�Ԫ��
    word_lists_set = list(word_lists_set)
    length = len(word_lists_set)
    print u"����%d���ؼ���" % length
    information = pd.read_excel('/Users/huazi/Desktop/zhanlang2.xlsx')
    world_number_list = []
    word_copy=[]
    for w in word_lists_set:
        if (len(w) == 1):
            continue
        if (word_lists.count(w) > 3):
            world_number_list.append(word_lists.count(w))
            word_copy.append(w)
    information['key'] = word_copy
    information['count'] = world_number_list
    information.to_excel('sun_2.xlsx')


# ���ƴ���
def save_jieba_result():
    # ���ö��߳��и�
    jieba.enable_parallel(4)
    dirs = path.join(path.dirname(__file__), '../pjl_comment.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()
    cut_text = " ".join(jieba.cut(comment_text))  # ��jieba�ִʵõ��Ĺؼ����ÿո����ӳ�Ϊ�ַ���
    with codecs.open('pjl_jieba.txt', 'a', encoding='utf-8') as f:
        f.write(cut_text)


def draw_wordcloud2():
    dirs = path.join(path.dirname(__file__), 'pjl_jieba.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()

    color_mask = imread("template.png")  # ��ȡ����ͼƬ

    stopwords = [u'����', u'��Ӱ', u'����', u'��ô', u'����', u'����', u'ʲô', u'û��', u'���', u'�Ǹ�', u'���', u'�Ƚ�', u'����', u'����',
                 u'����', u'ʱ��', u'�Ѿ�', u'����']
    cloud = WordCloud(font_path="/Users/huazi/Desktop/simsunttc/simsun.ttc", background_color='white',
                      max_words=2000, max_font_size=200, min_font_size=4, mask=color_mask, stopwords=stopwords)
    word_cloud = cloud.generate(comment_text)  # ��������
    word_cloud.to_file("pjl_cloud.jpg")


save_jieba_result()
draw_wordcloud2()
