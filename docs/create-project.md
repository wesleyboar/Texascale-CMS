# Create Project

## Table of Contents

- [Create Project](#create-project)
- [Set Up Project](#set-up-project)
- [Configure Build Action](#configure-build-action)
- [Create Custom App](#create-custom-app)

## Create Project

1. [Create a repository from our template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) "[Core CMS Template]".
2. Follow the steps in the `README.md` of the new repository.
3. Return to this doc as directed or for further customization.

## Set Up Project

1. [Remove Excess Content](#remove-excess-content)
2. [Customize Website Settings](#customize-website-settings)
3. [Configure Build Action](#configure-build-action)
4. Consider other changes, e.g.
    - [Create a Custom App](#create-a-custom-app)

### Remove Excess Content

> **Note**
> [Core CMS] supports standard TACC apps, URLs, and static asset directories. Consider its capabilities before creating something new.

| <u>If</u> Project Does Not Need: | <u>Then</u> Delete: |
| - | - |
| additional apps | the directory `apps/`<br />the `COPY /src/apps /code/taccsite_cms/apps` in `Dockerfile` |
| URLs for custom apps | `urls_custom.py` |
| custom code | `custom_app_settings.py` |

### Customize Website Settings

| Intent | File to Update |
| - | - |
| Test | `/cms/src/taccsite_cms/settings_custom.py` |
| Commit | [TACC/Core-Portal-Deployments][Core Portal Deployments]:`/project_dir/camino/settings_custom.py` |

To know what settings are available, see [TACC/Core-CMS:`/taccsite_cms/settings.py`](https://github.com/TACC/Core-CMS/blob/main/taccsite_cms/settings.py).

The settings usually edited are `PORTAL_LOGO` and `..._BRANDING`.

### Configure Build Action

1. Get `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` from [Stache secret](https://stache.utexas.edu/entry/fcf7c3b8029c98f8e8c16d9f7e0e81eb).
2. [Create repository secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) for `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`.

## Create Custom App

- Update `custom_app_settings.py` with pertinent content from [TACC/Core-CMS:`/taccsite_cms/custom_app_settings.example.py`](https://github.com/TACC/Core-CMS/blob/1d88c35/taccsite_cms/custom_app_settings.example.py).
- Update `urls_custom.py` with pertinent content from [TACC/Core-CMS:`/taccsite_cms/urls_custom.example.py`](https://github.com/TACC/Core-CMS/blob/1d88c35/taccsite_cms/urls_custom.example.py).


<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core CMS Template]: https://github.com/TACC/Core-CMS-Template
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments
