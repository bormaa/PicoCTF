w="jU5t_a_s"
s="jU5t_a_sna_3lpm18gb41_u_4_mfr340"
for i in range(8,16,1):
    w+=s[23-i]
for i in range(16,32,2):
    w+=s[46-i]
for i in range(31,17,-2):
    w+=s[i]

print(w)