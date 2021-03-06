import pandas as pd
import numpy as np


from pandas.plotting import scatter_matrix #导入散点图矩阵包
import matplotlib.pyplot as plt
from sklearn import model_selection 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC 


if __name__ == '__main__':
	url = r"train_new.csv"
	#names = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'class']
	data = pd.read_csv(url)
	data['review'] = data['review_text'].map(str) + data['review_summary'].map(str)
	data_1 = data.loc[:,['review','fit']]
	
	print(data_1)
	data_1.to_csv('Newcsv.csv')







#coding=gbk

import pickle
import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM, Dense, Embedding, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 导入数据
# 文件的数据中，特征为evaluation, 类别为label.
def load_data(filepath, input_shape=20):
    df = pd.read_csv(filepath)

    # 标签及词汇表
    labels, vocabulary = list(df['fit'].unique()), list(df['review'].unique())

    # 构造字符级别的特征
    string = ''
    for word in vocabulary:
        string += word

    vocabulary = set(string)

    # 字典列表
    word_dictionary = {word: i+1 for i, word in enumerate(vocabulary)}
    with open('word_dict.pk', 'wb') as f:
        pickle.dump(word_dictionary, f)
    inverse_word_dictionary = {i+1: word for i, word in enumerate(vocabulary)}
    label_dictionary = {label: i for i, label in enumerate(labels)}
    with open('label_dict.pk', 'wb') as f:
        pickle.dump(label_dictionary, f)
    output_dictionary = {i: labels for i, labels in enumerate(labels)}

    vocab_size = len(word_dictionary.keys()) # 词汇表大小
    label_size = len(label_dictionary.keys()) # 标签类别数量

    # 序列填充，按input_shape填充，长度不足的按0补充
    x = [[word_dictionary[word] for word in sent] for sent in df['review']]
    x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)
    y = [[label_dictionary[sent]] for sent in df['fit']]
    y = [np_utils.to_categorical(label, num_classes=label_size) for label in y]
    y = np.array([list(_[0]) for _ in y])

    return x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary

# 创建深度学习模型， Embedding + LSTM + Softmax.
def create_LSTM(n_units, input_shape, output_dim, filepath):
    x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary = load_data(filepath)
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size + 1, output_dim=output_dim,
                        input_length=input_shape, mask_zero=True))
    model.add(LSTM(n_units, input_shape=(x.shape[0], x.shape[1])))
    model.add(Dropout(0.2))
    model.add(Dense(label_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.summary()

    return model

# 模型训练
def model_train(input_shape, filepath, model_save_path):

    # 将数据集分为训练集和测试集，占比为9:1
    # input_shape = 100
    x, y, output_dictionary, vocab_size, label_size, inverse_word_dictionary = load_data(filepath, input_shape)
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.1, random_state = 42)

    # 模型输入参数，需要自己根据需要调整
    n_units = 100
    batch_size = 32
    epochs = 5
    output_dim = 20

    # 模型训练
    lstm_model = create_LSTM(n_units, input_shape, output_dim, filepath)
    lstm_model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1)

    # 模型保存
    lstm_model.save(model_save_path)

    N = test_x.shape[0]  # 测试的条数
    predict = []
    label = []
    for start, end in zip(range(0, N, 1), range(1, N+1, 1)):
        sentence = [inverse_word_dictionary[i] for i in test_x[start] if i != 0]
        y_predict = lstm_model.predict(test_x[start:end])
        label_predict = output_dictionary[np.argmax(y_predict[0])]
        label_true = output_dictionary[np.argmax(test_y[start:end])]
        print(''.join(sentence), label_true, label_predict) # 输出预测结果
        predict.append(label_predict)
        label.append(label_true)

    acc = accuracy_score(predict, label) # 预测准确率
    print('模型在测试集上的准确率为: %s.' % acc)

if __name__ == '__main__':
    filepath = './Newcsv.csv'
    input_shape = 100
    model_save_path = './corpus_model.h5'
    model_train(input_shape, filepath, model_save_path)

http://c-s-a.org.cn/html/2018/8/6483.html


https://www.jianshu.com/p/158c3f02a15b

https://www.jiqizhixin.com/articles/LSTM-implement-in-Keras

网络购物在给人们带来便捷的同时也具有很多不可避免的弊端, 无法真实的感受到商品的属性与尺寸, 为购买商品带来了很大的风险。
所以我们经常都会查看产品的各种属性以及别人留下的评论信息在我们做出购买商品决策之前来提供参考.
对商品评论信息的情感倾向分析不仅能够在消费者购买商品是提供指导, 也可以使商家客观的认识到自己商品的优缺点,来改进自己的商品.
因此对商品评论的文本情感分析不仅具有巨大的商业上的价值也可以对学术研究用到实际领域起到很好的推动作用。
本文将采用LSTM模型，训练一个能够识别评价文本small, fit, large三种评价的分类器。


