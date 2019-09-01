- BeautifulSoup(html_string,"html.parser") - parse HTML
- Once parsed. There are several ways to navigate
  - By Tag Name
  - Using find - returns one matching tag
  - Using find_all - returns a list of matching tags
  - We can use CSS selectors to navigate

## Navigating with CSS Selectors

`select` - returns a list of elements matching a CSS selector: - Select by id of foo: #foo - Select by class of bar: .bar - Select children: div > p - Select descendents: div p

## Accessing Data in Elements

- `get_text` - access the inner text in an element
- `name` - tag name
- `attrs`-dictionary attributes

You can also access attribute values using brackets

## Navigating with Beautiful Soup

Via Tags

- parent/parents
- contents
- next_sibling / next_siblings
- previous_sibling / previous_siblings

Via Searching

- find_parent / find_parents
- find_next_sibling / find_next_siblings
- find_previous_sibling / find_previous_siblings
