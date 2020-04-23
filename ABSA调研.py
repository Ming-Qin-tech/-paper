aspect based sentiment analysis 调研

-----------------------------------------------------------------------------------------------------------------------------------------
英文数据集整理：
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
        -------------------------------------------------------------------------------------------------------------------------------------------------------
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

情感极性专用数据集：
    英文：
        glue/sst2 句子级(BERT及其变种)

        ACL-14
            introduction:
                aspect level dataset
                twitter review ,通过搜索一些人们对名人、公司、产品发布的评论，整理了3类数据，消极，中立和积极（-1，0，1）各占25%、50%、25%
                train data 6248条， test data 692条
            year： 2014
            size：
            format:
                raw格式
                例子：
                    the $T$ does n't seem to run hot and the fan rarely turns on .
                    i3 processor
                    1
                    the i3 processor does n't seem to run hot and the $T$ rarely turns on .
                    fan
                    1

        SemEval-2014  dataset
            introduction：
                aspect level dataset
                reviews
                Laptops trial data (updated on 17/12/13)
                Restaurants trial data (updated on 17/12/13)
                Laptops train data (released on 15/12/13)
                Restaurants train data (released on 15/12/13)
                Annotation Guidelines (released on 18/2/14)
                Train data (Laptops & Restaurants) V2.0 (released on 18/2/14)
                Baselines, Evaluation, and Validation (released on 18/2/14)
                Test data: Phase A (released on 24/3/14)
                Test data: Phase B (released on 27/3/14)
                情感分为-1、0、 1 三类
            year: 2009
            size: 
            format:
                seg格式
                例子：
                    The tech guy then said the $T$ does not do 1-to-1 exchange and I have to direct my concern to the `` sales '' team , which is the retail shop which I bought my netbook from .
                    service center
                    -

        polarity dataset v2.0：
            intriduction: 
                Cornell University dataset
                http://www.cs.cornell.edu/people/pabo/movie-review-data/
                movie review
            year:2004
            size: 3MB
            format:
                txt 
                1000 positive and 1000 negative

        
        -------------------------------------------------------------------



    中文：
    https://github.com/SophonPlus/ChineseNlpCorpus
        ChnSentiCorp
            introduction:
                sentence level
                ChnSentiCorp 是一个中文情感分析数据集，包含酒店、笔记本电脑和书籍的网购评论。7000 多条酒店评论数据，5000 多条正向评论，2000 多条负向评论。
                只有0/1两种标注，即正面和负面评价两种
            year:
            size:1.7 MiB
            format:
                tsv
                一句话一个标注（0/1）



        waimai
            introduction:
                document level
                某外卖平台的review,正向 4000 条，负向 约 8000 条
            year：
            size：0.8 MiB
            format：
                csv
                只有0/1两种标注，即正面和负面评价两种


        online_shopping_10_cats
            introduction:
                document level
                下载地址： 
                数据概览： 10 个类别（书籍、平板、手机、水果、洗发水、热水器、蒙牛、衣服、计算机、酒店），共 6 万多条评论数据，正、负向评论各约 3 万条
                推荐实验： 情感/观点/评论 倾向性分析
                数据来源： 各电商平台，具体不详
                原数据集： 中文情感分析语料、中文情感分析语料库，网上搜集，具体作者、来源不详
                加工处理：
                将 2 份语料整合成 1 份语料
                将原来零散的 excel, txt 文档，整合成 1 个 统一的 csv 文档
                去重
            year:
            size:4 MiB
            format:
                csv
                比上面两个数据集多了分类标签，如书籍、水果、手机等，共有3个标签。


        weibo_senti_100k

            introduction:
                document level
                数据概览： 10 万多条，带情感标注 新浪微博，正负向评论约各 5 万条
                推荐实验： 情感/观点/评论 倾向性分析
                数据来源： 新浪微博
                原数据集： 新浪微博，情感分析标记语料共12万条，网上搜集，具体作者、来源不详
                加工处理：
                将原来的 2 份文档，整合成 1 份 csv 文件
                编码统一为 UTF-8
                去重
            year:
            size:9.15 MiB
            format:
                csv
                两个标签：文本+分类（0/1）

        
        
        simplifyweibo_4_moods 
            introduction: 
                document level
                下载地址： 小众数据集，存百度网盘
                数据概览： 36 万多条，带情感标注 新浪微博，包含 4 种情感，其中喜悦约 20 万条，愤怒、厌恶、低落各约 5 万条
                推荐实验： 情感/观点/评论 倾向性分析
                数据来源： 新浪微博
                原数据集： 微博情感分析数据集，网上搜集，具体作者、来源不详
                加工处理：
                将原来的 4 份文档，整合成 1 份 csv 文件
                原始语料进行了分词处理，我们重新将其还原为未分词的语料
                编码统一为 UTF-8
                去重
            year:
            size: 6.9 MiB
            format:
                csv
                两个标签，其中int类有0，1，2，3四种取值，分别0: '喜悦', 1: '愤怒', 2: '厌恶', 3: '低落'

        
        dmsc_v2
            introduction：
                下载地址： 百度网盘  /NLP/SA
                数据概览： 28 部电影，超 70 万 用户，超 200 万条 评分/评论 数据
                推荐实验： 推荐系统、情感/观点/评论 倾向性分析
                数据来源：豆瓣电影
                原数据集： Douban Movie Short Comments Dataset V2
                加工处理：
                去重并整理成与 MovieLens 兼容的格式
                进行脱敏操作，以保护用户隐私
            
            year:
            size:276 MiB
            format:
                csv
                userId,movieId,rating,timestamp,comment,like
                0,0,3,1431446400, 连奥创都知道整容要去韩国。,2404
                1,0,2,1429804800, 非常失望，剧本完全敷衍了事，主线剧情没突破大家可以理解，可所有的人物都缺乏动机，正邪之间、妇联内部都没什么火花。团结-分裂-团结的三段式虽然老套但其实也可以利用积攒下来的形象魅力搞出意思，但剧本写得非常肤浅、平面。场面上调度混乱呆板，满屏的铁甲审美疲劳。只有笑点算得上差强人意。,1231
                2,0,2,1429977600, 2015年度最失望作品。以为面面俱到，实则画蛇添足；以为主题深刻，实则老调重弹；以为推陈出新，实则俗不可耐；以为场面很high，实则high劲不足。气！上一集的趣味全无，这集的笑点明显刻意到心虚。全片没有任何片段给我有紧张激动的时候，太弱了，跟奥创一样。,1052


        yf_dianping 
            sentence level，比较规范的数据集/*****/
            introduction:
                下载地址： 百度网盘
                数据概览： 24 万家餐馆，54 万用户，440 万条评论/评分数据
                推荐实验： 推荐系统、情感/观点/评论 倾向性分析
                数据来源： 大众点评
                原数据集： Dianping Review Dataset，Yongfeng Zhang 教授为 WWW 2013, SIGIR 2013, SIGIR 2014 会议论文而搜集的数据
                加工处理：
                只保留原数据集中的评论、评分等信息，去除其他无用信息
                整理成与 MovieLens 兼容的格式
                进行脱敏操作，以保护用户隐私
            
            year:
            size: 820MiB
            format:
                csv
                类别，从0-5
        

        yf_amazon：
            introduction:
                下载地址： 百度网盘
                数据概览： 52 万件商品，1100 多个类目，142 万用户，720 万条评论/评分数据
                推荐实验： 推荐系统、情感/观点/评论 倾向性分析
                数据来源： 亚马逊
                原数据集： JD.com E-Commerce Data，Yongfeng Zhang 教授为 WWW 2015 会议论文而搜集的数据
                加工处理：
                将全角字符转换为半角字符，并采用 UTF-8 编码
                整理成与 MovieLens 兼容的格式
                进行脱敏操作，以保护用户隐私
            year:
            size:1.75 GB 
            format:
                csv
                格式同上

