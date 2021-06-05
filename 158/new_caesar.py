import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
nums=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
# print(ALPHABET)
def b16_encode(plain):
	enc = ""
	for c in plain:
    			
		binary = "{0:08b}".format(ord(c))
		# print(binary)
		# print(int(binary[:4], 2))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(enconded):
    	
	enc = ""
	bytesarary=""
	letters=""
	for c in enconded:
    			
		bytesarary+=str(ALPHABET.index(c))
	for i in range(0,len(bytesarary),2):
		arr=nums[int(bytesarary[i])]+nums[int(bytesarary[i+1])]
		# print(int(arr,2))
		letters+=chr(int(nums[int(bytesarary[i])]+nums[int(bytesarary[i+1])],2))
		# print(letters)
	return letters
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
def deshift(c, k):
	print("---------------deshift----------------------")
	print(c)
	print(k)
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	print("---------------deshift----------------------")

	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "abc"
key = "redacted"

b16 = b16_encode(flag)
print(b16)
enc = ""

for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
print("------------------------------------------")
b16 = b16_decode(b16)
print(b16)
b16="hfjcig"
enc=""
for i, c in enumerate(b16):
	print(key[i % len(key)])
	print(c)
	
	# print(shift(c, key[i % len(key)]))
	enc += deshift(c, key[i % len(key)])
	break

print(enc)