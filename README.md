## Texascale CMS

https://texascale.org/

## Quick Start

Follow [Core CMS Template's "Start Project"][core-cms-template-start].

## Documentation

> [!TIP]
> This project is built as a customization of a TACC <abbr title="Content Management System">CMS</abbr> website. To manage this project's CMS, reference [Core-CMS-Template Docs][core-cms-template-docs]. To develop this project's custom code, keep reading.

### Styles

Learn about [Texascale Stylesheets](./cms/src/taccsite_custom/texascale_cms/static/texascale_cms/css/README.md).

> [!IMPORTANT]
> If you change a `.postcss` file,  run **`npm run build`**.

### Deploy

> [!IMPORTANT]
> Initial deploy to [production site](https://texascale.org/) requires manual updates.
>
> In certain snippets, replace `css/build/` with  `css/`:
>
> * [Snippet #21](https://texascale.org/admin/djangocms_snippet/snippet/21/change/) (ref: [staging](https://pprd.texascale.tacc.utexas.edu/admin/djangocms_snippet/snippet/21/change/))
> * [Snippet #35](https://texascale.org/admin/djangocms_snippet/snippet/35/change/) (ref: [staging](https://pprd.texascale.tacc.utexas.edu/admin/djangocms_snippet/snippet/35/change/))
> * [Snippet #46](https://texascale.org/admin/djangocms_snippet/snippet/46/change/) (ref: [staging](https://pprd.texascale.tacc.utexas.edu/admin/djangocms_snippet/snippet/46/change/))
> * [Snippet #47](https://texascale.org/admin/djangocms_snippet/snippet/47/change/) (ref: [staging](https://pprd.texascale.tacc.utexas.edu/admin/djangocms_snippet/snippet/47/change/))
>
> <details><summary>Why?</summary>
> This repository builds a different CMS image than has previously been deployed to production. Certain changes must be made on production to accommodate this new image.
> </details>

<!-- Link Aliases -->

[Core CMS]: https://github.com/TACC/Core-CMS
[Core CMS Template]: https://github.com/TACC/Core-CMS-Template
[Core Portal Deployments]: https://github.com/TACC/Core-Portal-Deployments

[core-cms-template-setup]: https://github.com/TACC/Core-CMS-Template/blob/v0.3.0/docs/create-project.md#set-up-project
[core-cms-template-start]: https://github.com/TACC/Core-CMS-Template/blob/v0.3.0/docs/start-project.md#start-project
[core-cms-template-docs]: https://github.com/TACC/Core-CMS-Template/blob/v0.3.0/docs/README.md#tacc-custom-cms
