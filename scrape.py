from bs4 import BeautifulSoup
import json, string, re
existing_id = set()

def scrub_start(name):
    """
    Removes something like 'A1.' or '57.' from the start of a menu item
    """
    split = name.split()
    first = split[0]
    if any((char in string.digits) for char in first) and '.' in first:
        return ' '.join(split[1:])
    return name

def make_id(name):
    """
    Makes an id from a name by taking the first two letters of every word
    """
    out = ''
    name = re.sub(r'([^\s\w]|_)+', '', name)
    split = name.split()
    for word in split:
        out += word[:3] if len(word) > 3 else word
    if out in existing_id:
        out = out + "2"
    existing_id.add(out)
    return out

def scrub_price(price):
    """
    Parses the string price and returns the float value of the price
    """
    if price[0] == '$':
        price = price[1:]
    return float(price)


with open('xxxx.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

output = []
for ms in soup.find_all('div', class_='menuSection'):
    for mi in ms.find_all('div', class_='menuItemNew'):
        menu_item = dict() # Initialize empty entry for menu item

        menu_item['group'] = ms['name'] # Get group from menu section

        h = mi.find('h6', class_='menuItem-name')
        clean_name = scrub_start(h.a.string)
        menu_item['name'] = clean_name # Get name

        menu_item['id'] = make_id(clean_name) # Make an id from the name

        p = mi.find('span', class_='menuItem-displayPrice')
        menu_item['price'] = scrub_price(p.string) # Get and parse price

        output.append(menu_item) # Append finished menu item to output

file = open("xxxx.json", "w")
json.dump(output, file)
file.close()
