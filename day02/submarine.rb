class Submarine
  attr_accessor :depth, :horizontal_position

  VALID_INSTRUCTIONS = %q(forward down up).freeze

  def self.run(filepath = 'input.txt')
    sub = new(depth: 0, horizontal_position: 0)
    sub.move(filepath)
    puts sub.depth * sub.horizontal_position
  end

  def initialize(attributes)
    self.depth = attributes.fetch(:depth)
    self.horizontal_position = attributes.fetch(:horizontal_position)
  end

  def move(filepath)
    File.readlines(filepath).each do |line|
      instructions = line.split
      raise("Unallowed instruction! #{instructions[0]}") unless VALID_INSTRUCTIONS.include?(instructions[0])
      self.send(instructions[0], instructions[1].to_i)
    end
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

Submarine.run