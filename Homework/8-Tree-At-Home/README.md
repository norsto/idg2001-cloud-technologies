# Tree at home / from Wish

The command `tree` is great! It allows you to show a tree structure of all the subdirectories of a directory, as well as their contents. You should install and use it :D

For this homework, recreate the command, but simplfied. I want the following to be true:
 
- Running `tree` should show all subdirs and subsubdirs and so on, including all files. Easy difficulty: Only support 2 layers.
- Running `tree {FolderName}` (E.g., `tree Assignment2`) should do this for the dir (with subdirs etc.) or the folder `Assignment2`. Thus, "`tree .`" should be equivilent to "`tree`".
- Running `tree 2` should only go two levels down. Simply use the fact that "2" is an integer to detect whether or not the second argument is the depth or a folder. I.e., you would not expect your script to support `tree 2` where the foldername is "2".


## Suggestions
Google (og ChatGPT) how to list dirs and subdirs. StackOverflow has some nice examples. This uses the `os` module. You could also try to do this without googling the solution directly.


## Extensions
If you want to, you can extend the program to support folders named for example "2", by using modules like argparse to allow for something like `tree -L 2`, which is how the actual module works.