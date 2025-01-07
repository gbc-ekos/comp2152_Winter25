# Lab 01
## Initializing repository and basic commits

```
git init
git status
git add .  
git commit -m "init"  
git branch -M master`
```
*Adding multiple remotes*  
*Bitbucket repo is private and serves as a personal storage*
```
git remote add bitbucket git@bitbucket.org:ekosgbc/comp2152.git
git remote add github git@github.com:gbc-ekos/comp2152_Winter25.git
git push -u bitbucket master
git push -u github master
```