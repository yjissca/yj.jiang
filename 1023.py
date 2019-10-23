Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import jieba
>>> import numpy as np
>>> import pandas as pd
>>> import os
>>> os.chdir("E:\\nlp")
>>> data = pd.read_csv('Train_DataSet_Label.csv')
>>> data.head()
                                 id  label
0  7a3dd79f90ee419da87190cff60f7a86      2
1  7640a5589bc7486ca199eeeb38af79dd      1
2  8c5bda93e4ba401f90a0faa5b28fe57f      2
3  1aa777fed31a4b8a9d866f05b5477557      2
4  6c67ac55360340258e157f3710ebae6c      2
>>> data
                                    id  label
0     7a3dd79f90ee419da87190cff60f7a86      2
1     7640a5589bc7486ca199eeeb38af79dd      1
2     8c5bda93e4ba401f90a0faa5b28fe57f      2
3     1aa777fed31a4b8a9d866f05b5477557      2
4     6c67ac55360340258e157f3710ebae6c      2
...                                ...    ...
7350  0a8fbc25ea6a4241b9069919a8a88e1d      2
7351  54ef19d3fb1e4b8b8415623892868275      2
7352  0a9a42f8a78545f9b979fe5c7d33b33f      2
7353  87aca93ec1074c37a5e1ff14f9cdb253      2
7354  68680bb34bcf4829a04169885b4d92ff      2

[7355 rows x 2 columns]
>>> data.shape
(7355, 2)
>>> data = pd.read_csv('Train_DataSet.csv')
>>> data.shape
(7345, 3)
>>> data1 = pd.read_csv('Train_DataSet.csv')
>>> data2 = pd.read_csv('Train_DataSet_Label.csv')
>>> for i in range(0,data1.shape[0])
SyntaxError: invalid syntax
>>> data1.shape[0]
7345
>>> data1.id
0       7a3dd79f90ee419da87190cff60f7a86
1       7640a5589bc7486ca199eeeb38af79dd
2       8c5bda93e4ba401f90a0faa5b28fe57f
3       1aa777fed31a4b8a9d866f05b5477557
4       6c67ac55360340258e157f3710ebae6c
                      ...               
7340    0a8fbc25ea6a4241b9069919a8a88e1d
7341    54ef19d3fb1e4b8b8415623892868275
7342    0a9a42f8a78545f9b979fe5c7d33b33f
7343    87aca93ec1074c37a5e1ff14f9cdb253
7344    68680bb34bcf4829a04169885b4d92ff
Name: id, Length: 7345, dtype: object
>>> train_sen = data2.label
>>> train_sen
0       2
1       1
2       2
3       2
4       2
       ..
7350    2
7351    2
7352    2
7353    2
7354    2
Name: label, Length: 7355, dtype: int64
>>> train_sen.shape
(7355,)
>>> train_file = 'train.csv'
>>> train_data = []
>>> train
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    train
NameError: name 'train' is not defined
>>> train_header = ['title','label']
>>>  with open(test_label_file,'w',newline='') as f:
	ff = csv.writer(f)
	ff.writerow(label_header)
	
SyntaxError: unexpected indent
>>> with open(test_label_file,'w',newline='') as f:
	ff = csv.writer(f)
	ff.writerow(label_header)
	for i in range(0,data1.shape[0]):
		for j in range(i,data2.shape[0]):
			if data1.id[i]== data2.id[j]:
				row = [data1.title[i],data2.label[j]]
				ff.writerow(row)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    with open(test_label_file,'w',newline='') as f:
NameError: name 'test_label_file' is not defined
>>> with open(train_file,'w',newline='') as f:
	ff = csv.writer(f)
	ff.writerow(train_header)
	for i in range(0,data1.shape[0]):
		for j in range(i,data2.shape[0]):
			if data1.id[i]== data2.id[j]:
				row = [data1.title[i],data2.label[j]]
				ff.writerow(row)
				break

		
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    ff = csv.writer(f)
NameError: name 'csv' is not defined
>>> import csv
>>> with open(train_file,'w',newline='') as f:
	ff = csv.writer(f)
	ff.writerow(train_header)
	for i in range(0,data1.shape[0]):
		for j in range(i,data2.shape[0]):
			if data1.id[i]== data2.id[j]:
				row = [data1.title[i],data2.label[j]]
				ff.writerow(row)
				break

