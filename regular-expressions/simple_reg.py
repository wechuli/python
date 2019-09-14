import re

# define out phone number regex

pattern = re.compile(r"\d{3} \d{3}-\d{4}")


res = pattern.search("Call me at 415 555-4242!. rerer 815 543-4242")
res2 = pattern.findall("Call me at 415 555-4242!. rerer 815 543-4242")
print(res.string)
print(res2)
