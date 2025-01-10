# 概要
Q学習を用いて，ロボット(赤い点)が数値線上を動くプログラムです．以下の図はイメージです．  
数値線上の範囲は-10〜10で，右端(10)に達した時の報酬は10です．
  
  
![Screenshot_2025-01-10-14-42-49-264_com google android apps docs-edit](https://github.com/user-attachments/assets/4087b09b-3363-4aac-8fdf-55aac404ff51)


#  パラメータ

| パラメータ | 値 |
|:----:|:----:| 
| 学習率 | 0.1 |
| ε(グリーディ方策) | 0.1 |
| 割引率 | 1.0 |
| エピソード | 100 |


# 出力例

https://github.com/user-attachments/assets/69e3c5ee-2bd9-4570-a172-86c412bffb6c

# 注意事項
もし実行時に“x must be a sequence”と表示されたら，コードの頭に  
```
pip install -U matplotlib==3.8.4
```
と入力してください．
