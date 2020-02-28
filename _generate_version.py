#!/usr/bin/env python
from __future__ import print_function
import git


def main():
    try:
        repo = git.Repo()
        print(repo)
    except git.exc.InvalidGitRepositoryError:
        print('No git repository is found, exit.')
    else:
        sha = repo.head.object.hexsha
        print(sha)


if __name__ == '__main__':
    main()
