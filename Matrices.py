import json
import copy
from fractions import Fraction
import shutil
import math

size = int(input("size: "))
Default = []
for row in range(size):
  Default.append([])
  for column in range(size):
    Default[row].append(0)
  for column in range(size):
    if row == column:
      Default[row].append(1)
    else:
      Default[row].append(0)
Current = copy.deepcopy(Default)


def draw(text):
  max_length = shutil.get_terminal_size().columns
  justify = math.floor((max_length - 2*size)/(2*size))
  
  print(chr(27) + "[2J")
  for line in Current:
    pretty = ""
    for i, frac in enumerate(line):
      pretty = pretty + str(frac).ljust(justify)
      if i + 1 == size:
        pretty = pretty + '|'
      else:
        pretty = pretty + ','
    print(pretty)
  print (text)

while True:
  draw("clear(cl), define(def), switch(sw), line(number):")
  cli = input()
  match cli:
    case "clear" | "cl":
      Current = copy.deepcopy(Default)
      #break

    case "define" | "def":
      for line, line_v in enumerate(Current):
        for column, column_v in enumerate(line_v[:len(line_v)//2]):
          draw(f"({line+1}|{column+1})")
          val = input()
          if val == '':
            val = Current[line][column]
          else:
            val = Fraction(val)
          Current[line][column] = val
      #break
      
    case "switch" | "sw":
      text = "line 1:"
      draw(text)
      line1 = int(input()) - 1
      text += f" {line1 + 1} line 2:"
      draw(text)
      line2 = int(input()) - 1
      tmpLine = Current[line1]
      Current[line1] = Current[line2]
      Current[line2] = tmpLine
      print(Current)

    case source:
      source = int(source) - 1
      text = f"Source line = {int(source + 1)}, Factor"
      draw(f"{text}:")
      factor = Fraction(input())
      text += f" = {factor}, Target line"
      draw(f"{text}:") 
      target = int(input()) - 1
      for cell, cellv in enumerate(Current[source]):
        if not target == source:
          Current[target][cell] = Current[target][cell]+cellv*factor
        else:
          Current[target][cell] = cellv*factor