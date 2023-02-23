import codecs

f = open('draft.html', 'r', 'utf-8')

begin = f.find('<')
while begin > -1:
    end = f.find('>')
    f = f[: begin] + f[end + 1:]

    #return file
f.write("res.txt")
f.close()