13
31
28
36
35
52
31
26
29
18
28
31
18
21
39
43
7
84
25
29
29
34
17
20
18
24
22
20
35
23
30
38
14
26
14
31
19
20
25
24
25
27
25
30
27
26
25
19
26
24
9
26
45
25
27
25
28
24
15
24
26
41
26
15
26
25
19
17
12
26
29
22
19
18
35
23
17
29
29
26
26
21
36
18
27
28
22
18
36
27
33
29
23
24
28
25
28
18
39
33
23
28
39
32
28
27
24
29
16
27
29
30
30
34
25
25
22
23
25
23
38
27
33
37
40
27
36
34
40
22
8
38
39
28
18
28
36
16
21
25
27
37
25
29
25
26
30
18
32
28
38
20
39
25
21
25
40
33
28
29
19
27
25
25
26
34
33
29
38
34
38
19
15
31
27
26
27
39
25
20
31
30
30
39
31
40
15
37
19
28
35
17
31
28
18
25
44
34
25
32
24
28
13
42
20
28
25
33
27
34
38
31
27
36
29
44
31
22
21
25
30
34
45
45
26
23
21
36
28
37
23
35
18
39
25
18
23
38
32
39
29
38
39
26
38
36
17
22
37
31
39
15
37
40
22
32
38
26
30
32
35
25
29
21
37
39
23
26
37
40
29
33
33
39
28
15
31
29
19
34
40
33
37
32
39
21
32
25
42
34
34
34
27
25
27
27
36
29
30
29
27
41
26
39
26
33
40
30
22
33
22
44
39
19
20
25
20
40
38
27
40
46
34
38
29
24
35
28
35
38
30
32
30
29
21
23
32
34
20
26
17
35
41
19
38
32
39
24
38
33
25
22
31
38
24
41
21
34
20
38
21
25
40
31
31
34
30
28
31
33
29
30
31
29
27
35
20
39
28
28
20
23
40
21
38
25
42
37
41
23
22
39
29
38
35
18
39
15
23
33
21
38
33
38
31
22
34
29
41
23
38
28
34
33
36
23
38
37
26
34
32
27
37
38
27
26
39
39
24
40
36
27
24
27
37
31
14
32
40
30
21
21
26
45
23
23
37
19
36
27
39
36
27
33
25
34
30
34
34
21
16
36
25
39
31
31
27
25
33
31
30
28
23
25
27
21
18
25
29
25
26
44
33
23
59
30
23
34
44
30
36
42
39
22
33
34
29
39
23
32
25
19
24
28
31
33
28
14
23
49
18
30
25
35
21
39
26
22
31
25
47
18
27
26
39
18
29
19
39
29
32
33
38
25
25
34
48
28
32
27
22
34
16
24
26
37
30
43
29
38
39
32
29
25
24
20
33
26
32
21
29
23
29
22
16
31
31
27
23
33
29
39
25
38
40
25
26
34
39
37
17
41
32
17
34
37
18
31
28
24
14
31
27
40
28
38
30
24
20
38
34
34
37
30
20
33
26
31
27
24
38
29
15
33
18
45
34
33
17
38
34
17
37
31
22
25
24
31
21
25
28
36
34
27
27
28
31
31
38
31
29
22
16
36
23
28
28
28
30
34
21
36
30
25
12
23
33
27
36
28
31
34
30
32
32
30
32
33
38
21
33
16
28
26
35
27
37
16
27
33
25
29
22
33
25
22
26
18
38
26
38
20
23
26
28
24
38
13
35
25
17
36
33
31
27
39
50
31
30
26
23
23
31
25
38
39
25
14
32
33
18
27
27
15
20
38
30
27
37
34
33
39
22
24
19
34
29
42
26
33
30
27
37
29
21
30
25
24
27
33
40
28
25
31
35
36
31
40
27
44
24
29
33
29
40
30
27
26
20
39
23
23
37
34
23
41
14
40
35
24
27
18
40
40
31
30
40
25
39
34
30
29
29
26
26
22
36
22
30
31
24
33
43
31
41
22
35
29
32
36
19
26
22
30
31
27
23
19
20
31
32
31
34
6
18
51
92
22
31
23
37
32
34
29
38
27
30
24
21
26
16
20
35
27
38
31
16
19
26
32
22
19
29
37
38
24
25
27
Traceback (most recent call last):
  File "<pyshell#45>", line 8, in <module>
    ff.writerow(row)
