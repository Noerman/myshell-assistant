-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Guides](https://developer.android.com/guide)

# Cross device SDK

Stay organized with collections Save and categorize content based on your preferences.

The Cross device SDK makes it easier for developers to create apps that are compatible across multiple devices. The SDK simplifies the development of rich and engaging multi-device experiences by combining various connectivity technologies into one toolkit. Previously, developers needed to independently work with connectivity frameworks like Bluetooth and Wi-Fi to create multi-device experiences. Now, developers can focus on the most important parts of the user experience while the SDK handles these lower level technologies.

This SDK is part of our larger [multi-device development toolkit](https://developer.android.com/multi-device-development) that includes emulator support, profiling, and more. The Cross device SDK enables the following core functionality:

-   Device discovery and authorization
-   Secure connections and data transfers
-   Multi-device sessions

**Note:** For Developer Preview, the Cross device SDK only supports interactions between two devices at a time.

Some examples of applications and experiences that you can build using this SDK include multiplayer gaming, seamless switching between devices in productivity apps, and group food ordering.

When developing the Cross device SDK, we followed three basic principles to create an abstraction layer that safely and respectfully accelerates the development of multi-device apps and experiences. Those principles are:

-   Ubiquitous: The SDK should work on every device possible, starting with phones and tablets.
-   Modular: Developers should be able to mix the SDK with other solutions.
-   Empowering: The SDK does not restrict you to specific cross-device experiences, but rather allows you to build your own features and experiences.

## Use cases

**Note:** Developer Preview currently supports phone and tablet experiences. Additional devices are not supported in Developer Preview, but we hope to support them in future releases.

When discussing cross-device use cases, we consider two main categories: personal and communal experiences.

### Personal experiences

Personal experiences are built around a single user identity on multiple devices, such as mobile phones, watches, TVs, and/or cars. These experiences help users more effectively connect the various devices they own. For instance:

-   Complete a movie rental or purchase on your TV by using your phone to enter your form of payment.
-   Start reading a long article on your phone and finish reading it on your tablet without losing your place.

### Communal experiences

Communal experiences are enjoyed between a user and others around them. For example:

-   Share a map location as a passenger directly with your friend’s car.
-   Share your Sunday bike route with others that you’re biking with.
-   Collect items for a group food order without passing your phone around.
-   Take a group vote for the next TV show to watch together.

#### Media and other experiences

There are also multi-device experiences, such as continuous media controls and authentication, that could prompt discovering devices and passing data between participants. For these use cases, we have existing frameworks and SDKs that might be a better fit:

-   [Cast SDK](https://developers.google.com/cast) for media casting to other devices.
-   [Media sessions](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session#maintain-state) for continuous playback.
-   [Block Store](https://developers.google.com/identity/blockstore/android) for authentication.
-   [Companion Device Manager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing) for discovering and pairing companion devices such as fitness trackers or headphones.

Together with the Cross device SDK, these APIs and technologies allow you to build unique and seamless multi-device user experiences in your apps.

## Developer Preview limitations

As this is a Developer Preview version of the SDK, note the following:

-   The API surfaces are subject to change.
-   The Cross device SDK is NOT to be used in production applications.

Currently supported platforms and surfaces are limited to Android mobile and tablet devices.

We encourage you to share your feedback and suggestions. Please [submit bug reports here](https://issuetracker.google.com/issues/new?component=1205991&template=1706309).

## How it works

The Cross device SDK is a software abstraction layer that enables both platform-driven and developer-driven multi-device experiences by leveraging various wireless technologies such as Bluetooth, Wi-Fi, and ultra-wideband. This abstraction allows developers to focus on the most important parts of the user experience while the SDK handles underlying aspects of platform capabilities, device discovery, authentication, and compatibility.

!

**Figure 1**: Cross device SDK architecture.

For most application developers, we recommend using the Multi-Device Sessions API. This API allows app user experiences to be transferred to or shared with other devices. However, if you need more granularity or customization for your cross-device experiences, the standalone Device Discovery and Secure Connections APIs are available.

The Cross device SDK is open-source and will be available for different Android surfaces and non-Android ecosystem devices (ChromeOS, Windows, iOS). The goal of the SDK is to leverage existing technologies and platform capabilities while simplifying the development of multi-device experiences for app developers.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.