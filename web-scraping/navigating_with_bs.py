from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol class="super-special">
    <li class="special">This list item is special.</li>
     <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
   
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
data = soup.body.contents
# print(data)
# print(data[1].next_sibling)

data2 = soup.find(class_='super-special').parent.parent
# print(data2)


data3 = soup.find(id="first").find_next_sibling()
# print(data3)

data4 = soup.select("[data-example]")[1].find_previous_sibling()
print(data4)
