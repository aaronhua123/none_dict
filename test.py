name = "none_dict"
from none_dict import Dict

if __name__ == '__main__':
    # List([])[:]
    # print(Ellipsis)item
    # dict 1 没有值(list) 2 没有key 3 list 4 dict
    d = Dict({"a": None, "itemList": [{"e": 1}, {"e": 2}], "d": {"e": 123}})
    print(d['a'])
    print(int(d['a']))
    print(float(d['a']))
    print(bool(d['a']))
    print(None)
    # print(d.itemList[1])
    # d = {"a": None, "itemList": [{"e": 1}, {"e": 2}]*100_0000, "d": {"e": 123}}
    # 想拿字典
    # print(d['a'])
    # print(d['a'][1:2])  # 拿
    # print(d['a'][...])
    # print(d['b'][0:3])
    # print(d['b'][...])
    # print(d['b'])
    #
    # print(d['c'])
    # print(d['c'][2])
    # print(d['c'][...])
    # start = time.time()
    # for _ in range(1000000):
    # print(d['d'])
    # print(type(d['itemList'][:]))
    # for i in d['itemList']:
    #     print(i,type(i))
    # for i in d['itemList']:
    #     i
    # print(d['d'][...])
    # print(time.time()-start)
    # res = requests.Response()
    # res._content = b'{"a": null, "itemList": [1, 2],"d": {"e":123}}'
    # l = res.dict()
    # print(l['result']['itemList']['ass'])