# Chapter 2 | Git Repository Setup & SSH Authentication

> > SSH Key
An SSH key is a secure way to connect your computer with GitHub without entering your username and password every time.

> > SSH Key Pair

1. **Private Key** – Stored securely on your computer and should never be shared.
2. **Public Key** – Added to your GitHub account for authentication.

> > Git Configuration
> > Set your Git username and email before working with repositories.

>>in-powershell
git config --global user.name "Your Username"
git config --global user.email "your_email@example.com"

>>Useful commands:

>>in-powershell
git --version
git config --global --list

> > Generating an SSH Key

>> in-powershell
ssh-keygen -t ed25519 -C "your_email@example.com"

> > Starting the SSH Agent (Windows PowerShell)

>> in-powershell
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519

> > Copying the Public Key (Windows)

>> in-powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub

Or copy it directly to the clipboard:

>> in-powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard

> > Adding SSH Key to GitHub
> > Go to **GitHub → Settings → SSH and GPG Keys → New SSH Key**, then paste your copied public key.

> > Testing the Connection

>> in-powershell
ssh -T git@github.com

> > Working with Repositories

Clone a repository using SSH:

>> in-powershell
git clone git@github.com:user/repository.git

>>Change an existing repository's remote URL to SSH:

>> in-powershell
git remote set-url origin git@github.com:user/repository.git


> > Git Branches
A branch lets you develop new features without affecting the main branch.

>> in-powershell
git branch
git checkout -b feature/branch_name

> > Key Takeaway
Learned how to securely connect GitHub using SSH keys, configure Git, manage repositories, and work with branches using Windows PowerShell.