中文NLP专用数据集：
    中文，但不是SA，文本分类：
    全网新闻数据(SogouCA)
        介绍：
            来自若干新闻站点2012年6月—7月期间国内，国际，体育，社会，娱乐等18个频道的新闻数据，提供URL和正文信息

        格式说明：
            数据格式为

            <doc>

            <url>页面URL</url>

            <docno>页面ID</docno>

            <contenttitle>页面标题</contenttitle>

            <content>页面内容</content>

            </doc>

            注意：content字段去除了HTML标签，保存的是新闻正文文本

        相关任务：
            文本分类

            事件检测跟踪

            新词发现

            命名实体识别

            自动摘要
    -----------------
    中文最全NLP文本库收集：
        介绍：
            中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取、邮箱抽取、中日文人名库、中文缩写库、拆字词典、词汇情感值、停用词、反动词表、暴恐词表、繁简体转换、英文模拟中文发音、汪峰歌词生成器、职业名称词库、同义词库、反义词库、否定词库、汽车品牌词库、汽车零件词库、连续英文切割、各种中文词向量、公司名字大全、古诗词库、IT词库、财经词库、成语词库、地名词库、历史名人词库、诗词词库、医学词库、饮食词库、法律词库、汽车词库、动物词库、中文聊天语料、中文谣言数据、百度中文问答数据集、句子相似度匹配算法集合、bert资源、文本生成&摘要相关工具、cocoNLP信息抽取工具、国内电话号码正则匹配、清华大学XLORE:中英文跨语言百科知识图谱、清华大学人工智能技术…
        https://github.com/fighting41love/funNLP


    大连理工大学情感词汇本体库
    https://github.com/ZaneMuir/DLUT-Emotionontology


        例子：
            词语, 词性种类, 词义数, 词义序号, 情感分类, 强度, 极性, 辅助情感分类, 强度, 极性, , , 
            脏乱, adj, 1.0, 1.0, NN, 7.0, 2.0, , , , , , 
            糟报, adj, 1.0, 1.0, NN, 5.0, 2.0, , , , , , 
            早衰, adj, 1.0, 1.0, NE, 5.0, 2.0, , , , , , 



    中文公司名 人名语料库
        https://github.com/wainshine/Company-Names-Corpus
        https://github.com/wainshine/Company-Names-Corpus

    100+ Chinese Word Vectors 上百种预训练中文词向量：
        https://github.com/Embedding/Chinese-Word-Vectors

    中文wiki语料：
        https://github.com/mattzheng/ChineseWiki

    THUOCL（THU Open Chinese Lexicon）中文词库
        https://github.com/thunlp/THUOCL

    chinese_popular_new_words
        https://github.com/1data-inc/chinese_popular_new_words

    中文常用停用词表（哈工大停用词表、百度停用词表等
        https://github.com/goto456/stopwords
        
        停用词：
            通常意义上，停用词大致分为两类。
                一类是人类语言中包含的功能词，这些功能词极其普遍，与其他词相比，功能词没有什么实际含义，比如'the'、'is'、'at'、'which'、'on'等
                另一类词包括词汇词，比如'want'等，这些词应用十分广泛，但是对这样的词搜索引擎无法保证能够给出真正相关的搜索结果，难以帮助缩小搜索范围，同时还会降低搜索的效率，所以通常会把这些词从问题中移去，从而提高搜索性能。

            在网页内容中适当地减少Stop Words出现的频率，可以有效地帮助我们提高关键词密度，而在网页Title中避免出现Stop Words往往能够让我们优化的关键词更突出。


    Keyword_Extraction
        https://github.com/bigzhao/Keyword_Extraction/tree/master/%E5%AD%97%E5%85%B8
        如  创造101的人名，美食的名字

