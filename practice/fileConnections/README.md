## File Types
Below is a list of the most common file types. In addition to the ones below, there are many more file extensions
that tell you what information the file has and how it is encoded. Understanding the file extension
is crucial to parsing the files correctly.
### Why do I need to know the file type?
Any time you work with a file you need to parse it. Parsing a file means that you use a library (built in or imported)
to read the file so that the computer can understand what is written inside of it. 
If the file is not parsed correctly, the data can be corrupt which will not work for any further processing. 

Any time you work with a file, always double check that the data loaded correctly.
### File interactions - connect files together
In larger projects, all of the functionality is broken down into smaller pieces which are located in separate files. 
Sometimes you want to use a function that you defined in one file in another. In this case, 
you want to import the file that contains the function you need. 

For  example, in this project we have a function defined in lesson1_practice/ifStmts.py
If you want to use that function somewhere else, you would type in this code: 

``
import ifStmts.py
``

When you do an import of a local file, you have to make sure that wherever you import into can "see"
the file that you are trying to import. The computer can only "see" files that are in the same directory unless you provide the full file path
In the example above, the full file path would stem from the home directory.