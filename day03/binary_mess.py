class BinaryMess:
  '''Howdy Python'''

  def __init__(self, filepath):
    self.bit_counts = []
    self.contestants = []
    BinaryMess.count_bits(self, filepath)

  def run(filepath, part=1):
    binary_mess = BinaryMess(filepath)
    if part == 1:
      return binary_mess.gamma_rate() * binary_mess.epsilon_rate()
    elif part == 2:
      print("oxygen_generator_rating: ")
      print(binary_mess.oxygen_generator_rating())
      print("-------")
      print(binary_mess.contestants)
      return binary_mess.co2_scrubber_rating() * binary_mess.oxygen_generator_rating()

  def gamma_rate(self):
    return int(self.high_count_bits(),2)

  def high_count_bits(self):
    return ''.join(['0' if count['0'] > count['1'] else '1' for count in self.bit_counts])

  def low_count_bits(self):
    return ''.join(['1' if count['0'] > count['1'] else '0' for count in self.bit_counts])

  def epsilon_rate(self):
    return int(self.low_count_bits(),2)

  def oxygen_generator_rating(self):
    print(f"HIGH COUNT BITS: {self.high_count_bits()}")
    remaining_lines = self.contestants.copy()
    for idx, bit in enumerate(list(self.high_count_bits())):
      remaining_lines = [line for line in remaining_lines if line[idx] == bit]
      if len(remaining_lines) == 1:
        print(remaining_lines[0])
        return int(remaining_lines[0],2)

      # remaining_lines = filter(lambda line: line[idx] == bit, remaining_lines)

      # for line in remaining_lines:
      # This doesn't end up checking all the elements.......
      #   print(f"CHECKING LINE: {line}")
      #   print(f"VALUE IS {line[idx]}")
      #   if line[idx] != bit:
      #     print("REMOVE!")
      #     remaining_lines.remove(line)
      #     print(f"NOW REMAINING LINES IS {remaining_lines}")
        # if len(remaining_lines) == 1:
        #   return remaining_lines[0]
    #   print("REMINING LINES")
    #   print(remaining_lines)
    # return "101"

  def co2_scrubber_rating(self):
    return 1

  def count_bits(self, filepath):
    with open(filepath) as fp:
      line = fp.readline().strip()
      while line:
        self.contestants.append(line)
        column = 0
        for bit in list(line): # TODO: Comprehension...
          if len(self.bit_counts) <= column: # and not this...
            self.bit_counts.append({'0': 0, '1': 0})
          self.bit_counts[column][bit] += 1
          column += 1 # and not this
        line = fp.readline().strip()

######## TESTS
print("Part 1: TEST (should be 198)")
print(BinaryMess.run('./test_input.txt', 1))
print("")
print("Part 1")
print(BinaryMess.run('./input.txt', 1))
print("")
print("Part 2: TEST (should be 230")
print(BinaryMess.run('./test_input.txt', 2))
# print("Part 2")
# print(BinaryMess.run('./input.txt'))