UnicodeEncodeError: 'gbk' codec can't encode character '\xa5' in position 0: illegal multibyte sequence
>>> for i in range(0,data1.shape[0]):
		for j in range(i,data2.shape[0]):
			if data1.id[i]== data2.id[j]:
				data1.commont[i] = data2.label[j]
				break

			
Traceback (most recent call last):
  File "<pyshell#47>", line 4, in <module>
    data1.commont[i] = data2.label[j]
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'commont'
>>> for i in range(0,data1.shape[0]):
		for j in range(i,data2.shape[0]):
			if data1.id[i]== data2.id[j]:
				data1.comment[i] = data2.label[j]
				break

			
Traceback (most recent call last):
  File "<pyshell#49>", line 4, in <module>
    data1.comment[i] = data2.label[j]
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'comment'
>>> for i in range(0,data1.shape[0]):
		for j in range(i,data2.shape[0]):
			if data1.id[i]== data2.id[j]:
				data1.content[i] = data2.label[j]
				break

			
>>> data1
                                    id  ... content
0     7a3dd79f90ee419da87190cff60f7a86  ...       2
1     7640a5589bc7486ca199eeeb38af79dd  ...       1
2     8c5bda93e4ba401f90a0faa5b28fe57f  ...       2
3     1aa777fed31a4b8a9d866f05b5477557  ...       2
4     6c67ac55360340258e157f3710ebae6c  ...       2
...                                ...  ...     ...
7340  0a8fbc25ea6a4241b9069919a8a88e1d  ...       2
7341  54ef19d3fb1e4b8b8415623892868275  ...       2
7342  0a9a42f8a78545f9b979fe5c7d33b33f  ...       2
7343  87aca93ec1074c37a5e1ff14f9cdb253  ...       2
7344  68680bb34bcf4829a04169885b4d92ff  ...       2

[7345 rows x 3 columns]
>>> data1
                                    id  ... content
0     7a3dd79f90ee419da87190cff60f7a86  ...       2
1     7640a5589bc7486ca199eeeb38af79dd  ...       1
2     8c5bda93e4ba401f90a0faa5b28fe57f  ...       2
3     1aa777fed31a4b8a9d866f05b5477557  ...       2
4     6c67ac55360340258e157f3710ebae6c  ...       2
...                                ...  ...     ...
7340  0a8fbc25ea6a4241b9069919a8a88e1d  ...       2
7341  54ef19d3fb1e4b8b8415623892868275  ...       2
7342  0a9a42f8a78545f9b979fe5c7d33b33f  ...       2
7343  87aca93ec1074c37a5e1ff14f9cdb253  ...       2
7344  68680bb34bcf4829a04169885b4d92ff  ...       2

[7345 rows x 3 columns]
>>> data1[2]
Traceback (most recent call last):
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2897, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 131, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1607, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1614, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 2

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    data1[2]
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 2995, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 2899, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 107, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 131, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1607, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1614, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 2
>>> data1.info
<bound method DataFrame.info of                                     id  ... content
0     7a3dd79f90ee419da87190cff60f7a86  ...       2
1     7640a5589bc7486ca199eeeb38af79dd  ...       1
2     8c5bda93e4ba401f90a0faa5b28fe57f  ...       2
3     1aa777fed31a4b8a9d866f05b5477557  ...       2
4     6c67ac55360340258e157f3710ebae6c  ...       2
...                                ...  ...     ...
7340  0a8fbc25ea6a4241b9069919a8a88e1d  ...       2
7341  54ef19d3fb1e4b8b8415623892868275  ...       2
7342  0a9a42f8a78545f9b979fe5c7d33b33f  ...       2
7343  87aca93ec1074c37a5e1ff14f9cdb253  ...       2
7344  68680bb34bcf4829a04169885b4d92ff  ...       2

[7345 rows x 3 columns]>
>>> train_title = data1.title
>>> train_label = data1.content
>>> train_title
0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!
2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?
3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水
4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!
                              ...                       
7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物
7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安
7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365
7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！
7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样
Name: title, Length: 7345, dtype: object
>>> def chinese_word_cut(mytext):
	    return " ".join(jieba.cut(mytext))

	
