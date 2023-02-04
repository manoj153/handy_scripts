import re
import sys

url = sys.argv[1]
post_id = re.search("/p/(\w+)/", url).group(1)
print("post id\t" + post_id)
print("lyn id\t" + "[ig]" + post_id + "[/ig]")
