
'''
RC4 encryption algorithm
'''

import argparse


def rc4_encrypt(pt,key):
    l = len(pt)
    keystream = generate_keystream(key,l)
    cipher =''
    for i in range(l):
       cipher= cipher + (chr( ord(pt[i])^ord(keystream[i])))
    return cipher
def rc4_decrypt(cipher,key):
    l = len(cipher)
    keystream = generate_keystream(key,l)
    pt =''
    for i in range(l):
       pt= pt + (chr( ord(cipher[i])^ord(keystream[i])))
    return pt
    
    
def generate_keystream(key,l):
    S=[]
    T=[]
    keystream = []
    key = list(key)
    for i in range(256):
        S.append(i)
        T.append(ord(key[i%len(key)]))
    j = 0
    for i in range(256):
        j = (j + S[i]+T[i])%256
        S[i],S[j] = S[j],S[i]
    i=0
    j=0
    for r in range(l): 
        i = (i + 1)%256
        j = (j + S[i])%256
        S[i],S[j] = S[j],S[i]
        t = (S[i] + S[j])%256
        keystream.append(S[t])
    kk = '' 
    for c in keystream:
       kk =  kk+chr(c)
    return kk

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="rc4 encryption algrithm")

    parser.add_argument('key',action = 'store',type = str, help='specify the rc4 key')
    parser.add_argument('-e',action = 'store_true',help = 'encode')
    parser.add_argument('-d',action = 'store_true',help = 'decode')
    parser.add_argument('string',action = 'store', help = 'plaintext/cipher you want to encrypt/decrypt')

    args = parser.parse_args()


    if args.e:
        print("Encrpytion result:")
        print(rc4_encrypt(args.string,args.key))
    elif args.d:
        print("Decryption result:")
        print(rc4_decrypt(args.string,args.key))

    
