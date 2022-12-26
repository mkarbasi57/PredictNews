import re

def regex(text):
       x = re.sub(r"^.*- ایرنا -", "", text)
       x = re.sub(r"^.*- ایرنا-", "", x)
       return x