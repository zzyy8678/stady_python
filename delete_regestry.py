import os
import requests


class RegistryHandler(object):
    get_repos_url = '/v2/_catalog'
    get_tags_url = '/v2/{repo}/tags/list'
    get_digests_url = '/v2/{repo}/manifests/{tag}'
    delete_digest_url = '/v2/{repo}/manifests/{digest}'

    def __init__(self, host):
        self.host = host

    def get_repos(self):
        url = f'{self.host}{self.get_repos_url}'
        res = requests.get(url).json()
        return res['repositories']

    def get_tags(self, repo):
        url = f'{self.host}{self.get_tags_url.format(repo=repo)}'
        res = requests.get(url).json()
        return res['tags']

    def get_digest(self, repo, tag):
        headers = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}
        url = f'{self.host}{self.get_digests_url.format(repo=repo, tag=tag)}'
        resp = requests.get(url, headers=headers)
        return resp.headers['Docker-Content-Digest']

    def delete_digest(self, repo, digest):
        url = f'{self.host}{self.delete_digest_url.format(repo=repo, digest=digest)}'
        requests.delete(url)


if __name__ == '__main__':
    rh = RegistryHandler('http://10.204.112.43:5001')
    repos = rh.get_repos()
    for repo in repos:
        tags = rh.get_tags(repo)
        if not tags:
            continue

        delete_tags = sorted(
            filter(lambda tag: '.' in tag, tags),
            key=lambda tag: ''.join([f'{int(n):04d}' for n in tag.split('.')])
        )[:-1]
        for tag in delete_tags:
            try:
                digest = rh.get_digest(repo, tag)
                rh.delete_digest(repo, digest)
            except Exception as e:
                print(f'{repo}:{tag} delete fail: {e}')

    os.system("docker exec `docker ps | grep registry | awk '{print $1}'` registry garbage-collect /etc/docker/registry/config.yml")
    os.system("systemcel restart docker `docker ps | grep registry | awk '{print $1}'`")

    # docker exec -it $ registry sh -c 'registry garbage-collect /etc/docker/registry/config.yml'
    # curl -I -H "Accept: application/vnd.docker.distribution.manifest.v2+json" 10.204.114.43:5001/v2/$ImageName/manifests/$tag
