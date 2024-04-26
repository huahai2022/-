# 解题思路
将数据集中的train.txt分别翻译为阿拉伯、土耳其、俄罗斯语，得到4*8k个数据，然后利用chatgpt数据得到4\*5k个数据，最后合并两个数据，经过多次实验，数据全部加在一起在验证集上得到了最高的评分F~score~=0.7288,其中最好的是英文达到了0.85，最差的是土耳其语0.60。训练模型是cardiffnlp/twitter-xlm-roberta-base-sentiment，学习率是1e-5，batch_size=64，打乱数据集，epochs=3。然后我加入验证集作为训练数据，和上面使用一样的配置。
# 注意
预测主脚本必须以"predict.sh"命名并放在项目的根目录下，我们最终将在项目根目录下执行"sh predict.sh {predict\_file} {predict\_result}"来获取预测结果。其中predict\_file为待预测文件，格式为每一行一条文本"{文本}"，predict\_result为预测结果文件，格式必须为"{标签}|{文本}"。两个文件的需逐行对应，不得打乱顺序。

1. 需要下载transformers库
2. 压缩包中含有bm和tokenizer两个文件夹，解压缩之后确保两个文件夹在与predict.py的同级目录，以便predict.py能加载两个模型文件。

