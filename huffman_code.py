import huffman

frequency_table = [('a', 100), ('b', 150), ('c', 150), ('d', 250), ('e', 350)]

encodings = huffman.codebook(frequency_table)

print(f'encoded table: {encodings}')
print(f'frequency table: {frequency_table}')

total_bits = sum([(len(x[1])*y[1]) for x,y in zip(encodings.items(), frequency_table)])
print(f'total amount of bites: {total_bits}')

encoded_string = '1000000110110101'
decoded_string = ''
temp_string = ''
values = encodings.values()
inv_map = {v: k for k, v in encodings.items()}
for char in encoded_string:
  temp_string += char
  if temp_string in encodings.values():
    decoded_string += inv_map.get(temp_string)
    temp_string = ''

print(decoded_string)