>>> data1['cut_title'] = data1.title.apply(chinese_word_cut)
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\YJ03CB~1.JIA\AppData\Local\Temp\jieba.cache
Loading model cost 0.825 seconds.
Prefix dict has been built succesfully.
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    data1['cut_title'] = data1.title.apply(chinese_word_cut)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\series.py", line 4045, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas/_libs/lib.pyx", line 2228, in pandas._libs.lib.map_infer
  File "<pyshell#61>", line 2, in chinese_word_cut
    return " ".join(jieba.cut(mytext))
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\__init__.py", line 282, in cut
    sentence = strdecode(sentence)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\_compat.py", line 37, in strdecode
    sentence = sentence.decode('utf-8')
AttributeError: 'float' object has no attribute 'decode'
>>> data1['cut_title'] = chinese_word_cut(data1.title)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    data1['cut_title'] = chinese_word_cut(data1.title)
  File "<pyshell#61>", line 2, in chinese_word_cut
    return " ".join(jieba.cut(mytext))
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\__init__.py", line 282, in cut
    sentence = strdecode(sentence)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\_compat.py", line 37, in strdecode
    sentence = sentence.decode('utf-8')
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'decode'
>>> def word_cut(text):
	return " ".join(jieba.cut(mytext))

>>> data1['cut_title'] = data1.title.apply(word_cut)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    data1['cut_title'] = data1.title.apply(word_cut)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\series.py", line 4045, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas/_libs/lib.pyx", line 2228, in pandas._libs.lib.map_infer
  File "<pyshell#66>", line 2, in word_cut
    return " ".join(jieba.cut(mytext))
NameError: name 'mytext' is not defined
>>> def word_cut(text):
	return " ".join(jieba.cut(text))

>>> data1['cut_title'] = data1.title.apply(word_cut)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    data1['cut_title'] = data1.title.apply(word_cut)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\series.py", line 4045, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas/_libs/lib.pyx", line 2228, in pandas._libs.lib.map_infer
  File "<pyshell#69>", line 2, in word_cut
    return " ".join(jieba.cut(text))
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\__init__.py", line 282, in cut
    sentence = strdecode(sentence)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\_compat.py", line 37, in strdecode
    sentence = sentence.decode('utf-8')
AttributeError: 'float' object has no attribute 'decode'
>>> cut = jieba.cut(data1.title)
>>> cut
<generator object Tokenizer.cut at 0x00000242C82E1F48>
>>> data1.title
0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!
2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?
3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水
4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!
                              ...                       
7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物
7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安
7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365
7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！
7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样
Name: title, Length: 7345, dtype: object
>>> cut1 = jieba.cut("问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)")
>>> cut1
<generator object Tokenizer.cut at 0x00000242C82E1DC8>
>>> print("【全模式】：" + "/ ".join(cut1))
【全模式】：问责/ 领导/ (/ 上/ 黄镇/ 党委书记/ 张涛/ ，/ 宣国/ 才/ 真能/ 一手遮天/ 吗/ ？/ )
>>> join(cut)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    join(cut)
NameError: name 'join' is not defined
>>> "/".join(cut)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    "/".join(cut)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\__init__.py", line 282, in cut
    sentence = strdecode(sentence)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\_compat.py", line 37, in strdecode
    sentence = sentence.decode('utf-8')
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'decode'
>>> print("/".join(cut))

>>> print("/".join(cut1))

>>> print("" +"/".join(cut1))

>>> cut1 = jieba.cut("问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)")
>>> print("" +"/".join(cut1))
问责/领导/(/上/黄镇/党委书记/张涛/，/宣国/才/真能/一手遮天/吗/？/)
>>> print("/".join(cut1))

>>> cut1 = jieba.cut("问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)")
>>> print("/".join(cut1))
问责/领导/(/上/黄镇/党委书记/张涛/，/宣国/才/真能/一手遮天/吗/？/)
>>> data1['cut_title'] = " ".join(jieba.cut(data1.title))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    data1['cut_title'] = " ".join(jieba.cut(data1.title))
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\__init__.py", line 282, in cut
    sentence = strdecode(sentence)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\_compat.py", line 37, in strdecode
    sentence = sentence.decode('utf-8')
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'decode'
>>> dta1.title.astype(str)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    dta1.title.astype(str)
NameError: name 'dta1' is not defined
>>> data1.title
0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!
2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?
3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水
4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!
                              ...                       
