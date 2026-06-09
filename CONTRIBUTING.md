<!--
  - SPDX-FileCopyrightText: 2017 Nextcloud GmbH and Nextcloud contributors
  - SPDX-FileCopyrightText: 2013 Nextcloud GmbH and Nextcloud contributors
  - SPDX-License-Identifier: GPL-2.0-or-later
-->
## Contributing to Source Code

Thanks for wanting to contribute source code to Nextcloud. That's great!

We ask that you follow our [Code of Conduct](https://nextcloud.com/code-of-conduct/).

Please read the [Contribution Guide](https://nextcloud.com/contribute/) to get 
started.

## AI-assisted contributions

Nextcloud allows contributions made with the help of AI tools. You are the author of everything you submit - AI assistance does not change that responsibility.

* **Disclosure:** Declare AI tool use in the PR description and add an `Assisted-by: AGENT_NAME:MODEL_VERSION` git trailer to each affected commit.

* **Accountability:** You must be able to explain, defend, and modify every line you submit. If a reviewer asks why something works a certain way, "the AI wrote it" is not an answer.

* **Communication:** PR descriptions, review comments, and issue reports must be written in your own words. This applies throughout the review process - passing reviewer feedback to an AI and posting whatever comes out is not acceptable.

* **Quality:** AI output must be quality assured by the human, i.e. reviewed, cleaned up, and tested before submission. New features must be tested on a live instance by you, not by an agent. Code that has never been executed, or that shifts debugging work onto maintainers, will not be accepted.
s
* **Licensing:** Ensure AI-generated code contains no material incompatible with the license of the repository you are contributing to.

For the full policy including autonomous agent rules, security reports, and beginner issues, read the [AI Contribution Policy](https://github.com/nextcloud/.github/blob/master/AI_POLICY.md).

## Sign your work

We use the Developer Certificate of Origin (DCO) as an additional safeguard
for the Nextcloud project. This is a well established and widely used
mechanism to assure contributors have confirmed their right to license
their contribution under the project's license.
Please read [contribute/developer-certificate-of-origin](https://github.com/nextcloud/server/blob/master/contribute/developer-certificate-of-origin).
If you can certify it, then just add a line to every git commit message:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```

If you set your `user.name` and `user.email` git configs, you can sign your
commit automatically with `git commit -s`. You can also use git [aliases](https://git-scm.com/book/tr/v2/Git-Basics-Git-Aliases)
like `git config --global alias.ci 'commit -s'`. Now you can commit with
`git ci` and the commit will be signed.

## Apply a license

In case you are not sure how to add or update the license header correctly please have a look at [contribute/HowToApplyALicense.md](https://github.com/nextcloud/server/blob/master/contribute/HowToApplyALicense.md).

## Translations

Please submit translations via [Transifex](https://explore.transifex.com/nextcloud/).
