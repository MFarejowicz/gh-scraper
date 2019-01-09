# gh-scraper
This simple tool can be used to parse Grubhub restaurant pages and output
the menu items in an easy to use JSON format.

This was created to be used in conjunction with [McD4Me](https://github.com/MFarejowicz/McD4Me).
*Note that this is not an actual Grubhub scraper, since Grubhub loads the content
for their pages via HTTP requests.* Instead, it should be fed an HTML file that
it will then parse and output into JSON format.

## Usage
0. Make sure BeautifulSoup is installed. See
[this page](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
for details.
1. First, head to the Grubhub page for your desired restaurant.
2. Save the HTML page after it loads. This can be done by viewing page source
and saving or simply hitting CTRL-S or COMMAND-S on the page.
3. Move the HTML file to the same directory as `scrape.py`
4. Change the `'FILENAME.html'` and `'FILENAME.json'` parameters on lines 38 and
59 respectively, replacing `FILENAME` with the file name of your choice.
5. Run `python3 scrape.py`

The file will be output in the same folder as the input HTML file. To see an
example of the input and output, refer to the `example` folder.

### JSON output

The JSON output comes in the following format:
```
{
  "group":"Kung Fu Classic",
  "name":"Kung Fu Black Tea",
  "id":"KunFuBlaTea",
  "price":3.58
}
```
creating an object for each menu item, and putting everything in one resulting 
array.
