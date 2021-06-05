from pwn import *
import re
import json

letters="0123456789zxcvbnmasdfghjkl;qwertyuiop[]~!@#$%^&*()_+:"
# letters="ab"
r=remote('mercury.picoctf.net',64260)
dic={}

for i in letters:

    r.recvuntil("What data would you like to encrypt?")
    r.sendline(i)

    s=r.recvline()
    s=r.recvline().decode("utf-8").strip()
    dic[s]=i
    # print(s)
print(dic)



with open('data.json', 'w') as fp:
    json.dump(dic, fp,  indent=2)

# print(dic['51'])
# dic['46']='w'
# enc="51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959"
# dec=""
# for x in range(0, len(enc), 2):

#     let=enc[x]+enc[x+1]
#     # print(let)
#     dec+=dic[str(let)]

# print(dec)