# Start Project

1. Start [Docker] Containers:

    ```sh
    cd cms
    make start
    ```

> [!NOTE]
> If this is an initial or new project, keep reading. Otherwise, your project website is running locally again.

2. Configure [Django] Application:

    Create a `/cms/src/taccsite_cms/settings_local.py` with content from [Core-CMS `settings_local.example.py`](https://github.com/TACC/Core-CMS/blob/main/taccsite_cms/settings_local.example.py).

> [!NOTE]
> If your project uses a `secrets.py` to connect to a remote CMS database, stop reading. Follow instructions specific to your project.

3. Prepare [Django] Application:

    ```sh
    docker exec -it core_cms /bin/bash
    # This opens a command prompt within the container.
    ```

    (Run these commands within the container.)

    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    # To use default "Username" and skip "Email address", press Enter at both prompts.
    # At "Password" prompts, you may use an easy-to-remember password.
    python manage.py collectstatic --no-input
    ```

    (Exit the shell and container e.g. `exit()` then `exit`.)

4. Enter [Django CMS]:
    1. Open http://localhost:8000/.
    2. Login with the credentials you defined in step 2.
    3. Create one CMS page.\
        (With "New page" highlighted, click "Next" button.)
        - This page will automatically be your local homepage.

> [!IMPORTANT]
> A new local CMS will be empty. It will **not** have content from staging nor production. To have that, follow and adapt instructions to [copy a database](https://tacc-main.atlassian.net/wiki/x/GwBJAg).

> [!IMPORTANT]
> A new custom CMS may or may not include or integrate with an instance of [Core Portal]. Follow instructions specific to your project.

> [!TIP]
> For CMS user instructions, read TACC's [Django CMS User Guide].


<!-- Link Aliases -->

[Docker]: https://docs.docker.com/get-docker/
[Django]: https://www.djangoproject.com/
[Django CMS]: https://www.django-cms.org/

[Django CMS User Guide]: https://tacc-main.atlassian.net/wiki/x/phdv

[Core Portal]: https://github.com/TACC/Core-Portal
