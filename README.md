<p align="center">
<a href="https://hub.climatetownproductions.com">
<img width="200" src="./spud.png">
</a>
</p>

[![YouTube subs](https://img.shields.io/youtube/channel/subscribers/UCuVLG9pThvBABcYCm7pkNkA?label=ClimateTown&style=for-the-badge)](https://www.youtube.com/@ClimateTown)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/ClimateTown)

[![All Contributors](https://img.shields.io/github/all-contributors/ClimateTown/discord-bot?color=ee8449&style=flat-square)](#contributors)

---

This is the code that runs our friendly custom bot (their name is Spud) in the Climate Town Discord server!

## Contributing

Contributions welcome! Suggest features for the bot by [posting an issue](https://github.com/ClimateTown/discord-bot/issues/new/choose), or by messaging in `🔨server-suggestion-box`.

Note that bot feature suggestions are approved/dis-approved at the discretion of the moderators (aka. Comptrollers) of the server\*.

If you want to contribute code, thank you! Head over to the issues section and find an issue you're interested in (voice your interest so other developers know what you're up to). Then go ahead and create your PR, get it reviewed, and merge it in!

\* Note: Approved features will likely be in line with the limitations of the existing infrastructure. See the [infrastructure](#infrastructure) section for more details on where the code is being run, and resources the machine has. If you have an amazing feature that would provide benefit to users, this may warrant us upgrading infrastructure to accommodate 😉.

## Development setup


This repo uses Python and [uv](https://github.com/astral-sh/uv) for dependency management.


- [Install uv](https://github.com/astral-sh/uv#installation) if you haven't already
- To set up the project, run:
  - `uv venv` (creates a virtual environment)
  - `uv run ...` to run a command in the uv environment

This codebase uses [pre-commit](https://pre-commit.com/) and [pre-commit CI](https://pre-commit.ci/) to run linting on code, format Python code, and generally help with code quality. If you (optionally) want to run pre-commit locally, install it (e.g., via brew) then you can use the following commands:

- `pre-commit install` to install the hooks
- `pre-commit uninstall` to uninstall the hooks
- `pre-commit run --all-files` to run pre-commit manually (without making a commit)

### Adding Python dependencies

```
uv add pacakge_name
```

This will update your environment and the necessary config files with the new dependency.

## Infrastructure

Currently the bot is running in a virtual machine (`e2-micro`, see the specs [here](https://cloud.google.com/compute/docs/general-purpose-machines#e2-shared-core)) on Google Cloud Platform (GCP) as part of their [free tier](https://cloud.google.com/free/docs/free-cloud-features#compute).

As such, we are keeping things to text interactions (no image/video processing), and no database for the time-being.

_Note we will likely move to a greener platform if we exceed GCP's free tier. Let us know in `🔨server-suggestion-box` if you have suggestions for cloud providers._

## ✨Contributors

Thanks go to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification. Contributions of any kind are, again, welcome!
