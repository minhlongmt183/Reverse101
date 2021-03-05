import string

data = [ 
	0xa7c0aac235e24401, 0xfbc27a78732cd5c1, 0xe2bcc8dacc8f3ec1, 
	0x85d5db630397266b, 0x69bea716dfcc2f31, 0x5c8ba862e345f0c1, 
	0x37ff4d930dbf8d49, 0xd8d2a106d49107e3, 0x1a7e8d3ebcdb3381, 
	0x9a508da98d061483, 0xf8f6b6a16de5f681, 0xcd4cc067299fe05b,
	0x7d522ac63e52b6e9, 0x906c70584e07620b, 0x3f57d685d28b6b59,  
	0xe4d62684f5725a53, 0xf440fb91a0cb38f1, 0x1a5b98f646b8e7fb, 
	0xc030861704e18149, 0x5c0f7d9501e27b7b, 0x1fd3fae061fb3959, 
	0x8975066309fb71a3, 0xbb4c46f8d4f95501, 0x986c040271e0462b, 
	0xc21b85b2ba32a8b1, 0x4ab4a8ae2c428723, 0x965b0bcbf404f3c1, 
	0xb4dd1a1572321143, 0xe07a17b5aba8c741, 0xe043c7dee0cc3,  
	0x7444d23acc711ac1, 0xc6b08dadaec60843, 0xdd01213585018e41, 
	0x61c066798641a3c3
]
mask = 2**64-1
check_rcx = 0
num_xor = 0x5bc1048e26f1ce02
rcx = 0xabcdef9876543201

len_flag = len(data)

for i in range(len_flag):
    for char in string.printable:
        c = ord(char)

        if (rcx ** c) & mask == data[i]:
            print(char, end="")
            break

    rcx = data[i] ^ num_xor
