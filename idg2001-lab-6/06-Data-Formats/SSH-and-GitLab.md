# Setting up SSH with GitLab
For git and GitLab (or GitHub) to work properly together, we want to set up SSH keys. These are essentially password files used when cloning, pushing and pulling, so we won't have to mess around with passwords.

Follow the first parts of this guide - down to (and maybe including) the config file.

https://docs.gitlab.com/ee/user/ssh.html

Try without the config file. If it does not work, make the file.

Set up GitLab (and maybe GitHub) with the contents of the public key (`blabla.pub`). Clone a repo and see if it worked.


## GitLab IDG2001 repos
When done, might I suggest cloning the IDG2001-2024 repos?

https://gitlab.stud.idi.ntnu.no/idg2001/2024

Then you can just pull the repos to get the most up to date contents of the lectures, labs, etc.


## Puller/sync script
We can make a script pulling all scripts. See the file called `autopuller.sh`. Feel free to rename it. Mine are usually called `sync.sh`, for example.

### Unix
If using Mac or Linux, they should work - though you may have to tell the OS it is an executable script. Run the following command.

```bash
chmod +x autopuller.sh
```

(Or whatever you've renamed the file as.) You may have to add `sudo` in front of the command.

```bash
sudo chmod +x autopuller.sh
```

### Windows
If you're using Windows, you have a few possible solutions. You can

1. Use Git Bash or WSL/Ubuntu (and use what described above)
2. Use Powershell instead.

If using Powershell, do the following.

1. Rename the file to `autopuller.ps1` (the file extension being the important thing here)
2. Install suggested Powershell add-on in VS Code.
3. Press Run button in VS Code to pull all.

You can also use `Set-ExecutionPolicy` to allow running scripts, make a Windows shortcut for it, maybe modify the shortcut to allow running it in Powershell, etc. It works. It may be a good idea. It definitely takes a bit of effort.
