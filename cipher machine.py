print('hi! I am a cipher machine.')

userPut = input('Type in a sentence.')

key = input('Type in a longer sentence.')

#This is codebook
cb = {
    'a':0, 'b':1, 'c':2, 'd':3, 'e':4,
    'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10,
    'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
    'r':17, 's':18, 't':19, 'u':20,'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
#This is used for deciphering numbers.
cb2 = {
    0:'a', 1:'b', 2:'c', 3:'d', 4:'e',
    5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k',
    11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q',
    17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

encoded = ''

while len(key) < len(userPut):
    print("your 2nd sentence wasn't longer than your 1st sentence. Type again.")
    key = input('type a sentence.')

for a in range(len(userPut)):
  Kurr = key[a]
  curr = userPut[a]
  coded = cb[Kurr] + cb[curr]
  if coded > 25:
     coded = coded - 26 
  encoded = encoded + cb2[coded]
  
print('this is your (encoded) sentence:' + encoded)

decoded = ''

for a in range(len(encoded)):
  Kurr = key[a]
  curr = encoded[a]
  coded = cb[curr] - cb[Kurr]
  if coded < 0:
     coded = coded + 26 
  decoded = decoded + cb2[coded]

print('this is your orignal (uncoded) sentence:' + decoded)
print(""" To code the message,
I turn both sentences into numbers and
add them, and then tun them back
into letters. In other words, the
cipher would be impossible to crack
without the 2nd sentence.To decode
the message, I do the process
backward. Pretty cool, huh?""")




