def say_hi(func): # decorator
  def new_toy():
      print("hi")
      func()
  def second_toy():
      print("hello")
  return new_toy


def talk():
  print("I'm a Robot")

@say_hi #panggil decorator
def sing():
  print("la la la")
talk()
sing()
talk()