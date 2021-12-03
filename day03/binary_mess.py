class BinaryMess:
  '''Howdy Python'''

  def __init__(self, filepath):
    self.bit_counts = []
    BinaryMess.count_bits(self, filepath)

  def run(filepath):
    binary_mess = BinaryMess(filepath)
    return binary_mess.gamma_rate() * binary_mess.epsilon_rate()

  def gamma_rate(self):
    bits = ''.join(['0' if count['0'] > count['1'] else '1' for count in self.bit_counts])
    return int(bits,2)

  def epsilon_rate(self):
    bits = ''.join(['0' if count['0'] < count['1'] else '1' for count in self.bit_counts])
    return int(bits,2)

  def count_bits(self, filepath):
    with open(filepath) as fp:
      line = fp.readline().strip()
      while line:
        column = 0
        for bit in list(line): # TODO: Comprehension...
          if len(self.bit_counts) <= column: # and not this...
            self.bit_counts.append({'0': 0, '1': 0})
          self.bit_counts[column][bit] += 1
          column += 1 # and not this
        line = fp.readline().strip()

######## TESTS
print("Part 1: TEST (should be 198)")
print(BinaryMess.run('./test_input.txt'))
print("")
print("Part 1")
print(BinaryMess.run('./input.txt'))
# print("")
# print("Part 2: TEST (should be 230")
# print(BinaryMess.run('./test_input.txt'))
# print("Part 2")
# print(BinaryMess.run('./input.txt'))