------------------------------------------------------------------------------------------------------------------------------------------
企业界现状：

    JD AI评论观点抽取：https://neuhub.jd.com/ai/api/nlp/comment

    百度AI  评论观点抽取：https://ai.baidu.com/tech/nlp/comment_tag

    阿里云情感分析：https://ai.aliyun.com/nlp/sa?spm=5176.11907134.1249450.6.77c44705N9VL6e

    Google cloud api:https://cloud.google.com/natural-language/docs/sentiment-tutorial  https://cloud.google.com/natural-language/docs/sentiment-tutorial?hl=zh-cn

    AWS:https://docs.aws.amazon.com/comprehend/latest/dg/API_DetectSentiment.html

    brand24:https://brand24.com/ai-driven-sentiment-analysis/?adgr=txt-best-iii-sentiment_analysis_broad&keyword-ext=%2Bsentiment%20%2Banalysis&placement=&adgr=txt-best-iii-sentiment_analysis_broad&gclid=Cj0KCQjwj7v0BRDOARIsAGh37ipJMjsTsuIzul0jE2BugpUjzSnZlGxuLFYwHTNvVfSn-TR5nbldmmUaAkRPEALw_wcB
------------------------------------------------------------------------------------------------------------------------------------------

比赛：
    1.2019 搜狐校园算法大赛（ABSA）   有open code，但数据集找不到，据说质量不高
    2. 美团、创新工场  2019 AI Challenge  (同样是数据集难找)
