import base64

# list for debug values
debugs = []
with open('.log', 'r') as log_file:
    lines = log_file.read().split('\n')
for line in lines[1:-1]:
    debugs.append(int(line.split()[3]))


def decrypt(passwd, debugs):
    solve = []
    b = 14695981039346656037
    c = 1099511628211
    passwd = int(base64.b64decode(str.encode(passwd)).decode(), 16)
    passwd ^= 1152921504606846975
    debugs.append(passwd)
    debugs = debugs[::-1]
    debugs.append(b)
    for i in range(len(debugs) - 1):
        solve.append(chr(int((debugs[i] ^ debugs[i+1]) / c)))
    print( 'PASSWORD: ' + ''.join(solve[::-1]))
    quit()


print(decrypt('YzQwZDFmMWI3YmRkNjAxMg==', debugs))
