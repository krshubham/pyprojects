import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bitss, encoding='utf-8', errors='surrogatepass'):
	for bits in bitss.split(' '):
		n = int(bits, 2);
		ans = int2bytes(n).decode(encoding, errors)
		print(ans,end='');

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


print('Welcome!');
print('type "bin" to conevrt str to binary and "str" to convert bin to string');
a = input();

if(a=='bin'):
	print('Enter the string, space delimitted');
	string = input();
	ans = ' '.join(format(ord(x), 'b') for x in string);
	print(ans)
elif(a=='str'):
	print('Enter the binary string, space delimitted');
	string = input();
	text_from_bits(str(string));
	print();
