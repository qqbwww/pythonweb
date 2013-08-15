from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols')

#需要全部参数
print s.substitute(lang='Python', howmany=3)
#可以缺少key
print s.safe_substitute(lang='Python')

