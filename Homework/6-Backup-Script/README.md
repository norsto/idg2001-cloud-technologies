# Backup script
I want to be able to run `backup .` or `backup foldername` to make a compressed file of the folder. The folder should be named after the date, so something like `2024-03-20.tar.gz` (or `.zip`).

__Problem:__
Make a script which does this, and alias/Powershell function it as `backup`.

__Hints:__
For Unix (Mac/Linux) you'd probably want to use the `tar` command and format, while in Windows (Powershell) you'd probably want to use `zip` files and the `Compress-Archive` function.

You decide whether or not the compressed file will be placed in the current working directory, or if it will be placed in some sort of centralized backup folder.
