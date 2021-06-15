## FMS RC4 攻击实验

### 威胁模型：
1. 攻击者能截获所有的 WEP 报文，报文中包含密文和初始向量 IV
2. 攻击者已知每段密文对应的明文的第一个字节

### 攻击流程模拟：
1. 随机产生明文
2. 用rc4和wep密钥加密明文
3. 攻击者截获足够多的密文与并得知密文对应的明文的第一个字节，利用 FMS 攻击还原出 WEP 密钥。

### 实验设定：
1. IV 长度为 3 个比特，WEP 加密时随机产生
2. 标准 WEP 密钥长度为 40 比特和 104 比特，本实验中 WEP 密钥长度可以任意设置
3. RC4 密钥为"IV|WEP_key"形式，即初始向量在 WEP 密钥前，两者拼接共同组成 RC4 密钥 4) 实验中的明文随机产生

### 文件说明
+ RC4.py RC4加密/解密 ，使用方法：RC4.py [-h] [-e] [-d] key string
+ RC4_attack.py 单次攻击模拟，使用方法：RC4_attack.py [-h] [-k KEY] [-m MESSAGE_VOLUME]

```sh
示例：python RC4_attack.py -k password! -m 300
```
+ run.py 多次重复攻击模拟,输出成功率以及成功率与报文量的折线图，使用方法：run.py [-h] [-t Times]
```sh
python run.py -t 100
```
