<数学之美>：
    模型不平滑：
        即有很多预测的条件概率为零
        
        如：
            汉字200000个，即便用全部互联网的资料去训练，依然有很多未曾出现的词，这就导致会有很多预测的概率为零。其实真实并不是零，这就是不平滑。
        
            对于没出现的事件，我不能认为它的概率就是零。如何解决样本的这个问题，进一步更好的训练呢？
                我们对不可信的统计数据打折扣，同时将折扣出来的那一小部分概率给予未出现但概率不可能为零的小概率事件。越是不可信折扣就越多。——（Good-Turing Estimate）
    
    分词：
        词的分节符（Delimit）
        
        一开始用于中间无空格的东亚文字，后来也应用到了英文的手写识别中（手写识别有的是连笔，必须分词）

        最早  梁南元——查字典，最长匹配  缺点：北京大学生--->  "北京大学" + "生"
        二、 王晓龙博士   最少次数的分词理论      ---->不能解决二义性问题    应"发展中国家"--->"发展"+"中"+"国家"   而非： "发展"+ "中国" + "家"
        三、郭进：统计语言模型   计算概率最大的分法（维特比算法（动态规划））   缺点：依赖大众的看法，在特定情况下是错的   优点：已经比人工标记准确了

        词的颗粒度划分：
            有两派语言学家：
                1. 清华大学  整体是一个词
                2.应该分为  "清华" 和 "大学" 两个词

            但各有好处，如：
                        在机器翻译中： "联想公司"视作一个词比较好
                        在搜索引擎中，视作两个词，否则，用户搜索"清华"搜不出清华大学
            
            所以综合一下:采用一个分词器同时支持不同层次的词的划分。"清华大学"既可以被视作一个整体又可以视作两个词。
                分词器：
                    1.基本词表：基本词比较稳定，分词方法已经解决，只要定期增加一些新词即可
                    2.复合词表

        中文分词以统计语言模型为基础，经过几十年的发展和完善，今天基本上可以看作一个已经解决的问题。吴军认为分词是一个已经解决的问题，提升的空间微乎其微。只要采用统计语言模型，效果都差不到哪里去。
        当然不同的人做的分词器有好有坏，这里面的差别主要在于数据的使用和工程实现的精度。


--------------------------------------------------
李永乐老师:youtube 傅里叶变换
变换： 向量到数字表换是一种最简单的变换
    标准正交基： 向量绝对值唯一，且互相垂直

傅里叶变换分为两种：

    傅里叶级数任何一个周期性的函数f（t）都可以变换成一系列正（余）弦函数（）的和。

    不同频率信号---> 振幅、相位、频率三个维度进行表示。

傅里叶变换：
    将信号（即便不是周期函数，也可以视作周期无穷大）里的正余弦函数摘出来，也可以把这些正余弦函数还原回原信号（变换）

    应用：
        1.声音的处理
            低频信号--->男生  高频信号---->女生 超低频信号---->噪音
            男声变女声  ----->傅里叶变换将低频转为高频再反变换回去。
            奥巴马的声音、本拉登的声音
        2.图像的处理
            人像：图片--->傅里叶变换---->低频（轮廓）  高频（细节（斑点）），处理完高频信号还原回去（磨皮美艳的原理）

想法：对新闻做傅里叶变换可不可能分开真相和情绪？
---------------------------------------------------------------------------

