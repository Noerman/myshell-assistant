-   [Android Developers](https://developer.android.com/)
-   [Modern Android](https://developer.android.com/modern-android-development)
-   [Jetpack](https://developer.android.com/jetpack)
-   [Libraries](https://developer.android.com/jetpack/androidx/explorer)

# AndroidX releases

Stay organized with collections Save and categorize content based on your preferences.

---

Overview | | | | |

Jetpack libraries ship separately from the Android OS, so updates to the libraries can happen independently and more frequently.

The libraries follow [strict semantic versioning](https://semver.org/) for binary compatibility with an added inter-version sequence of pre-release revisions. A version string (like `1.0.1-beta02`) contains three numbers representing major, minor, and bugfix levels. Pre-release versions also have a suffix that specifies the pre-release stage (alpha, beta, release candidate) and revision number (01, 02, and so on).

**Please note** that `androidx` libraries are encouraged, but not required, to preserve source compatibility across minor versions. The reason being a major version update would force all artifacts that depend on the previous major version to be explicitly migrated, which would disrupt the workflow of developers.

Every version of a library moves through three pre-release stages on its way to becoming a stable release. The criteria for each pre-release stage is:

**Alpha**

-   Alpha releases are functionally stable, but may not be feature-complete.
-   While a release is in alpha, APIs may be added, removed, or changed.

**Beta**

-   Beta releases are functionally stable and have a feature-complete API surface.
-   They are ready for production use but may contain bugs.
-   A beta release cannot use experimental compiler features (such as `@UseExperimental`).
-   Dependencies on other libraries must be beta, rc, or stable versions. No alpha dependencies are allowed.

**Release Candidate (RC)**

-   A release candidate is a prospective stable release.
-   It may contain critical last-minute fixes.
-   Its API surface is final.
-   Dependencies on other libraries must be rc or stable versions only.

A library can have multiple versions at the same time. Each version has a different release stage. For example, while the stable release of `androidx.activity` could be `1.0.0`, there might also be a `1.1.0-beta02` release as well as a `2.0.0-alpha01` release.

Use this page to learn of the latest updates to the libraries.

The  lists the libraries that have recently changed. Google's [Maven repository](https://dl.google.com/dl/android/maven2/index.html) shows the complete version history.

Use the table below to view the most recent stable and preview versions of every AndroidX library. The links on each row take you to the library's release notes. In the release notes you'll find:

-   The chronological history of all the releases.
-   A code snippet with the default Gradle dependency declarations to use the artifacts.
-   Links to the Kotlin and Java reference pages for the packages in each artifact.

**Note:** Jetpack libraries don't send any user data to a backend service of any kind. This means that integrating a Jetpack library into your app has no impact on your app's  in the Play Console.

### Jetpack libraries

**Caution:** AndroidX libraries are moving to a default minimum supported Android API level 21 (previously 19) starting with releases in April, 2024. If you are currently supporting a lower minSdkVersion, we recommend bumping up to 21 and cleaning up any code to support prior versions.

Some AndroidX libraries, like camera, have multiple artifacts that are maintained separately. These libraries are marked with an asterisk (\*). See the release notes to view the version updates for all of the artifacts.

| Maven Group ID | Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
| --- | --- | --- | --- | --- | --- |
|  | April 17, 2024 |  | \- | \- | \- |
|  | March 8, 2023 | \- | \- | \- |  |
|  | April 17, 2024 |  | \- |  | \- |
|  | July 26, 2023 |  | \- | \- |  |
|  | May 24, 2023 | \- | \- | \- |  |
|  | February 22, 2023 |  | \- | \- | \- |
|  | October 5, 2022 |  | \- | \- |  |
|  | May 24, 2023 |  | \- |  |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | September 21, 2022 |  | \- | \- |  |
|  | November 29, 2023 | \- | \- | \- |  |
|  | March 6, 2024 |  | \- | \- | \- |
|  | April 17, 2024 |  |  | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | September 21, 2018 |  | \- | \- | \- |
|  | January 24, 2024 |  | \- | \- | \- |
|  | April 17, 2024 |  | \- | \- | \- |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- | \- |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | March 20, 2024 |  | \- | \- |  |
|  | October 4, 2023 |  | \- | \- |  |
|  | September 21, 2018 |  | \- | \- | \- |
|  | October 4, 2023 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- | \- |
|  | January 24, 2024 | \- | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | September 21, 2018 |  | \- | \- | \- |
|  | September 21, 2022 |  | \- | \- |  |
|  | September 5, 2019 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- | \- |
|  | August 18, 2021 |  | \- | \- |  |
|  | May 11, 2022 |  | \- | \- | \- |
|  | March 22, 2023 |  | \- | \- | \- |
|  | December 4, 2019 |  | \- | \- |  |
|  | January 27, 2021 |  | \- | \- |  |
|  | December 13, 2023 |  | \- | \- |  |
|  | January 13, 2021 |  | \- | \- | \- |
|  | December 13, 2023 |  | \- | \- | \- |
|  | April 17, 2024 |  |  | \- |  |
|  | April 17, 2024 |  | \- | \- | \- |
|  | April 17, 2024 |  | \- |  | \- |
|  | April 17, 2024 | \- |  | \- | \- |
|  | May 24, 2023 |  | \- |  | \- |
|  | April 3, 2024 | \- |  | \- |  |
|  | January 10, 2024 | \- | \- | \- |  |
|  | July 26, 2023 | \- | \- | \- |  |
|  | February 21, 2024 |  | \- | \- | \- |
|  | September 20, 2023 | \- | \- |  | \- |
|  | September 21, 2018 |  | \- | \- | \- |
|  | November 1, 2023 | \- | \- |  | \- |
|  | September 2, 2020 | \- | \- |  | \- |
|  | November 15, 2023 |  |  | \- |  |
|  | September 21, 2018 |  | \- | \- | \- |
|  | April 17, 2024 |  | \- |  | \- |
|  | February 21, 2024 | \- | \- | \- |  |
|  | October 9, 2019 |  | \- | \- | \- |
|  | January 12, 2022 |  | \- | \- | \- |
|  | November 29, 2023 |  | \- | \- | \- |
|  | January 10, 2024 |  | \- | \- | \- |
|  | April 12, 2024 |  | \- | \- |  |
|  | March 20, 2024 |  | \- | \- | \- |
|  | December 17, 2018 |  | \- | \- | \- |
|  | January 10, 2024 | \- | \- |  | \- |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 3, 2024 |  | \- |  | \- |
|  | September 21, 2018 |  | \- | \- | \- |
|  | September 21, 2018 |  | \- | \- | \- |
|  | July 26, 2023 |  | \- | \- | \- |
|  | October 28, 2020 | \- | \- |  | \- |
|  | November 15, 2023 | \- | \- | \- |  |
|  | April 17, 2024 | \- | \- |  | \- |
|  | August 9, 2023 | \- | \- | \- |  |
|  | March 6, 2024 | \- | \- | \- |  |
|  | March 20, 2024 | \- | \- | \- |  |
|  | October 18, 2023 | \- | \- | \- |  |
|  | February 7, 2024 |  | \- | \- |  |
|  | September 21, 2018 |  | \- | \- | \- |
|  | October 18, 2023 |  | \- | \- |  |
|  | May 7, 2019 |  | \- | \- | \- |
|  | January 26, 2022 |  | \- | \- | \- |
|  | November 29, 2023 |  | \- | \- | \- |
|  | March 22, 2023 |  | \- | \- | \- |
|  | March 6, 2024 |  | \- | \- |  |
|  | October 5, 2022 |  | \- | \- | \- |
|  | January 13, 2021 | \- | \- | \- |  |
|  | January 26, 2022 |  | \- | \- | \- |
|  | January 11, 2023 |  | \- | \- |  |
|  | October 18, 2023 |  | \- | \- | \- |
|  | July 22, 2020 |  | \- | \- |  |
|  | February 29, 2024 |  | \- | \- |  |
|  | February 21, 2024 |  | \- | \- | \- |
|  | March 23, 2022 | \- | \- | \- |  |
|  | November 29, 2023 |  | \- | \- |  |
|  | April 17, 2024 |  |  | \- | \- |
|  | October 4, 2023 | \- | \- | \- |  |
|  | August 19, 2020 | \- | \- | \- |  |
|  | April 20, 2022 |  | \- |  | \- |
|  | January 10, 2024 |  | \- | \- | \- |
|  | September 15, 2021 |  | \- | \- |  |
|  | May 24, 2023 |  | \- |  | \- |
|  | January 10, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | March 6, 2024 |  | \- | \- |  |
|  | March 6, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  | \- | \- |  |
|  | April 17, 2024 |  |  | \- |  |
|  | April 3, 2024 |  | \- |  | \- |
|  | June 7, 2023 |  | \- | \- | \- |
|  | April 17, 2024 |  | \- | \- |  |

(\*) This library has multiple artifacts. See its release notes for more information.  

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2024-04-18 UTC.