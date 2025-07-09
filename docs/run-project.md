# Run Project

## Individual Projects

Read the `README.md` of the relevant project repository.

## Multiple Projects

> [!NOTE]
> By default, multiple projects can not be run simultaneously.[^1]

To stop one project, and run another:

1. Cancel any active `make start` output i.e. press <kbd>control</kbd> + <kbd>C</kbd>.

2. Take down one project.

    > [!NOTE]
    > This remove containers, but not volumes e.g. database.

    ```sh
    cd custom_project_1
    make stop
    ```

3. Start another project.

    ```sh
    cd custom_project_2
    make start
    ```

[^1]: If you want to run multiple projects simultaneously, see [Simultaneous Projects](#simultaneous-projects).

## Simultaneous Projects

> [!CAUTION]
> With these instructions, you will **not** be able to use the database (**nor** internal search index) of an already set up custom project (i.e. its local volumes).[^2]

To run multiple projects simultaneously:

1. Stop and take down any started projects (i.e. [Multiple Projects](#multiple-projects) step 2).
2. Create a custom `docker-compose.dev.yml` in your project.
3. Replace all instances of the text `core_cms` with custom name e.g. `custom_project_name_cms`.

[^2]: Advanced adaptation of these instructions may support retaining database access, et cetera.
