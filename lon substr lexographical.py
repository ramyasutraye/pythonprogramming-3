s=str(raw_input())
for x in range(1,len(s)):
    if s[x:]>s:
        print(s[x:])
        break
