def main():
    print("Commands to add and upload a file to GitHub:")
    print("git status")
    print("git add path/to/file")
    print('git commit -m "Add file"')
    print("git push origin main")

    print("\nIf your branch is master instead of main:")
    print("git push origin master")

    print("\nIf this is a brand-new local repo:")
    print("git init")
    print("git add path/to/file")
    print('git commit -m "Add file"')
    print("git branch -M main")
    print("git remote add origin https://github.com/USERNAME/REPO.git")
    print("git push -u origin main")

    print("\nCheck the remote repo:")
    print("git remote -v")


if __name__ == "__main__":
    main()
