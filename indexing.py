Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#positive Indexing
a="vijayawada"
a[2]
'j'
a[4]
'y'
a[0]+a[1]=a[2]
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a[0]+a[1]+a[2]
'vij'
a="i am in class
SyntaxError: unterminated string literal (detected at line 1)
a="i am in class"
a[2]
'a'
a[3]+a[4]+a[5]
'm i'
>>> a[4]
' '
>>> a="vijayawada is a royal city"
>>> a[14]
'a'
>>> a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
>>> a[22]+a[23]+a[24]+a[25]
'city'
>>> a[11]+a[12]
'is'
>>> a="vizag is a city of destiny"
>>> a[-15]+a[-14]+a[-13]+a[-12]
'city'
>>> a[-25]+a[-24]+a[-23]+a[-22]+a[-21]
'izag '
>>> a[-25]+a[-24]+a[-23]+a[-22]+a[-21]+a[-20]
'izag i'
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[21]
'vizags'
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]=a[-2]+a[-1]
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'f destiny'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
>>> a="simple is better than complex"
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
>>> a[-7]+a[-8]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'c omplex'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
