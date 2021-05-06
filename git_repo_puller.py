#!/usr/bin/env python
"""
This script MUST not throw errors. If it does, the pod will fail to start.
"""
import os
import argparse
import urllib
import git


def pull_repos(repos):
    """
    Try to get everything in the manifest. Allow single entries to fail.
    Don't overwrite anything or throw any errors.
    """
    for repo_url in repos:
        try:
            purl = urllib.parse.urlparse(repo_url)
            repo_name = os.path.basename(purl.path)
            print(f'Cloning repo: {repo_url} into {repo_name}')
            git.Repo.clone_from(repo_url, repo_name)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('repos', nargs='+',
                        help='github repos to pull on notebook startup')
    args = parser.parse_args()

    pull_repos(args.repos)
