import this
import codecs
my_zen=codecs.encode(this.s,'rot13')
print (my_zen)

My_lowerZen=my_zen.lower()
My_lowerZen.count('better')
My_lowerZen.count('never')
My_lowerZen.count('is')

my_upperZen=my_zen.upper()
print(my_upperZen)

my_replace=my_zen.replace('i', '&')
print(my_replace)