self-attention
    图：印象笔记：self-attention

    (张俊林博士：张俊林-深度学习中的注意力机制(2017版)https://blog.csdn.net/malefactor/article/details/78767781

    图1形象化展示了人类在看到一副图像时是如何高效分配有限的注意力资源的，其中红色区域表明视觉系统更关注的目标，很明显对于图1所示的场景，人们会把注意力更多投入到人的脸部，文本的标题以及文章首句等位置。

    Encoder-Decoder框架（seq2seq）
        /*/一般而言，文本处理和语音识别的Encoder部分通常采用RNN模型，图像处理的Encoder一般采用CNN模型。
        Encoder-Decoder框架是没有体现出“注意力模型”的，所以可以把它看作是注意力不集中的分心模型。

        大多数深度学习注意力模型附着在Encoder-Decoder框架下，当然，其实注意力模型可以看作一种通用的思想，本身并不依赖于特定框架，这点需要注意。

        图2是文本处理领域里常用的Encoder-Decoder框架最抽象的一种表示。

        Source和Target可以是同一种语言，也可以是两种不同的语言。而Source和Target分别由各自的单词序列构成：
            Encoder顾名思义就是对输入句子Source进行编码，将输入句子通过非线性变换转化为中间语义表示C：

            对于解码器Decoder来说，其任务是根据句子Source的中间语义表示C和之前已经生成的历史信息y1,y2......yi-1来生成i时刻要生成的单词yi：
        
        如果Source是一篇文章，Target是概括性的几句描述语句，那么这是文本摘要的Encoder-Decoder框架；如果Source是一句问句，Target是一句回答，那么这是问答系统或者对话机器人的Encoder-Decoder框架。

        Encoder-Decoder框架不仅仅在文本领域广泛使用，在语音识别、图像处理等领域也经常使用。比如对于语音识别来说，图2所示的框架完全适用，区别无非是Encoder部分的输入是语音流，输出是对应的文本信息；而对于“图像描述”任务来说，Encoder部分的输入是一副图片，Decoder的输出是能够描述图片语义内容的一句描述语。

Attention模型：
    soft attention：（最常见的attention模型）

        Encoder-Decoder框架是没有体现出“注意力模型”的，所以可以把它看作是注意力不集中的分心模型。

        为什么说encoder-decoder模型是“分心模型”呢？
            见图三
            其中f是Decoder的非线性变换函数。从这里可以看出，在生成目标句子的单词时，不论生成哪个单词，它们使用的输入句子Source的语义编码C都是一样的，没有任何区别。

            而语义编码C是由句子Source的每个单词经过Encoder 编码产生的，这意味着不论是生成哪个单词，y1,y2还是y3，其实句子Source中任意单词对生成某个目标单词yi来说影响力都是相同的，这是为何说这个模型没有体现出注意力的缘由。这类似于人类看到眼前的画面，但是眼中却没有注意焦点一样。

            图四
            理解Attention模型的关键就是这里，即由固定的中间语义表示C换成了根据当前输出单词来调整成加入注意力模型的变化的C1、C2、C3。增加了注意力模型的Encoder-Decoder框架理解起来如图3所示


            其中，f2函数代表Encoder对输入英文单词的某种变换函数，比如如果Encoder是用的RNN模型的话，这个f2函数的结果往往是某个时刻输入Xi后隐层节点的状态值；g代表Encoder根据单词的中间表示合成整个句子中间语义表示的变换函数，一般的做法中，g函数就是对构成元素加权求和，即下列公式：
            图五



-------------------------------------------------------------------
知识蒸馏：将复杂的model压缩为简单的model（小模型训练非常快），且精度几乎没损失
    1.训练好老师模型
    2.

    hard target：[0, 1, 0, 0, 1]

    soft target:[0.1, 0.2, 0.6, 0.5, 0]


    学生模型和老师模型结构一摸一样，如果多个老师分别会语文、数学，学生会更厉害，
        老师模型如果太差，相当于引入噪音
        如果老师和学生差异太小，学生就没办法学太多东西。(学生和老师达到不同的局部最优)

        如何衡量差异大小？
            老师模型时间离得近，差异小，离得远，参数差异大
            每个样本的老师信号都来自于不同的历史时刻，相当于像多个局部最优同时学习

    长周期老师是在某一个






---------------------------------------------------------------------------------------------------------------------------------------------------------------
李航NSR论文：深度学习NLP的现有优势与未来挑战
    NLP若划分为5个任务：分类、匹配（matching）、翻译、结构化预测（structured prediction:named entity recognition）、与序贯决策过程。深度学习在前四个的任务的精确度均已超过机器学习。
        classification（如sentiment classification, CNN:86%  SVM:79.4%  差6%）
        matching（question answering， CNN, p@1 ：49.6%， MLP p@1（多层感知机）：36.1%， 差13%）
        translation(NMT, BLEU:39.0, SMT,BLEU:37.0, 差2)
        structured prediction:(DL acc:91.8%, ML acc:90.7%, 差1%)

    深度学习的挑战： no good at indference and decision making 

    等，未完待续。。。。https://www.jiqizhixin.com/articles/2017-10-04-5


            


--------------------------------------------------------------------------
深度学习在情感分析中的应用的研究现状？  知乎
zhihu.com/question/33985819
    情感分析本质上是文本分类，很多最新的文本分类技术可以应用到SA。
        见回答：
            即便你找不到深度学习在SA上的论文，文本分类总是可以的哇。——非典型CS博士 东南大学 计算机科学博士在读

            看过不少先发在文本分类上的论文然后稍微改改发到顶会上的paper，如emnlp   ——不思蜀



--------------------------------------------------------------------------------------
---------------------------------------------------------------------------
准确率P、召回率R、F1 值：
    定义：
        准确率（Precision）：P=TP/(TP+FP)。通俗地讲，就是预测正确的正例数据占预测为正例数据的比例。
        召回率（Recall）：R=TP/(TP+FN)。通俗地讲，就是预测为正例的数据占实际为正例数据的比例
        F1值（F score） F1 = 2/（1/P + 1/R） = （2*P*R）/（P+R）
    
    F1值得意义：
        实际生产生活中，单纯的追求准确率和召回率都没有意义，只有二者皆不错才可能实际应用，这就是F1值得作用。    

ROC、AUC
    定义：
        TPR=TP/(TP+FN)=TP/actual positives
        FPR=FP/(FP+TN)=FP/actual negatives
        ROC是由点（TPR,FPR）组成的曲线，AUC就是ROC的面积。AUC越大越好。
        一般来说，如果ROC是光滑的，那么基本可以判断没有太大的overfitting



-------------------------------------------------------------------------------------------------------------------
http://sofasofa.io/forum_main_post.php?postid=1001112
F1 score是一个用来评价二元分类器的度量。先回顾一下它的计算公式：

F1=21recall+1precision=2recall×precisionrecall+precision



F1是针对二元分类的，那对于多元分类器，有没有类似F1 score的度量方法呢？有的，而且还不止一种，常用的有两种，这就是题主所问的两种，一种叫做macro-F1，另一种叫做micro-F1。



macro-F1(宏观)

假设对于一个多分类问题，有三个类，分别记为1、2、3，

TPi是指分类i的True Positive；

FPi是指分类i的False Positive；

TNi是指分类i的True Negative；

FNi是指分类i的False Negative。

接下来，我们分别计算每个类的精度(precision)

precisioni=TPiTPi+FPi

macro精度就是所有精度的均值

precisionma=precision1+precision2+precision33

类似地，我们分别计算每个类的召回(recall)

recalli=TPiTPi+FNi

macro召回就是所有召回的均值

recallma=recall1+recall2+recall33

最后macro-F1的计算公式为

F1,ma=2recallma×precisionmarecallma+precisionma



micro-F1

假设对于一个多分类问题，有三个类，分别记为1、2、3，

TPi是指分类i的True Positive；

FPi是指分类i的False Positive；

TNi是指分类i的True Negative；

FNi是指分类i的False Negative。

接下来，我们来算micro精度(precision)

precisionmi=TP1+TP2+TP3TP1+FP1+TP2+FP2+TP3+FP3

以及micro召回(recall)

recallmi=TP1+TP2+TP3TP1+FN1+TP2+FN2+TP3+FN3

最后micro-F1的计算公式为

F1,mi=2recallmi×precisionmirecallmi+precisionmi



如果这个数据集中各个类的分布不平衡的话，更建议使用mirco-F1，因为macro没有考虑到各个类别的样本大小。
------------------------------------------------------------------------------------------------------
任务一： 整理现在有哪些开源数据集，数据集大小、格式；
2020/3/30
    如何查看dataset的格式：https://blog.csdn.net/hulumei123/article/details/90490027
        推荐使用pycharm读取
            pycharm中使用python console， 
                import json
                source = json.load(json.path)
                
                使用pd.read_json()不会在special variables框中显示
                使用pd.read_csv()读取json文件会内存溢出报错，别问我是怎么知道的。。

    csv 和 json的区别：
        csv和json是Python里面常见的文本数据保存格式，

            1、csv文件可以用exel打开，里面的内容格式：数据之间是使用‘，’隔开。

            [,..........,]   用excel打开一个，就是隔着一列

            2、json数据格式是，保存一张列表，列表成员一般是字典，字典再去保存数值

            [{},{}...........]

    tsv和csv的区别
        TSV文件和CSV的文件的区别是：前者使用\t作为分隔符，后者使用,作为分隔符。
        使用pandas读取tsv文件的代码如下：
            train=pd.read_csv('test.tsv', sep='\t')
    
    jsonl： json lines文件， json lines文件是一种便于存储结构化数据的格式，可以一次处理一条记录。可以用作日志文件或者其他。每条json数据之间存在一个"\n"分隔符。
        读取jsonl，用json.load(),pycharm可以树形显示格式
            with open('./multinli_1.0/multinli_1.0/multinli_1.0_train.jsonl', 'r') as json_file:
                json_list = list(json_file)

            for json_str in json_list:
                result = json.loads(json_str)
                print("result: {}".format(result))
                print(isinstance(result, dict))

    train\dev(也叫validation set)\test集

        train集可以不和dev、test集同分布
        dev集一定要和test集同分布

        主要疑问是dev集为什么要从test集中分离出来？
            dev集的存在很好理解，要对用不同分布数据训练出来的模型做参数上的调整。
            那还要test集做什么？
                因为如果在dev集上过拟合了怎么办？那就可能dev集上表现很好，但是实际应用时可能差得远。——这就是test集的存在意义，检测dev集上是否过拟合。

    token 和 tokenization
        token(符号):包括单词和标点

        tokenization(分词,也叫做word segmentation)：我是中国人->['我', '是', '中国人']

    自然语言处理里的 IOB tagging 是什么意思？
        BIO/IOB tagging 是一种对给定句子中的单元做序列标注的方式，用于从给定句子中抽取连续字/词块构成的有意义短语，例如名词短语（noun phrases, NP）、命名实体（named entites, NE）等。对于一个给定句子，将其中每个词标注为B（Beginning，指示某短语起始）、I（Inside，指示短语内部）、O（Outside，指示不在短语中）中的一个。以命名实体识别（NER）为例可以将John supports Leceister City这句话里的四个词分别标注为：B-人名 O B-机构名 I-机构名。 类似变体还有BILOU等……


    constituent parsing & dependency parsing
        句法分析是对句子进行分析非常重要的部分，主要包括constituency parsing(成分句法分析)和dependency parsing(依存句法分析)，两者具有非常大的差异。
        
        成分分析（constituent parsing）
            成分分析树是将一个文本分成短语，树中的非叶子节点是短语的类型。
            如：
                            Sentence
                                    |
                    +-------------+------------+
                    |                          |
                Noun Phrase                Verb Phrase
                    |                          |
                    John                 +-------+--------+
                                        |                |
                                        Verb          Noun Phrase
                                        |                |
                                        sees              Bill

            有专门的句法树的构成规则，详见：https://www.ling.upenn.edu/~beatrice/annotation/syn-intro.htm#ordinary_ips
            例： 
                (ROOT (IP (PP (P 在) (NP (DNP (NP (NN 秋天)) (DEC 的)) (NP (NN 时候)))) (PU ，) (NP (NR 陶喆)) (VP (VV 爱) (IP (VP (VV 吃) (NP (NN 苹果)))))))
                图见：https://app.yinxiang.com/Home.action#n=189f1a0a-8a40-4860-9a52-fe5d35ad050d&s=s47&ses=4&sh=5&sds=2&
        
        依赖分析（dependency parsing）
            依存句法树能够根据成分句法树转换而来，但成分句法树不能通过依存树转化来。
                root(ROOT-0, 爱-7)
                case(时候-4, 在-1)
                nmod:assmod(时候-4, 秋天-2)
                dep(秋天-2, 的-3)
                nmod:prep(爱-7, 时候-4)
                punct(爱-7, ，-5)
                nsubj(爱-7, 陶喆-6)
                ccomp(爱-7, 吃-8)
                dobj(吃-8, 苹果-9)
                图：https://app.yinxiang.com/Home.action#n=189f1a0a-8a40-4860-9a52-fe5d35ad050d&s=s47&ses=4&sh=5&sds=2&x=jsonl&
        
        Head word
            一个长短语的head word表示最能表示整个短语的那个词，名词短语一般是名词，动词短语一般是动词。
                在”布朗访问上海“这一整棵树中head word就是“访问”这个词，而在右子树上head word是“访问”。
                图见：https://app.yinxiang.com/Home.action#n=189f1a0a-8a40-4860-9a52-fe5d35ad050d&s=s47&ses=4&sh=5&sds=2&




-------------------------------------------------------------------------------------------------------------------------------------------------
HMM（隐马尔科夫模型）   ------->   CRF(条件随即场)

HMM
    随即过程和随机变量
        随机过程，如股票的走势，股票价格本身是个未知的，但是t+1时刻的价格和t时刻的价格有关系，这恰恰是人们感兴趣的。整个过程是随机的，但过程之中的相邻点却是相关的。  当然，随机过程的状态度量不一定是时间t，还可以是各种“path”。
        以往随机变量之间都是不相关的，这体现了进步。
        参考：https://www.zhihu.com/question/280948058

    独立性输出假设：
        
        P(o1,o2,o3,...|s1,s2,s3....)=P(o1|s1)*P(o2|s2)*P(o3|s3)...  从意义上理解它的定义了，公式上不好推


CRF 
    A CRF can be considered as a generalization of HMM or we can say that a HMM is a particular case of CRF where constant probabilities are used to model state transitions.
    判别式模型
        判别式模型 discriminative model 计算条件概率，
            给出x预测y
        而生成式模型 generative model 计算联合概率分布。
            给出P（x，y）和x，求使P（x， y）最大的y
    It has been observed that CRF-based learning method was more suitable for mining aspects, opinions and intensifiers (including phrases) in comparison to LHMMs based and statistical methods. 


    The task of assigning labels to a set of observation sequences arises in many fields, 

    在很多应用里，我们都希望能够预测相互关联的多个变量。如一个sports team的比赛表现和每位队员的健康状况有关，而队员的健康状况和team的比赛密度安排和行程劳顿程度有关。比赛结果还和士气有关，而士气又反过来影响健康状况。

    可以看出，多个变量彼此内部相关联。用CRF条件随机场来解决此类问题非常有效。
    有许多类似应用， 如抽取NLP句法，图片区域的划分，DNA链的划分。

    在这些应用中，我们希望根据观测到的特征矢量，来预测一些随机变量。

    1. graphical model
        graphical model是表示这种相互之间关系的一个自然的做法。graphical model 包括Bayesian 网络，神经网络，factor graphs，马尔科夫随机场等等。 
    
    2. 为什么只有有graphical model不够？  -----要删繁就简
        大多数NLP的应用都期望得到联合概率分布，也就是得到生成模型。
        A generative model is a model for randomly generating observable data based on given parameters. 
        生成模型虽然有种种好处，但是也有不少弊端，如输入数据的维度一般很大，并且特征之间有很复杂的依赖关系，所以根据这两者构建一个概率模型很难，即便真的构建出来也会很复杂，很可能过拟合。

        所以不如我们部分忽略这些依赖，CRF只考虑输入临近的数据？
            如用米饭在盘子上猜一个菜肴，我们很难猜，因为这样的例子太多了。如果告诉你他旁边有扬州面条，扬州烤鸭，扬州里脊，你可能就能猜出这是扬州炒饭了。这就是CRF的原理。至于桌子因这个菜下沉了几微米，空气流动因为这个菜收到了什么影响就不去管了。

            HMM就是忽略的太多了，只利用了米饭和盘子这一个相关信息，没有利用临近信息。
---------------------------------------------------------------------------
    CRF如何解决graphical models面临的问题？  （CRF也是一种graphical model）
        一种解决方法是直接将条件分布model出来，对于分类问题来说这就是所需的全部了。/？/
        CRF本质上是将classification和graphical modeling的优势结合在一起。将利用大量数据进行预测和利用compactly 多变量数据建模的优势结合起来。
        
        /？/从某种角度来说，生成模型和CRF的关系可以类比于朴素贝叶斯和逻辑回归分类。
        /？/其实多项式逻辑回归模型可以被看作最简单的一种CRF--只有一个输出变量。
        /*/ 填坑：朴素贝叶斯   逻辑回归

    
    所以究竟什么是CRF？
        用来分类和segmenting 结构数据，如序列，树和lattice。CRF尤其适合于对时序数据进行建模（因为时间依赖可以通过各种不同的方式表达），The underlying idea is that of defining a conditional probability distribution over label sequences given a particular observation sequence, rather than a joint distribution over both label and observation sequences. 

        CRF的主要优势是放宽独立假设（the variables don’t depend on each other and they don’t affect each other in any way）取得的。
    
    HMM vs CRF  /?/
        HMM is a generative model and it gives the output directly by modeling the transition matrix based on the training data. The results can be improved by providing more datapoints, but there is no direct control over the output labels. HMM learns the transition probabilities on its own based on the training data provided. Hence if we provide more datapoints, then we can improve the model to include wider variety. CRF is a discriminative model which outputs a confidence measure. This is really useful in most cases because we want to know how sure the model is about the label at that point. This confidence measure can be thresholded to suit various applications. The good thing about confidence measure is that the number of false alarms is low compared to HMM.

        The primary advantage of CRFs over HMMs is their conditional nature, resulting in the relaxation of the independence assumptions required by HMMs. Additionally, CRFs avoid the label bias problem, a weakness exhibited by Markov models based on directed graphical models.
        /*/ A CRF can be considered as a generalization of HMM or we can say that a HMM is a particular case of CRF where constant probabilities are used to model state transitions. CRFs outperform HMMs on a number of real-world sequence labeling tasks.

        /？/填坑：HMM的：labe   l bias problem（有向图的天生不足，无向图如CRF无此缺点）

        There are many libraries available out there like HCRF, CRFall, CRF++ etc, that have CRF functionalities nicely defined and implemented. You can check them out and see how they work out for your project.

    

---------------------------------------------------------------------------
https://towardsdatascience.com/implementing-a-linear-chain-conditional-random-field-crf-in-pytorch-16b0b9c4b4ea

code implement for CRF  
    Over the last few years, CRFs models were combined with LSTMs to get state-of-the-art results. In the NLP community this was considered a rule of thumb for sequence tagging: if you want more accuracy just stack a CRF on top of your LSTM layer and bang ⭐️! You can see some examples here or here.

    In a sequence classification problem, our final objective is to find the probability of a sequence of labels (y) given an input of sequence vectors (X). This is denoted as P(y | X).

    图1：https://app.yinxiang.com/Home.action#n=b36da91d-e2b6-44ae-9a65-ca2d96928dcb&s=s47&ses=4&sh=5&sds=2&x=crf&
    These are some intuitions of why we use exp:
        Underflow: When we multiply very small numbers, we get a smaller number which may suffer underflow.
        Non-negative outputs: All values are mapped between 0 and +inf.
        Monotonically increasing: It pushes high values up and low values down. This has a similar effect with an argmax operation. More here.

    Now we are going to add new learnable weights to model the chance of a label yk being followed by yk+1. By modelling this, we are creating a dependency between successive labels! Thus, the name linear-chain CRF! In order to do so, we multiply our previous probability by P(yk+1 | yk), for which we can use exponential properties to rewrite it as unary scores U(x, y) plus learnable transition scores T(y, y):
    图2：https://app.yinxiang.com/Home.action#n=b36da91d-e2b6-44ae-9a65-ca2d96928dcb&s=s47&ses=4&sh=5&sds=2&x=crf&


    图3：https://app.yinxiang.com/Home.action#n=b36da91d-e2b6-44ae-9a65-ca2d96928dcb&s=s47&ses=4&sh=5&sds=2&x=crf&
    Turns out it’s not trivial to compute Z(X) because we have too many nested loops 😖! It’s a sum over all possible combinations over the label set at each timestep. To be more precise, we have ℓ computations over the label set. This give us a time complexity of O(|y|^ℓ).
    
    Luckily, we can exploit the recurrent dependencies and use dynamic programming（动态规划） to compute it efficiently 😁! The algorithm that does this is called forward algorithm or backward algorithm — depending on the order that you iterate over the sequence.
--------------------------------------------------------------------------------------------------------------------------

显示特征explicit：“I love the touchscreen of my phone but the battery life is so short。

隐式特征implicit： “This camera is sleek and very affordable“


-----------------------------------------------------------------------------------------------------------------------