7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物
7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安
7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365
7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！
7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样
Name: title, Length: 7345, dtype: object
>>> data1.title.astype(str)
0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!
2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?
3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水
4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!
                              ...                       
7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物
7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安
7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365
7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！
7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样
Name: title, Length: 7345, dtype: object
>>> data1['cut_title'] = " ".join(jieba.cut(data1.title))
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    data1['cut_title'] = " ".join(jieba.cut(data1.title))
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\__init__.py", line 282, in cut
    sentence = strdecode(sentence)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\jieba\_compat.py", line 37, in strdecode
    sentence = sentence.decode('utf-8')
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'decode'
>>> data1.title = data1.title.str.decode('utf8')
>>> data1.title
0      NaN
1      NaN
2      NaN
3      NaN
4      NaN
        ..
7340   NaN
7341   NaN
7342   NaN
7343   NaN
7344   NaN
Name: title, Length: 7345, dtype: float64
>>> data =pd.read_csv('Train_DataSet.csv')
>>> data1.title = data.title
>>> data1.title
0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!
2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?
3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水
4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!
                              ...                       
7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物
7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安
7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365
7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！
7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样
Name: title, Length: 7345, dtype: object
>>> data1.title = data1.title.str.decode('utf8')
>>> data1.title
0      NaN
1      NaN
2      NaN
3      NaN
4      NaN
        ..
7340   NaN
7341   NaN
7342   NaN
7343   NaN
7344   NaN
Name: title, Length: 7345, dtype: float64
>>> data1.title = data.title
>>> import ast
>>> data1.title = data1.title.apply(ast.literal_eval).str.decode("utf-8")
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    data1.title = data1.title.apply(ast.literal_eval).str.decode("utf-8")
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\series.py", line 4045, in apply
    mapped = lib.map_infer(values, f, convert=convert_dtype)
  File "pandas/_libs/lib.pyx", line 2228, in pandas._libs.lib.map_infer
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\ast.py", line 46, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
                             ^
SyntaxError: invalid character in identifier
>>> data1.title
0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)
1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!
2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?
3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水
4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!
                              ...                       
7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物
7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安
7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365
7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！
7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样
Name: title, Length: 7345, dtype: object
>>> title1 = str(data1.title)
>>> title1
'0                            问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)\n1                               江歌事件:教会孩子，善良的同时更要懂得保护自己!\n2                             绝味鸭脖广告"开黄腔"引众怒 "双11"这么拼值吗?\n3                        央视曝光!如东一医药企业将槽罐车改成垃圾车，夜间偷排高浓度废水\n4       恶劣至极，央视都曝光了!南通如东一医药企业将槽罐车改成洒水车，夜间偷排高浓度废水...丢大发了!\n                              ...                       \n7340                              珊瑚裸尾鼠：首个因全球气候变暖灭绝的哺乳动物\n7341                             独居老人做饭忘关火 南通志愿者及时发现转危为安\n7342                被生意上的人给利用合同诈骗，诈骗三十万够判多少年--在..._律师365\n7343                              奎山汽贸城去年那场火灾，调查情况报告出来了！\n7344                        曝光台•调查｜市场消防通道被长期霸占？事情并非想象的那样\nName: title, Length: 7345, dtype: object'
>>> for title in data1.title
SyntaxError: invalid syntax
>>> for title in data1.title:
	data1.title = " ".join(jieba.cut(data1.title[title]))

Traceback (most recent call last):
  File "<pyshell#108>", line 2, in <module>
    data1.title = " ".join(jieba.cut(data1.title[title]))
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\series.py", line 1071, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Users\yj.jiang\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 4730, in get_value
    return self._engine.get_value(s, k, tz=getattr(series.dtype, "tz", None))
  File "pandas/_libs/index.pyx", line 80, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 88, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 128, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 91, in pandas._libs.index.Int64Engine._check_type
KeyError: '问责领导(上黄镇党委书记张涛，宣国才真能一手遮天吗？)'
>>> for title in data1.title:
	data1.title = " ".join(jieba.cut(title))

	
Traceback (most recent call last):
  File "<pyshell#110>", line 2, in <module>
    data1.title = " ".join(jieba.cut(title))
MemoryError
>>> 
