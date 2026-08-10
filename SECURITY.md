# Security Policy

## Supported Versions

Only the latest release of `names_generator` receives fixes. If you are pinned to an
older release, please upgrade before reporting an issue.

## Reporting a Vulnerability

Please report suspected vulnerabilities privately using GitHub's
[private vulnerability reporting](https://github.com/glentner/names_generator/security/advisories/new)
rather than opening a public issue. If that is unavailable to you, email
`glentner@purdue.edu` and allow a few days for a response.

Please do not include exploit details in a public issue, pull request, or discussion
thread until a fix has been released.

## Release Integrity

Releases are published to [PyPI](https://pypi.org/project/names_generator) exclusively by
the `publish` GitHub Actions workflow in this repository:

- Publishing uses [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
  (short-lived OIDC credentials). There is no long-lived PyPI API token stored in this
  repository, so there is no token to steal or leak.
- The publish job is gated on the protected `pypi` environment and requires manual
  approval before it can run.
- Distributions are built from a tagged commit and uploaded with
  [PEP 740 attestations](https://peps.python.org/pep-0740/), which you can verify against
  this repository.
- All third-party GitHub Actions are pinned to full commit SHAs.

If you ever see a release on PyPI that does not have a corresponding tag and workflow run
in this repository, treat it as a compromise and report it immediately.

## Social Engineering

This project is small, stable, and deliberately low-churn. Maintainers will **never**:

- ask you for credentials, API tokens, or recovery codes;
- ask you to install or run an unpublished build "to test something";
- add a maintainer or transfer ownership over email, chat, or a GitHub issue.

Requests along those lines are not legitimate, regardless of who they appear to come from.

Note also that the name listings are **frozen upstream** (see
[moby/moby#43210](https://github.com/moby/moby/pull/43210)) and therefore frozen here.
Pull requests that add names will be closed. Changes to `names.py` are only accepted when
they bring this port back in sync with the upstream Moby listing.