------------------------------------------------------------------------------------------------------------------------------------------
section 大纲：
    section 1：Deep learning based model
        现在的主流方法

        填坑： self-attention、transformers、bert architecture

    section 2：特征工程
        缺点：人工设计低效成本高，遇到新的数据集可能要重新设计，复用性低
        and inefficient to design features manually. 
-----------------------------------------------------------------------------------------------------------------------------------------
内容调研：
    section 1:Deep learning（又可以分为 RNN baselint（LSTM） Non-RNN baseline）
        主要论文：（按发表顺序，survey和doc paper）
            1 Effective LSTMs for Target-Dependent Sentiment Classification（COLING2016）
            2 Attention-based LSTM for Aspect-level Sentiment Classification（EMNLP2016）
            3 Aspect Level Sentiment Classification with Deep Memory Network（EMNLP2016）
            4 Interactive Attention Networks for Aspect-Level Sentiment Classification（IJCAI2017）
            5 Learning to Attend via Word-Aspect Associative Fusion for Aspect-based Sentiment Analysis（AAAI2018）
            6 Targeted Aspect-Based Sentiment Analysis via Embedding Commonsense Knowledge into an Attentive LSTM（AAAI-18）
            7 Multi-grained Attention Network for Aspect-Level Sentiment Classification（2018） 
            8 Aspect Level Sentiment Classification with Attention-over-Attention Neural Networks (2018)
            9 Transformation Networks for Target-Oriented Sentiment Classification(2018)
            10 CAN---Constrained Attention Networks for Multi-Aspect Sentiment Analysis(2018)
            11 Attentional Encoder Network for Targeted Sentiment Classification(2019)
            12 Zeng Biqing, Yang Heng, et al. "LCF: A Local Context Focus Mechanism for Aspect-Based Sentiment Classification." 
            论文1：Effective LSTMs for Target-Dependent Sentiment Classification（COLING2016）
                创新思路：
                    在这篇论文里面作者主要是介绍了三种基于LSTM的模型，来解决 ABSA 任务：

                        LSTM
                        Target-Dependent LSTM 
                        Target-Connection LSTM 
                    LSTM：
                        跟普通的对文本情感分析的做法没有区别，最终得到的也是这个句子的全局情感，所以最后的效果一般。

                        具体做法就是对句子中的 token 进行 embedding 处理作为模型的输入，经过一次一次的计算隐层和输入之后得到一个句子表示 ，接着对这个向量进行 softmax 计算概率。
                    TD-LSTM（ Target-Dependent LSTM）：
                        解决上面 LSTM 忽略目标词的问题。
                            基本思想是对于一个 target-word，充分考虑其上下文信息，具体来说使用了两个 LSTM，从左往右的和从右往左的，分别对 target word 的左边和右边的信息建模。
                            两个LSTM得到的向量concat（或sum/average）一下----->softmax
                    TC-LSTM（Target-Connection LSTM）：
                        在 TD-LSTM 的基础上进一步加强了 target-word 与句子中每个 token 的关联。
                        见图1.2

                contribution（提升）：
                    TC-LSTM和SVM相比提高9%（Accuracy& F1）
                    accuracy: 0.715(最优)   Macro-F1: 0.695（仅次于Target-dep+）


            ---------------------------------------------------------------
            论文2：Attention-based LSTM for Aspect-level Sentiment Classification（EMNLP2016）
                创新思路：
                    
                    /？/However, those models can only take into consideration the target but not aspect information which is proved to be crucial for aspect-level classification.

                    作者这里提到了两个概念：target 和 aspect。我们可以认为 target 是包含在句子中出现的词，而 aspect 属于预先定义的比较 high-level 的类别刻画。基于以上，提出了两种模型：/？/
                        引入概念：
                            Aspect Embedding：对于 ABSA 问题，aspect 信息对于最终的情感判别是非常重要的。因此作者对每个 aspect 都学习一个相应的 aspect embedding 来表示。
                        引入模型：

                            Attention-based LSTM (AT-LSTM)
                            Attention-based LSTM with Aspect Embedding (ATAE-LSTM)
                    
                    AT-LSTM：
                        使用传统注意力机制，也就是 key-value-query 。（参考：理解 Attention 机制原理及模型: https://blog.csdn.net/Kaiyuan_sjtu/article/details/81806123）

                    ATAE-LSTM：
                        将 aspect embedding 与 word embedding 共同组合成模型的输入。（类似于TC-LSTM 对 TD-LSTM的改进）
                    


                contribution（提升）：
                    使用数据集：SemEval 2014 Task 4
                        /*/耍了滑头，没有和最厉害的TC-LSTM对比（应该没有TC提升多才如此吧），只和TD和普通LSTM做了对比，是有一些提升(AE-LSTM比TD提升1%，ATAE比TD提升2%)，
                
                        ------------------------------------------------------------
            论文3：Aspect Level Sentiment Classification with Deep Memory Network（EMNLP2016）
                创新思路：
                    文章借鉴了来自QA领域的记忆网络解决ABSA问题。Memory Network提出的目的之一就是为了解决RNN、LSTM等网络的记忆能力较差的问题。它维护了一个外部的记忆单元用于存储之前的信息，而不是通过cell内部的hidden state。
                contribution（提升）：
            ------------------------------------------------------------
            论文4：Interactive Attention Networks for Aspect-Level Sentiment Classification（IJCAI2017）
                创新思路：
                    也是将target和context进行交互获取句子的准确表达，利用的模型是attention。与上面几个模型不同的在于，这里考虑了target可能存在好几个word组成的短语，另外添加了一层对于target的attention操作用于计算权重。提出了Interactive Attention Networks(IAN)。

                    计算attention权重得分
                contribution（提升）：
                    state-of-art：
                        比ATAE-LSTM  ：restaurant（78.6%：提升1%）   laptop(72.1%：提升4%)
                        
                        
                        虽没对比，可能没有论文5结果好
            ---------------------------------------------------------------------------------------------------------------------------------
            论文5：Learning to Attend via Word-Aspect Associative Fusion for Aspect-based Sentiment Analysis（AAAI2018）
                创新思路：
                    对于上一节的 ATAE-LSTM，作者认为仍然存在以下不足：

                    不是让注意力层专注于学习上下文词的相对重要性，而是给注意力层增加了对aspect和上下文词之间的关系进行建模的负担；
                    除了对顺序信息进行建模之外，LSTM的参数现在还承担了额外的负担，即，它还必须学习aspect和单词之间的关系。ATAE-LSTM中的LSTM层在一个由sapect embedding主导的序列上进行训练，这将大大增加模型的训练难度；
                    简单的拼接会使ATAE-LSTM中LSTM层的输入加倍，这会增加LSTM层参数成本， 影响内存占用量，计算复杂性和存在过拟合风险。

                    提出模型：
                        Aspect Fusion LSTM (AF-LSTM）
                    
                    AF-LSTM：
                        在输入经过 embedding 层和 LSTM 层之后进入到 Word-Aspect Fusion Attention Layer，这也是该模型的重点。

                        「Normalization Layer（optional）：」 在隐状态矩阵和 aspect vector 进行交互之前可以选择性地对其进行正规化操作，可以选用 Batch Normalization；

                        「Associative Memory Operators：」 用于计算 context word 和 aspect word 之间的关系。有两种：circular correlation 和 circular convolution
                contribution（提升）：
                    数据集：SemEval 2014 Task 4
                    比ATAE-LSTM取得了巨大的进步，每项提升4%-8%左右

            ------------------------------------------------------------
            论文6：Targeted Aspect-Based Sentiment Analysis via Embedding Commonsense Knowledge into an Attentive LSTM（AAAI-18）
                创新思路：
                    作者在对先前论文review之后给出了几个仍未解决的问题：

                        target包含多个实体或单词时，现有的研究都是认为各部分重要性一致并且简单地计算平均值作为向量表示；
                        使用hierarchical attention建模得到的target和情感词之间的关联是一个黑箱；
                        未引入包含更多信息的外部知识
                        全局的attention会编码与任务不相关的信息

                    文章给出了三个解决方案：

                        创建多层attention模型来分别明确计算目标词（target）和整个句子；
                        将外部知识引入传统LSTM网络；
                        将常识性情感知识融入深层神经网络。

                    整体框架如/*/图4.1，主要包括两个组分：「sequence encoder」和「hierarchical attention」


                    「Commonsense Knowledge：SenticNet」
                        引入外部知识库SenticNet，含有50000个实例，每个实例对应一系列情感属性。情感属性提供了每个实例的表示，也将各个aspect与其情感链接起来。
                contribution（提升）：
            -------------------------------------------------------------   
            论文7：Multi-grained Attention Network for Aspect-Level Sentiment Classification
                创新思路：
                    使用的attention mechanism都是属于粗粒度的（简单地求和操作），如果对于target word和context都很长的话会引入额外的损失；
                    另外，先前的工作都是将aspect和context视作是单独的instance进行训练，没有考虑到具有相同上下文的instance之间的关联，而这些关联很有可能会带有额外的信息。

                    提出model：
                        多粒度注意力网络（Multi-grained Attention Network， MGAN）

                        改进：
                            「细粒度注意力机制（fine-grained attention mechanism）：」 单词级别（word-level）的target和context之间的交互，可以减少粗粒度attention的损失；
                            「多粒度注意力机制 （multi-grained attention network）：」 粗粒度attention和细粒度attention结合；
                            「aspect alignment loss：」 在目标函数中加入aspect alignment loss，以增强context相同而情感极性不同的aspect对context权重学习的差异性。

                            loss function 重新设计

                contribution（提升）：
                    和paper5的IAN比提升3%左右
            ---------------------------------------------------------------
                    
            论文8：Aspect Level Sentiment Classification with Attention-over-Attention Neural Networks（AOA-LSTM）
                创新思路：
                    这篇文章的思路好像跟上一篇很像，模型可以分为四个部分：

                        word embedding
                        Bi-LSTM
                        Attention-over-Attention
                        Final Classification

                    提出概念：
                        Attention-over-Attention（AOA）
                contribution（提升）：
                    没有paper6的提升大


            ------------------------------------------------------------
           论文9：Transformation Networks for Target-Oriented Sentiment Classification
                创新思路：
                    改进Attention：
                        作者提出用attention去提取context和aspect之间的语义相关性存在一定的缺陷

                        例子：
                            “This dish is my favorite and I always get it and never get tired of it.” 这句话中，attention机制会提取出相对于dish不相关的词语比如"never","tired"等。

                        于是提出可以利用CNN来取代attention来提取context中相对重要的信息，同时对朴素CNN进行了进一步的处理使其适合该任务

                        提出model： Target-Specific Transformation Networks (TNet)
                contribution（提升）：
                    相比于IAN有所提升，但和论文11（AEN）相比差很多
            ------------------------------------------------------------
            论文10：CAN---Constrained Attention Networks for Multi-Aspect Sentiment Analysis(2018)
                创新思路：
                    引入orthogonal regularization，使得对于不同的aspect，attention weight聚焦在句子不同的部分；
                    引入sparse regularization ，使得每个aspect的attention weight只关注句子中的几个单词；
                    不同于之前大多数研究一次只得出一个aspect的sentiment，本文可以同时得到句子中所有aspect的sentiment；
                    引入multi-task多任务学习，在学习aspect level sentiment classification(ALSC)的同时学习aspect category detection (ACD)任务
                contribution（提升）：
            ----------------------------------------------------------------------------------------------------------------
            论文11：Attentional Encoder Network for Targeted Sentiment Classification  /*/ BERT
                创新思路：
                    提出model1：
                        提出了注意力编码网络（Attentional Encoder Network，AEN）
                    思路：
                        避免了RNN系模型的缺点（难以并行化，需要大量数据/内存/计算）；
                        同时提到先前的工作大都忽略了标签不可信问题（label unreliability issue），这里在损失函数中引入了标签平滑正则项。

                        作者开源了论文对应的代码库：songyouwei/ABSA-PyTorch 而且里面还有很多其他模型的实现。
                contribution（提升）：
                    其中，基于BERT的取得了最好成绩 比IAN 提升6%！
            -------------------------------------------------------------------------------------------------------------------------------------------
            论文12：Zeng Biqing, Yang Heng, et al. "LCF: A Local Context Focus Mechanism for Aspect-Based Sentiment Classification." Applied Sciences. 2019, 9, 3389.
                传统的机器学习方法都是特征工程方法
                创新思路：
                        previous works fail to notice the correlation between the aspect’s sentiment polarity and the local context. 
                        Multi-head Self-Attention (MHSA).
                        具体做法，将形容词和据它最近的名词短语联系在一起，由距离算法配对

                contribution（提升）：
                    state-of-art： Laptop（accuracy:78 --->82.3\F1:75---->79）、    restaurant(accuracy:84---->87%\F1: 78----->81%)、    twitter(ac)
                    三者都最优
                数据集：
                    the laptop and restaurant datasets of SemEval-2014 and the ACL twitter dataset均达到最优





            
    section 2： ML

    section 2.1:CRF
            论文1：Supervised Aspect Category Detection of Co-occurrence Data using Conditional Random Fields
                创新思路：
                contribution（提升）：
                    micro-F1:88%（目前为止见过的最高）
                缺点：
                    无法处理非结构化数据，所以要对输入的文本进行处理，在进行下一步，所以计算的复杂度很高。

        开源的libraries：
            HCRF、CRFall、CRF++

    section 2.2:SVM
        主要论文：（按发表顺序，survey和doc paper）
            1Implicit feature identification in Chinese reviews using explicit topic mining model

        
            论文1：Implicit feature identification in Chinese reviews using explicit topic mining model（2015）
                中文评论的分析
                使用自己标注的数据集，结合LDA，重点改进implicit aspect 的分析
                我们计算了我们抓取的中文评论，发现至少30％的句子是隐性的句子。
                主题建模方法（使用LDA+先验知识）可以被认为是聚类的聚类算法术语分为同类主题（或类），以及预先存在的知识可以指导聚类算法产生更好的更有意义的集群。
                LDA为什么要加先验知识？
                    产品功能经常与好，坏等常见词同时出现，仅举几例用于描述产品功能。 因此，使用时基本的LDA将显式语句聚类，一些乘积功能可能聚集在错误的主题中。
                创新思路：
                
                    首次关注了隐式属性，
                contribution（提升）：
                    比baseline提高了十五个点左右，但是由于是特征设计，难以推广

    section 2.3:最大熵

        论文1：UWB: Machine Learning Approach to Aspect-Based Sentiment Analysis（2014）
            数据集：Semeval 2014
            F1：  79%

综上所述，现如今ABSA类型的问题主流的方法已经是基于深度学习的，特别是基于BERT和LSTM的居多，所以我打算通过研究以下开源code入手，通过理清代码思路先实现一个目前效果最好的深度模型----->和主流AI公司的开源api效果对比

    另外，得知学术界新的进展一般首先出现在文本分类，然后进一步的应用到情感分析，所以之后定期关注一下文本分类的进展。


    




