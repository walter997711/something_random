# z=int(input("X: "))
# while True:
#     z=3*z*(1-z)
#     print(z)
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq)
print(gc_fraction(my_seq),type(gc_fraction(my_seq)))