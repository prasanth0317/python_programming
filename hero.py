class superhero:
      def __init__(self,name,power):
          self.name=name
          self.power=power

      def display_power(self):
            print(f"{self.name} 's power is {self.power}")

class ironman(superhero):
     def __init__(self,name,power,suit_type):
           super().__init__(name,power)
           self.suit_type=suit_type

     def display_suit(self):
           print(f"{self.name} wears a {self.suit_type} suit.")


ironman=ironman("ironman","genius intellect","marks 85")
ironman.display_power()
ironman.display_suit()

           
