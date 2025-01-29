# CLI Basics


## Relevant commands
| Command | Description |
|-|-|
| ls <dir> | Lists content of folder |
| cd <dir> | Change-Directory. Changes the active directory.  |
| pwd | Print-Working-Direcroty. Prints the current working directory (cwd) |
| mkdir/rmdir <dir> | Make or remove directory. |
| cat <file> | Print file |
| touch <file> | Make (empty) file |
| grep <query> | Pipe stuff into grep, and search. E.g., `cat <file> \| grep <search term>` |


## Paths and terms
- Active directory: The path printen when running `pwd`.
- Relative paths: Where is a file or folder located _relative to active directory_.
- Absolute paths: Where is a file or folder located _relative to root directory ("/")_.
- `..`: Go up one layer
- `~`: Home dir


## Alias / PS Functions vs PATH
To create your own commands for running scripts, without having to do something like `/Users/username/Documents/scripts/run_update.sh`, we can do one of two things:

1. Add the directory `/Users/username/Documents/scripts` to the PATH variable.
2. Add an alias/function.

Solution (1) is the most proper way, I guess, but more effort. Use (2) alias (Mac/Linux) or PowerShell functions (Windows) instead.

And feel free to ask me (Paul) if you want to copy my file(s).

### Mac/Linux**
Find your profile file, which is probably `~/.zprofile` or something like that, and add something like this following.

```bash
alias update=/Users/username/Documents/scripts/run_update.sh
```

Restart the terminal, and the command `update` should now work, and run the script `run_update.sh`. This assumes it has the relevant permissions, though. Google it. It should be something like:

```bash
sudo chmod +x run_update.sh
```

when in the same dir.

### Windows
First of all, use Powershell (you can also install Windows Terminal in the Windows Store).

Run the following command to ensure the profile file exits.

```powershell
$profile
```

It should then print out the location of the file, which should be something like `~/Documents/Windows-Powershell`.

Add something like the following, and restart Powershell/Terminal.

```bash
function update {pwsh -File "/Users/username/Documents/scripts/run_update.sh"}
```

Possible modifications:
- You need to change the path to Windows-style path.
- If the function should take trailing arguments, you need to add ` $args` after the path (before the curly brackets).

Example where I create the `code <opts>` command which actually runs `code-insiders <opts>`:

```bash
function code {code-insiders $args}
```
