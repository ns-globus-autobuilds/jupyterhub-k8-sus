#!/usr/bin/env python
"""
This script MUST not throw errors. If it does, the pod will fail to start.
"""
import os
import sys
import argparse
import urllib
import requests
import git


def try_connect(url, max_connection_attempts):
    """
    AWS Calico currently has a problem where fetching a notebook on a first time try Fails.
    This attempts to wait until a url can be successfully fethed before failing with an error.
    """
    for tries in range(max_connection_attempts):
        try:
            requests.head(url, timeout=1)
            return True
        except requests.exceptions.Timeout:
            print(f'Failed to HEAD {url}, retrying {tries + 1}/{max_connection_attempts}...')
    return False


def pull_repos(repos, retries=5, raise_exc=False):
    """
    Try to get everything in the manifest. Allow single entries to fail.
    Don't overwrite anything or throw any errors.
    """
    errors = 0
    for repo_url in repos:
        try:
            if not try_connect(repo_url, retries):
                print(f'Failed to connect to {repo_url}')
                errors += 1
                continue
            purl = urllib.parse.urlparse(repo_url)
            repo_name = os.path.basename(purl.path)
            print(f'Cloning repo: {repo_url} into {repo_name}')
            git.Repo.clone_from(repo_url, repo_name)
        except Exception as e:
            print(str(e))
            errors += 1

    if raise_exc and errors:
        raise Exception(f'Error cloning repos')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('repos', nargs='+',
                        help='github repos to pull on notebook startup')
    parser.add_argument('--retries', type=int, default=5,
                        help='Retries for fetching repo before giving up')
    parser.add_argument('--raise-exc', action='store_true', default=False,
                        help='Return non-zero on failure. ')
    args = parser.parse_args()

    try:
        pull_repos(args.repos, retries=args.retries, raise_exc=args.raise_exc)
    except Exception as e:
        print(e)
        sys.exit(1)
