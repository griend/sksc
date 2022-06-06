"""
Update all Git Repos in ~/Projects.
If a repo has changed locally, a warning is printed instead. 
"""


import logging
import os
from pathlib import Path

from git import Repo


def update(dir: str) -> None:
    logger = logging.getLogger(__name__)

    logger.debug('update() - Started')

    repo = Repo(dir)

    if repo.is_dirty():
        logger.warning(f'update() - {dir} is dirty')
    else:
        logger.debug('update() - pulling')
        repo.remotes.origin.pull()
        logger.info(f'update() - {dir} pulled')

    logger.debug('update() - Finished')


def main() -> None:
    logger = logging.getLogger(__name__)

    try:
        logger.info('main() - Started')

        prj = os.path.join(Path.home(), 'Projects')

        for name in os.listdir(prj):
            dir = os.path.join(prj, name)
            dot = os.path.join(prj, name, '.git')

            if os.path.isdir(dot):
                update(dir)

        logger.info('main() - Finished')
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    main()
