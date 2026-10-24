from tools.tavily import tavily_search

from tools.flight import search_flights

res = search_flights("plan a 7 day Nepal trip from Bangladesh")

# res = tavily_search("Best Hotels in India")
print(res)