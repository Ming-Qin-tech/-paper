
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





-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    GLUE 大系列（The General Language Understanding Evaluation (GLUE) ,tensorflow中有集成）：
        有句子和句子对的数据集和任务
        有现在的算法能达到的最好水平的显示

        GLUE/cola(The Corpus of Linguistic Acceptability)
            标记的是否有语法错误
            Corpus Sample
                c-05	0	*	Books were sent to each other by the students.
                swb04	1		She voted for herself.
            第一列：encode representation
            第二列： 人工标注错误
            第三列： 原作者标注错误
            第四列： 这句话

        GLUE/sst2(The Stanford Sentiment Treebank )7.09 MiB  由几个TXT文件组成
        train: 67,349   test:1821     validation:872 
            电影评论，句子级的情感极性，利用了PTB数据集，
                如
                    phrase ids|sentiment values
                        0|0.5
                        1|0.5
                        2|0.44444
                        3|0.5
                        4|0.42708
            Penn treebank（PTB数据集）词性标注集
                为每个单词标上词性
                    过去每句话的成分都是由专家标注，然后形成production rule（见下文解释）,速度慢成本高
                    现在有了人们精心建立的treebank，计算机就可以通过算法直接从treebank中抽取出production rule.

                treebank的问题：
                    最大的一个问题是 too big to fail。因为建立这些 treebank 很费时费力费钱，所以它们不能轻易的被替代；另外，尽管大多数的决定是由专家来做的，然而大多数的 coding 确是由非专家来完成的，而这些人也处于高压以及有限预算下，treebank 并不是尽善尽美的。

                    产生式和蕴含式：
                        产生式（production rule）:
                            例子：
                                IF 动物有犬齿 AND 有爪 AND 眼盯前方
                                    THEN 该动物是食肉动物
                                其中，r6是该产生式的编号；“动物有犬齿 AND 有爪 AND 眼盯前方”是产生式的前提P；“该动物是食肉动物”是产生式的结论Q。

                        蕴含式（implication / entailment）  
                            例子：
                                设p、q为两个命题。复合命题"如果p，则q"称为p与q的蕴含式，记作p→q。并称p为蕴含式的前件，q为后件。并规定p→q为假当且仅当p为真q为假。
                        总结：
                            (1) 蕴涵式表示的知识只能是精确的，产生式表示的知识可以是不确定的原因是蕴涵式是一个逻辑表达式，其逻辑值只有真和假。
                            (2) 蕴含式的匹配一定要求是精确的，而产生式的匹配可以是不确定的
        

        gule/mrpc(The Microsoft Research Paraphrase Corpus)   语义
            introduction:
                从在线新闻中自动提取出来的句子对语料库，人工标注判断两句话在语义上是否等价
                比如来自一条新闻的一句话从A媒体登出和在B媒体等处可能语义上等价
            year:2005
            size:1.43 MiB
            format:
                train:3,668  test:1,725 validation 408
                txt格式

                例子：
                Quality	#1 ID	#2 ID	#1 String	#2 String
                1	702876	702977	Amrozi accused his brother, whom he called "the witness", of deliberately distorting his evidence.	Referring to him as only "the witness", Amrozi accused his brother of deliberately distorting his evidence.
                0	2108705	2108831	Yucaipa owned Dominick's before selling the chain to Safeway in 1998 for $2.5 billion.	Yucaipa bought Dominick's in 1995 for $693 million and sold it to Safeway for $1.8 billion in 1998.


        

        glue/qqp（The Quora Question Pairs2 dataset）   语义
            introduction:
                    同样是判断句子对语义等价性。
                    目的：查询“美国人口最多的州是什么？” 和“美国哪个州的人口最多？” 不应在Quora上单独存在，因为两者的意图是相同的。想要自动判断两个问题是否是同一个意思。
            year:
            size:57.73 MiB 
            format：
                tsv
                train: 363,849   test: 390,965   validation:40,430

                格式例子：
                id	qid1	qid2	question1	question2	is_duplicate
                404285	433578	379845	How many keywords are there in the Racket prog...	How many keywords are there in PERL Programmin...	0
                404286	18840	155606	Do you believe there is life after death?	Is it true that there is life after death?	1
            

        
        
        glue/stsb(The Semantic Textual Similarity Benchmark,语义文本相似性基准)       语义
            introduction： 
                语义文本相似性
            year:2017
            size:784.05 KiB
            format:
                csv
                train: 5,749   test: 1,379   validation:1500
                               train  dev test total 
                        -----------------------------
                        news     3299  500  500  4299
                        caption  2000  625  625  3250
                        forum     450  375  254  1079
                        -----------------------------
                        total    5749 1500 1379  8628
                
                例子：
                    main-captions	MSRvid	2012test	0001	5.000	A plane is taking off.	An air plane is taking off.
                    main-news	headlines	2014	0193	0	Former LAPD officer sought in Irvine slayings	Former CIA officer sentenced to 30 months in prison for info leak
        

        glue/mnli(The Multi-Genre Natural Language Inference Corpu,多类自然语言推理语料库)    推理/蕴含
        Inference/textual entailment：推理/文本蕴含
        introduction：
            多类：前提语句是从十种不同来源收集的，包括转录的语音，小说和政府报告。
            任务是预测前提是否包含假设（蕴含），与假设相矛盾（矛盾）或两者都不（中立）。
            introduction：
            year：2017
            size：298.29 MiB
            format：
                jsonl： json lines文件， json lines文件是一种便于存储结构化数据的格式，可以一次处理一条记录。可以用作日志文件或者其他。每条json数据之间存在一个"\n"分隔符。
            例子：
                sentence 1:
                    'in that other you know uh that i should do it or that or just to think about doing it rat her than having someone  tell him to do it i know that was a big thing in our house for a long time was that if i wanted my husband to do something to help'
                sentence 1_binary_parse:
                    ( ( ( ( in ( that other ) ) ( you ( know ( uh ( ( that i ) ( should ( do it ) ) ) ) ) ) ) or ) ( ( that ( or ( just ( to ( think ( about ( doing ( it ( ( rat her ) ( than ( having ( someone ( tell ( him ( to ( ( do it ) ( i ( know ( that ( was ( ( a ( big thing ) ) ( in ( ( our house ) ( for ( a ( long time ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ( was ( ( that if ) ( i ( wanted ( my ( husband ( to ( do ( ( something to ) help ) ) ) ) ) ) ) ) ) ) )
                sentence 1_parse:
                    (ROOT (SBAR (SBAR (WHPP (IN in) (WHNP (WDT that) (NP (JJ other)))) (S (NP (PRP you)) (VP (VBP know) (SBAR (S (INTJ (UH uh)) (NP (DT that) (FW i)) (VP (MD should) (VP (VB do) (NP (PRP it))))))))) (CC or) (SBAR (WHNP (WDT that)) (PRN (CC or) (ADJP (RB just) (S (VP (TO to) (VP (VB think) (PP (IN about) (S (VP (VBG doing) (S (NP (PRP it)) (VP (VB rat) (NP (PRP her)) (PP (IN than) (S (VP (VBG having) (S (NP (NN someone)) (VP (VB tell) (S (NP (PRP him)) (VP (TO to) (VP (VB do) (NP (PRP it)) (SBAR (S (NP (FW i)) (VP (VBP know) (SBAR (IN that) (S (VP (VBD was) (NP (NP (DT a) (JJ big) (NN thing)) (PP (IN in) (NP (NP (PRP$ our) (NN house)) (PP (IN for) (NP (DT a) (JJ long) (NN time)))))))))))))))))))))))))))))) (S (VP (VBD was) (SBAR (IN that) (IN if) (S (NP (FW i)) (VP (VBD wanted) (NP (PRP$ my) (NN husband) (S (VP (TO to) (VP (VB do) (NP (NN something) (TO to) (VB help))))))))))))))

       
        glue/qnli( The Stanford Question Answering Dataset ,斯坦福问答语料库)      阅读理解
            introduction:
                SQuAD 2.0： 斯坦福整理的Question & Answer 型数据集
                任务是确定上下文句子是否包含问题的答案。 （从Wikipedia提取）包含相应问题的答案（由注释者编写）。
            year:
            size: 10.14 MiB
            format:  
                Split	Examples
                'test'	5,463
                'train'	104,743
                'validation'	5,463

                json,具体结构整理见小本本。

        glue/rte(The Recognizing Textual Entailment (RTE) datasets)
            introduction：
                constructed based on news and Wikipedia text.


        glue/wnli（The Winograd Schema Challenge ）           阅读理解，主要目标是解决代词消解问题  市议员拒绝了示威者的许可证，因为他们[害怕/主张]暴力。他们指得谁？
            introduction:
                是一个winograd schema的阅读理解的任务。有代词消解问题
                /*/有中文的winograd 训练语料库

                Winograd模式
                    Winograd模式是一对句子，它们之间只有一个或两个词不同，并且包含歧义，这在两个句子中以相反的方式解决，并且需要使用知识及其推理来解决。
                    如： Terry Winograd的一个著名示例

                            市议员拒绝了示威者的许可证，因为他们[害怕/主张]暴力。
                            如果``害怕''一词，则``他们''大概是指市议会; 如果它是``主张''，那么``他们''大概是指示威者。
            year：2011
            size：28.32 KiB
            format：
                Split	Examples
                'test'	146
                'train'	635
                'validation'	71

        glue/ax：   推理/蕴含
            introduction：
                手动编制的评估数据集，用于对各种语言现象的系统性能进行细粒度分析。 该数据集通过自然语言推理（NLI）问题（文本蕴含）评估句子的理解能力。 使用在MulitNLI上训练的模型为该数据集生成预测。
            year：

            size： 217.05 KiB

            format：(tsv)

                Split	Examples
                'test'	1,104
                只有测试集
            例子：
            
                Lexical Semantics	Predicate-Argument Structure	Logic	Knowledge	Domain	Premise	Hypothesis	Label
                0	NaN	NaN	Negation	NaN	Artificial	The cat sat on the mat.	The cat did not sit on the mat.	contradiction
                1	NaN	NaN	Negation	NaN	Artificial	The cat did not sit on the mat.	The cat sat on the mat.	contradiction
                2	NaN	NaN	Negation	NaN	News	When you've got no snow, it's really hard to l...	When you've got snow, it's really hard to lear...	neutral
                1099	NaN	Active/Passive	NaN	NaN	Artificial	Tunics or shirts of some form or another are w...	People wear tunics or shirts of some form or a...	entailment
----------------------------------------------------------------------------------------------------------------------------------------------------------------
2020/04/20
        SWAG(Inference)   Common Sense 知识推理
            introduction:
                Situations with Adversarial Generations（SWAG）是一个由113k多项选择问题组成的数据集，这些问题涉及丰富的基础情境。
            year:2018
            size:113k个问题， 80 MiB左右
            format：csv

                例子1:
                ,video-id,fold-ind,startphrase,sent1,sent2,gold-source,ending0,ending1,ending2,ending3,label
                71400	lsmdc3028_GHOST_RIDER_SPIRIT_OF_VENGEANCE-12779	18689	Dropping his gun, a guard races away. Someone	Dropping his gun, a guard races away.	Someone	gen	opens fire with men.	 he flies  .   he was fired   he loves swimming.   0   			
                
                0号句子，即Someone	gen	opens fire with men.最符合上文文意。

        Event2Mind (Inference)/*/
            introduction:
                关于事件，意图和反应的常识推断,大型语料库，包含25,000个事件
                用一句话描述一个事件，分析这句话描述的两个人的情绪反应。
                作者提到一个应用：可以通过训练识别电影中的性别歧视行为。我认为可以用于AS我要研究的工作。/*/
            year: 2018
            size: 6.44 MiB
            format:csv

                例子：
                    PersonX puts PersonY in jail.

                    author's annotations:
                        PersonX's intent: ["none", "justice", "to display power"]

                        PersonX's reaction: ["vindicated", "great", "sad", "satisfied"]

                        Other people's reaction: ["sad", "angry", "guilty", "worried", "frustrated"]

                    Source,Event,Xintent,Xemotion,Otheremotion,Xsent,Osent
                    it_events,It starts to rainy,"[""none""]","[""none""]","[""upset""]",,3
                    it_events,It starts to rainy,"[""none""]","[""none""]","[""sad, gloomy""]",,1

                    Xsent， Osent表示情绪反应，从1到5表示从负面情绪到正面情绪。

        Amazon 商品评论（opinion mining ，SA）
            introduction：
                亚马逊各类商品的评论，数据量很多，GB级。
                year：update at 2018
                size: 100GB左右
                format：

                    例子：
                    reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B
                    asin - ID of the product, e.g. 0000013714
                    reviewerName - name of the reviewer
                    helpful - helpfulness rating of the review, e.g. 2/3
                    reviewText - text of the review
                    overall - rating of the product
                    summary - summary of the review
                    unixReviewTime - time of the review (unix time)
                    reviewTime - time of the review (raw)

                    {
                    "reviewerID": "A2SUAM1J3GNN3B",
                    "asin": "0000013714",
                    "reviewerName": "J. McDonald",
                    "helpful": [2, 3],
                    "reviewText": "I bought this for my husband who plays the piano.  He is having a wonderful time playing these old hymns.  The music  is at times hard to read because we think the book was published for singing from more than playing from.  Great purchase though!",
                    "overall": 5.0,
                    "summary": "Heavenly Highway Hymns",
                    "unixReviewTime": 1252800000,
                    "reviewTime": "09 13, 2009"
                    }






-----------------------------------------------------------------------
    基于https://github.com/niderhoff/nlp-datasets整理了英文数据集






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
    判别式模型
        判别式模型 discriminative model 计算条件概率，而生成式模型 generative model 计算联合概率分布。

    It has been observed that CRF-based learning method was more suitable for mining aspects, opinions and intensifiers (including phrases) in comparison to LHMMs based and statistical methods. 
