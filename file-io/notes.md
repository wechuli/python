# File IO With Python

- Read text files in Python
- Write text files in Python
- Use "with" blocks when reading/writing files
- Decribe the different ways to open a file
- Read CSV files in Python
- Write CSV files in Python
- Reading JSON Files

## Reading Files

- You can read a file with the `open` function
- `open` returns a file object to you
- You can read a file object with the `read` method

### Cursor Movement

Python reads files by using a cursor
This is like the cursor you see when you are typing
After a file is read, the cursor is at the end
To move the cursor, use the `seek` method

You can close a file with the close method
You can check if a file is closed with the closed attribute
Once closed, a file can't be read again
Always close files - it frees up system resources!

## File Modes

- 'r' - open for reading
- 'w' - open for writing, truncating the file first
- 'x' - open for exclusive creation, failing if the file already exists
- 'a' - open for writing, appengin to the end of the file if it exists
- 'b' - binary mode
- 't' - text mode(default)
- '+' - text mode(default)