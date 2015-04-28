参考DummySpider.py中的示例.

# parse #
```
def parse(self, response):
    '''如果有返回值将被传递到process_item处理'''
    ...
```

## xpath ##
```
hxs = HtmlSelector(response.body)
itemlist = hxs.re('<td class=\'td10\'>·.*?<\/td>')
for item in itemlist:
    title = item.re('<a[^>]*[^>]*>(.*)[^<]*<\/a>')[0]
    yield title
```

## regex ##
```
itemlist = hxs.select('//td[@class="td10"]')
for item in itemlist:
    #print item._root.xpath('a/text()')
    title = item.select('a/text()').extract()[0]
    link = item.select('a/@href').extract()[0]
    yield (title, link)
```

# pipeliner #
```
def process_item(self, item):
    ...
```