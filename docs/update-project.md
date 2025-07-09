# Update Project

To update an existing CMS instance.

## New Major CMS Version

1. Follow [Upgrade Project](https://github.com/TACC/Core-CMS/blob/main/docs/upgrade-project.md).
2. Follow [for New Branch or CMS Version](#for-new-branch-or-cms-version).

## for New Branch or CMS Version

1. If CMS Docker files changed, rebuild Docker Containers:

    ```sh
    cd customproject_cms
    make stop
    make build
    make start
    ```

2. If static assets or database models changed[^1], update the Django app:

    ```sh
    docker exec -it core_cms /bin/bash
    # That opens a command prompt within the container.
        python manage.py migrate
        python manage.py collectstatic --no-input
        # If the project has no new/changed assets,
        # then expect output of "0 static files […]"
    ```

[^1]: Pertinent changes are those in the Core CMS or the custom project. Changes to external assets or databases are not pertinent.
