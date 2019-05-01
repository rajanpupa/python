astr = 'Hello World'

# try parsing astr to int
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)
# try parsing again
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)