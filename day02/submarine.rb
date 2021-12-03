class Submarine
  attr_accessor :depth, :horizontal_position

  VALID_INSTRUCTIONS = %q(forward down up).freeze

  def self.run(filepath = 'input.txt')
    sub = new
    sub.move(filepath)
    puts sub.depth * sub.horizontal_position
  end

  def move(filepath)
    File.readlines(filepath).each do |line|
      instructions = line.split
      raise("Unallowed instruction! #{instructions[0]}") unless VALID_INSTRUCTIONS.include?(instructions[0])
      self.send(instructions[0], instructions[1].to_i)
    end
  end
end

class Part1Submarine < Submarine
  def initialize
    self.depth, self.horizontal_position = 0, 0
  end

  private def forward(units)
    self.horizontal_position += units
  end

  private def down(units)
    self.depth += units
  end

  private def up(units)
    self.depth -= units
  end
end

class Part2Submarine < Submarine
  attr_accessor :aim

  def initialize
    self.aim, self.depth, self.horizontal_position = 0, 0, 0
  end

  private def forward(units)
    self.horizontal_position += units
    self.depth += aim * units
  end

  private def down(units)
    self.aim += units
  end

  private def up(units)
    self.aim -= units
  end
end

Part1Submarine.run('test_input.txt')
Part2Submarine.run('test_input.txt')