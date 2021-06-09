
import random
import sys
import argparse 

parser = argparse.ArgumentParser(description="RC4 attack script")

parser.add_argument('-k',action='store',type=str,help='wep key, if no input, it will be set as passw0rd',default='passw0rd')
parser.add_argument('-m',action="store",type=int,help='message volume used to recover the wep key',default=300)

args = parser.parse_args()

wep_key = args.k.encode('ascii')
print('WEP PSK is %s '%wep_key)
len_rc4key = len(args.k)+3
message_volume = args.m
print("Message volume is %d"%args.m)
print("RC4 attacking...")

keys = []

def random_str(slen=10):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

def generate_rc4key(k):
    v = random.randint(0,255)
    iv = (k,255,v)
    rc4key =  bytearray()
    rc4key.append(iv[0])
    rc4key.append(iv[1])
    rc4key.append(iv[2])
    rc4key.extend(wep_key)
    return (v,rc4key)

def rc4_encode(plaintext,rc4key):
    S=[]
    T=[]
    keystream = []
    ciphers = []
    plaintext = list(plaintext)
    for i in range(256):
        S.append(i)
        T.append(rc4key[i%len(rc4key)])

    j = 0
    for i in range(256):
        j = (j + S[i]+T[i])%256
        S[i],S[j] = S[j],S[i]
    i=0
    j=0
    for r in range(len(plaintext)): 
        i = (i + 1)%256
        j = (j + S[i])%256
        S[i],S[j] = S[j],S[i]
        t = (S[i] + S[j])%256
        keystream.append(S[t])
    for r in range(len(plaintext)):
        cipher = plaintext[r] ^ keystream[r]
        ciphers.append(cipher)
    return bytes(ciphers)


def run(k,true_keystream,rc4key,key_k_dict):
    S=[]
    T=[]
    keystream = []
    ciphers = []
    for i in range(256):
        S.append(i)
        T.append(rc4key[i%len(rc4key)])

    j = 0
    for i in range(k):
        j = (j + S[i]+T[i])%256
        S[i],S[j] = S[j],S[i]
    i=0
    ### TODO:
    if (S[0]+S[1] == k):
        key_k = ((true_keystream - j - S[k])+256)%256
        key_k_dict[key_k] += 1
        

    
def rc4_crack(ciphers,ivs,first_byte,k):
        
        key_k_dict = [0]*256
        for i in range(message_volume):
            int_a = int.from_bytes(first_btyes[i], sys.byteorder)
            int_b = ciphers[i][0]
            true_keystream = int_a^int_b
            rc4key =  bytearray()
            rc4key.extend(bytes(list(ivs[i])))
            for j in range(k-3):
                rc4key.append(keys[j])
            # print(rc4key)
            run(k,true_keystream,rc4key,key_k_dict)
        cnt = 0
        for times in key_k_dict:
            cnt += times 
        
        max = -1
        backup_key_k=0
        for (i,times) in enumerate(key_k_dict):
            if times >= cnt*0.048 and times <= cnt*0.052 :
                key_k = i
                return key_k
            if times>max:
                max = times
                backup_key_k = i
        return backup_key_k
        

if __name__ == '__main__':
    for k in range(3,len_rc4key):
        ciphers = []
        ivs = []
        first_btyes = []
        for i in range(message_volume):
            (v,rc4key) = generate_rc4key(k)
            iv = (k,255,v)
            ivs.append(iv)
            plaintext = random_str(random.randint(10,100)).encode('ascii')
            first_btyes.append(plaintext[0:1])
            cipher = rc4_encode(plaintext,rc4key)
            # print(len(cipher))
            # print(cipher)
            ciphers.append(cipher)
            
        key_k = rc4_crack(ciphers,ivs,first_btyes,k)
        keys.append(key_k)

    kk = ''
    for i in keys:
        kk += chr(i)
    print("Cost %d message totally"%(message_volume*(len_rc4key-3)*255*255))
    print("The wep key is %s"%kk)
    if wep_key.decode('ascii')!=kk:
        exit(-1)
    # else:
    #     exit(0)