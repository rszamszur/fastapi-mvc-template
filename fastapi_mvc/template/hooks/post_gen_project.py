"""Fastapi-mvc cookiecutter template post_gen_project hook."""
import os


def remove(paths):
    """Remove directories and files provided in paths list.

    Args:
        paths(list): List of relative paths to remove.

    """
    pwd = os.getcwd()

    for path in paths:
        path = os.path.join(pwd, path)

        if path and os.path.exists(path):
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.remove(path)


def set_gh_actions():
    """Remove GitHub actions if not enabled."""
    if "{{ cookiecutter.github_actions }}" != "yes":
        remove([".github"])


def set_vagrantfile():
    """Remove Vagrantfile if not enabled."""
    if "{{ cookiecutter.vagrantfile }}" != "yes":
        remove(["Vagrantfile", ".github/workflows/integration.yml"])


def set_aiohttp():
    """Remove aiohttp utility implementation and tests if not enabled."""
    if "{{ cookiecutter.aiohttp }}" != "yes":
        remove([
            "{{ cookiecutter.package_name }}/app/utils/aiohttp_client.py",
            "tests/unit/app/utils/test_aiohttp_client.py"
        ])


def set_helm():
    """Remove Helm chart if not enabled."""
    if "{{ cookiecutter.helm }}" != "yes":
        remove([
            "charts",
            ".github/workflows/integration.yml",
            "build/dev-env.sh"
        ])


def set_redis():
    """Remove Redis utility implementation and tests if not enabled."""
    if "{{ cookiecutter.redis }}" != "yes":
        remove([
            "manifests",
            "{{ cookiecutter.package_name }}/app/utils/redis.py"
        ])


if __name__ == "__main__":
    set_gh_actions()
    set_vagrantfile()
    set_aiohttp()
    set_helm()
    set_redis()
