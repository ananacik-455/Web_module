import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

try:
    response = requests.get(URL)
    response.raise_for_status()
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()

soup = BeautifulSoup(html_content, "html.parser")

# <span class="mw-page-title-main">Python (programming language)</span>
title_wiki = soup.find("span", class_="mw-page-title-main").text
print(title_wiki)

# <tr>
#     <th scope="row" class="infobox-label">
#         <a href="/wiki/Software_developer" class="mw-redirect" title="Software developer">Developer</a>
#     </th>
#     <td class="infobox-data organiser">
#         <a href="/wiki/Python_Software_Foundation" title="Python Software Foundation">Python Software Foundation</a>
#     </td>
# </tr>

# table_keys = soup.find_all("th", class_="infobox-label")
# print(table_keys)
# print(len(table_keys))
# table_values = soup.find_all("td", class_="infobox-data")
# print(table_values)
# print(len(table_values))

# for t_k, t_v in zip(table_keys, table_values):
#     key_name = t_k.text
#     value_name = t_v.text
#     print(key_name, value_name)

all_h2 = soup.select("h2#Syntax_and_semantics")
print(all_h2)
