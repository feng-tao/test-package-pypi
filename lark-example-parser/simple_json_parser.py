"""
Learn Lark following https://github.com/lark-parser/lark/blob/master/docs/json_tutorial.md

Full examples could be found in https://github.com/lark-parser/lark/tree/master/examples

Repos:
- https://github.com/kennknowles/python-jsonpath-rw
- https://github.com/lark-parser/lark
"""

from lark import Lark, Transformer

json_parser = Lark(r"""
    value: dict
         | list
         | ESCAPED_STRING
         | SIGNED_NUMBER
         | "true" | "false" | "null"

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : ESCAPED_STRING ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')

json_parser_v2 = Lark(r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')

class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]
    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

text = '{"key": ["item0", "item1", 3.14]}'
"""
The AST looks like the following:

dict
  pair
    string	"key"
    list
      string	"item0"
      string	"item1"
      number	3.14
"""
ret = json_parser_v2.parse(text)

a = TreeToJson().transform(ret)
print (a) # it converts the string to AST then back to json
print( ret.pretty() )