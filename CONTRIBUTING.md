## Contributing

I am open to, and grateful for, any contributions made by the community to help develop this project. Please go through this document once completely before you contribute or open a pull request.

## How to Contribute

- Take a look at the Existing [Issues](https://github.com/nightmare-tech/PWD_Vault/issues) or create your own Issues!
- Fork the Repo and create a Branch for any Issue that you are working upon.
- Create a Pull Request which will be promptly reviewed and suggestions would be added to improve it.
- Add Screenshots to help us know what this is all about.

## How to make a Pull Request

**1.** Fork the <a href="https://github.com/nightmare-tech/PWD_Vault">repository</a> by clicking fork symbol at the top right corner.

**2.** Clone the forked repository.
```
   git clone https://github.com/<your-username>/PWD_Vault
```

**3.** Navigate to the project directory.
```
   cd PWD_Vault
```

**4.** Set upstream command:

```
git remote add upstream https://github.com/nightmare-tech/PWD_Vault
```

**5.** Create a new branch:
```
   git checkout -b <Add your branch name>
```

**6.** Sync your fork or your local repository with the origin repository:

```
git fetch upstream
```

```
git merge upstream/main
```

**6.** Make necessary changes and commit those changes:

Add all the changes to the staging area
```
git add --a
```

Now commit those changes using the `git commit` command:

```
git commit -m "commit message"
```

**7.** Push changes to GitHub: 

Push your changes using the command `git push`:

```
git push origin -u <your-branch-name>
```

replacing `<your-branch-name>` with the name of the branch you created earlier.


**8.** Make a Pull Request: 

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

Now submit the pull request.

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll encounter often as a contributor!
