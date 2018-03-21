=begin
class Ha
    attr_accessor :value, :next_node

    x= Hash.new
    x.value = "Azhar"
    x.next_node = 2
    puts x
end
asfasgas
aasgasgas
agagasf


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