=begin
class Hash

    attr_accessor :value, :next_node

    def initialize
        @val = value
        @next_nodex = next_node
        puts "Initialized a Node with value:  " + value.to_s 
    end

    def self.attr

    end

    x= Hash.new
    x.value = "Azhar"
    x.next_node = 2
    puts x
end



# String is already the parent class
class Post
  attr_accessor :title

  def replace_title(new_title)
    self.title = new_title
  end

  def print_title
    puts title
  end
end
=end

Rails::Initializer.run do |config|
    h = HashWithIndifferentAccess.new
    puts h
end


pst = Post.new
pst.title = "Cream of Broccoli"
pst.replace_title("Cream of Spinach")
puts pst.print_title