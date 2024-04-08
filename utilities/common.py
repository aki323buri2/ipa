# %%
from pathlib import Path 
from functools import reduce 
from datetime import date
from dateutil.relativedelta import relativedelta 
import pandas as pd 
import csv 

def sand(s, a, b=None): return f"{a}{s}{a if b is None else b}"
def sq(s): return sand(s, "'")
def dq(s): return sand(s, '"')
def paren(s): return sand(s, "(", ")")
def braces(s): return sand(s, "{", "}")
def bracket(s): return sand(s, "[", "]")
def comma(*ss): return ",".join(ss)
def and_(*ss): return " and ".join([paren(x) for x in ss])
def  or_(*ss): return  " or ".join([paren(x) for x in ss])

# a = "a"
# b = "b"
# s = "s"
# ss =["a=aa", "b=bb", "c=cc"] 
# print(f"sand({comma(*[dq(x) for x in [s, a, b]])}) → {dq(sand(s, a, b))}")
# print(f"sand({comma(*[dq(x) for x in [s, a]])}) → {dq(sand(s, a))}")
# print(f"sq({comma(*[dq(x) for x in [s]])}) → {dq(sq(s))}")
# print(f"dq({comma(*[dq(x) for x in [s]])}) → {sq(dq(s))}")
# print(f"paren({comma(*[dq(x) for x in [s]])}) → {dq(paren(s))}")
# print(f"paren({braces(*[dq(x) for x in [s]])}) → {dq(braces(s))}")
# print(f"paren({bracket(*[dq(x) for x in [s]])}) → {dq(bracket(s))}")
# print(f"paren({comma(*[dq(x) for x in ss])}) → {dq(comma(*ss))}")
# print(f"and_({comma(*[dq(x) for x in ss])}) → {dq(and_(*ss))}")
# print(f" or_({comma(*[dq(x) for x in ss])}) → {dq( or_(*ss))}")

def kishu(day = date.today()):
  kishu = day + relativedelta(month=4, day=1)
  return kishu if kishu <= day else kishu + relativedelta(years=-1)
def kimat(day = date.today()):
  return kishu(day) + relativedelta(years=1, days=-1)

# memo = None 
# for day in [date.today() + relativedelta(months=-x) for x in range(20)]:
#   shu = kishu(day)
#   mat = kimat(day)
#   if shu.year != memo:
#     memo = shu.year 
#     print("*" * 20)
#   print(shu, "|", day, "|", mat)

def fullpath(*path):
  root = Path(".")
  full = reduce(lambda a, b: Path(a) / Path(b), path, root)
  return full.resolve().absolute() 

def ensure_dir(*path): 
  dirname = fullpath(*path)
  dirname.mkdir(exist_ok=True, parents=True)
  return dirname 


def save_csv(df, filename, encoding="utf-8_sig", index=False, quoting=csv.QUOTE_ALL, **kwargs):
  filename = fullpath(filename) 
  df.to_csv(filename, encoding=encoding, index=index, quoting=quoting, **kwargs)
  return filename 

def load_csv(filename, encoding="utf-8_sig", **kwargs): 
  return pd.read_csv(filename, encoding=encoding, **kwargs)

# df = pd.DataFrame([dict(id=x, name=f"name of {x:3}") for x in range(100)])
# filename = ensure_dir("text") / "test.csv" 
# kwargs = {} 
# load_csv(save_csv(df, filename))

class dotdict(dict):
  def __getattr__(self, name): 
    return self.get(name)
  def __setattr__(self, name, value):
    self[name] = value 
  def dict(self):
    return dict(self)

