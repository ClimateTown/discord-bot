### it's been months and we still haven't come up with a usecase for this Discord bot. Archiving until this has a purpose... (if you have an idea, post an issue here or tag  `@Comptrollers` in Discord)

<p align="center">
<a href="https://hub.climatetownproductions.com">
<img width="200" src="https://placehold.co/400">
</a>
</p>

[![YouTube subs](https://img.shields.io/youtube/channel/subscribers/UCuVLG9pThvBABcYCm7pkNkA?label=ClimateTown&style=for-the-badge)](https://www.youtube.com/@ClimateTown)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/ClimateTown)

[![All Contributors](https://img.shields.io/github/all-contributors/ClimateTown/discord-bot?color=ee8449&style=flat-square)](#contributors)

---

This is the code that runs our custom `<bot name>` bot in the Climate Town Discord server!

## Contributing

Contributions welcome! Suggest features for the bot by [posting an issue](https://github.com/ClimateTown/discord-bot/issues), or by messaging in `🔨server-suggestion-box`.

Note that bot feature suggestions are approved/dis-approved at the discretion of the moderators (aka. Comptrollers) of the server\*.

If you want to contribute code, thank you! Head over to the issues section and find an issue you're interested in (voice your interest so other developers know what you're up to). Then go ahead and create your PR, get it reviewed, and merge it in!

\* Note: Approved features will likely be in line with the limitations of the existing infrastructure. See the [infrastructure](#infrastructure) section for more details on where the code is being run, and resources the machine has. If you have an amazing feature that would provide benefit to users, this may warrant us upgrading infrastructure to accommodate 😉.

## Development setup

This repo uses Python.

- [install Python](https://www.python.org/downloads/) if you haven't already (minimum version 3.9)
- create a virtual environment, then activate it (optional, but recommended)
  - `python -m venv venv`
  - activate the environment using either:
    - `source venv/bin/activate` (Linux/MacOS)
    - `venv\Scripts\activate.bat` (Windows)
- `pip install -r requirements.txt`
- OPTIONAL: `pre-commit install`

This codebase uses [pre-commit](https://pre-commit.com/) and [pre-commit CI](https://pre-commit.ci/) to run linting on code, format Python code, and generally have help with code quality. `pre-commit install` is an optional step in case you also want to have pre-commit run locally.

To run pre-commit manually (without making a commit), use `pre-commit run --all-files`. If you want to stop using pre-commit locally, just do `pre-commit uninstall`.

### Adding Python dependencies

This codebase uses [`pip-tools`](https://pypi.org/project/pip-tools/) to manage dependencies. If you add a new dependency, you can add it to `requirements.in` and run `pip-compile` to update `requirements.txt`. To update your environment run `pip-sync`.

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
