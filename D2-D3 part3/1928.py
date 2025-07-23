str = "TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u"
str2 = ""
for ch in str:
    ch = ord(ch)
    num = format(ch, "08b")
    str2 += num
# print(str2)

for i in range(0, len(str2), 6):
    # print(str2[i : i + 6])
    new_num = int(str2[i : i + 6], 2)

    print(new_num, end=" ")
