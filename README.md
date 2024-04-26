我最近参加了腾讯安全竞赛的机器学习赛道，不难，可能属于入门级别的小竞赛，给的时间也很短暂。[游戏安全技术竞赛-腾讯游戏安全中心官网-腾讯游戏 (tencent.com)](https://gss.tencent.com/competition/2024/index.htm)



竞赛分为初赛和决赛两个部分，赛题大同小异

# 初赛

## **游戏跨语言恶意内容识别**

背景：在打游戏时，游戏文本内容审核系统会识别出游戏场景中不合规的文本，比如：色情低俗，侮辱谩骂等。在海外游戏中，文本的审核系统就面临着多语言的挑战，参赛者需要基于英语数据集开发一款跨语言恶意文本的识别模型。

评估：最终模型将在包含英语、葡语的测试集上进行评估效果，并取各语种的F_score值的平均值作为最终成绩的依据。采用每个语种测试集上的F_score值作为指标，如英语的指标为：
$$
F_{score_{en}}=(1+\beta^2)\frac{precision_{en}*recall_{en}}{\beta^2*precision_{en}+recall_{en}}
$$


最终的评估指标为各个语种的F_score值的平均：
$$
F_{score_{avg}}=\frac{F_{score_{en}}+F_{score_{pt}}}{2}
$$

## 数据集

1. 训练集以及相关的数据集：8k条带有标注的数据（英文）；2\*200k条无标注的数据（英语、葡语个200k）；2*5k条chatgpt标注数据（英语、葡语各5k）
2. 验证集：2*100条带标注的数据（英语、葡语各100）
3. 测试集：2*1k无标注数据（英语、葡语各1k），不对外提供。

## 思路

没有想到无标签数据的作用，所以没有使用无标签数据集，用了8k带有标注的数据何2*5k条chatgpt标注的数据进行的。选择的模型是cardiffnlp/twitter-xlm-roberta-base-sentiment，epoch=10，bs=64，lr=1e-5。

最后在验证集上得到的结果是73%。

完整训练+测试代码见：

[huahai2022/TX-safety-race-ML (github.com)](https://github.com/huahai2022/TX-safety-race-ML)

# 复赛

## 游戏跨语言恶意内容识别

和初赛内容基本一致，但是语言做了改变，是用来英语、阿拉伯语、土耳其语和俄罗斯语四种语言，数据集做了相应的变化。

## 数据集

1. 8K条带有标注的数据（英语），文件名：train.txt
2. 4*20k条无标注的数据，文件名：unlabel_text.txt
3. 4*5k条chatgpt标注数据，每个语种各5k，文件名为：labeled_text_by_chatgpt.txt。
4. 50k平行语料（以英语为元语言，通过chatgpt获取）：parallel_text_by_chatgpt.txt

## 思路

和初赛方式一样，我没有像怎么使用无标签数据集，所以unlabel_text.txt和parallel_text_by_chatgpt.txt我无法使用，后面就是用了4*5k个chatgpt的标注数据，以及是用了小牛翻译将8k个带有标注的数据分别翻译为了对应的语言，总有4\*13k个数据。

选择的模型是cardiffnlp/twitter-xlm-roberta-base-sentiment，epoch=3，bs=64，lr=1e-5，在这种情况下获得了最高的验证机准确率，为72%

完整训练+测试代码见：

[huahai2022/TX-safety-race-ML (github.com)](https://github.com/huahai2022/TX-safety-race-ML)

# 总结

最后没有进入前6名，意料之中，总的来说，用时不是很长，是一次不错的竞赛体验，准确率不高的一个原因便是没有使用无标签数据集，没想起来怎么用。
