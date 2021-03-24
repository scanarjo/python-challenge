input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

def convert(char):
  codePoint = ord(char)

  if(codePoint < 97):
    return char

  newCodePoint = (((ord(char) + 2) - 97) % 26) + 97

  return chr(newCodePoint)


convertedChars = list(map(convert, input))

print(''.join(convertedChars))

url = "/pc/def/map"

transTable = url.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

print(url.translate(transTable))
