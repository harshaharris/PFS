Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:4]
'code'
a[4:9]
'gnan'
[:3]
SyntaxError: invalid syntax
a[:3]
'cod'
a[4:]
'gnan'
a[0:9]
'codegnan'
a="work hard until you succeed"
a[10:15]
'until'
a[5:9]
'hard'
a[0:5]
'work '
a[20:27]
'succeed'
b="time is very precious"
a[13:21]
'il you s'
b[13:21]
'precious'
b[8:12]
'very'
b[0:4]
'time'
#negative
a="i love python"
a[-1:-7]
''
a[-7:-1]
' pytho'
a[-6:-1]
'pytho'
a[-7:0]
''
a[-6:0]
''
a[-6:

  ]
'python'
a[-12:-7]
' love'
a[-11:-7]
'love'
b="today is weekend"
b[-18:11]
'today is we'
b[-18:-11]
'today'
b[-7:-1]
'weeken'
b[-10:8]
'is'
b[-7:]
'weekend'
a="data science"
a[::]
'data science'
a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a[::3]
'dacn'
>>> a="machine learning"
>>> a[::4]
'miln'
>>> a[:9]
'machine l'
>>> a[::6]
'men'
>>> a[5:]
'ne learning'
>>> a[:9]
'machine l'
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a="cloud computing"
>>> a[1:11:2]
'lu op'
>>> a[2:14:4]
'ocu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dcmu'
>>> #upside striding
>>> #from cloud computing
>>> #negative striding
>>> #negative striding
>>> a="python course"
>>> a[-1:-11-2]
''
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
