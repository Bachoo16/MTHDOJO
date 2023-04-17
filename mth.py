
class Mathdojo:
      def __init__(self):
            self.resultado = 0

      def mas(self, *args):
            for arg in args:
                  self.resultado += arg
            return self
      
      def menos(self, *args):
            for arg in args:
                  self.resultado += arg
            return self
      
md = Mathdojo()

md.mas(31, 23, 20)
print(md.resultado)

md.mas(1).mas(2,3).mas(44, 56, 68)
print(md.resultado)

md.menos(23, 12, 23)
print(md.resultado)

md.menos(6).menos(3, 2).menos(3, 12, 16)
print(md.resultado)