-   [Android Developers](https://developer.android.com/)
-   [Essentials](https://developer.android.com/get-started)
-   [Health & fitness dev center](https://developer.android.com/health-and-fitness)
-   [Guides](https://developer.android.com/health-and-fitness/guides)

# Get started with health on Android

Stay organized with collections Save and categorize content based on your preferences.

Android Health provides the following APIs to create health and fitness apps across form factors:  and . You can use one or both for your app experience.

This developer center includes guidance for using both APIs, and points to additional resources from across Android to help you build health and fitness apps.

## Read and write on-device health and fitness data using Health Connect

 is an Android platform that allows health and fitness apps to store and share the same on-device data, within a unified ecosystem. It also offers a single place for users to control which apps can read and write health and fitness data. Health Connect supports reading and writing over 50 different data types, from cycling speed to body temperature.

You might be familiar with the Google Fit Android API, which supports many fitness-related actions such as reading near-time and historic data and recording activities. The Google Fit Android API has been [marked as deprecated](https://developers.google.com/fit/android). Many of the actions you can perform with the Google Fit Android API can be done with Health Connect. If your app uses the Google Fit Android API, consult the  to learn about alternatives for maintaining your app's capabilities. If you're building a new app, we recommend you use Health Connect.

## Access high-quality sensor data with Health Services on Wear OS

 is an API that acts as an intermediary to the various sensors and related algorithms on Wear OS devices. The API provides apps with high-quality data related to activity, exercise, and health, in a battery-efficient way. Health Services is consistent across devices running Wear OS 3 or higher, meaning you only need to write your app once, and Health Services takes care of ensuring the app performs the same, regardless of the device.

## Android Health across devices

**Health Connect** is only available on Android mobile devices. However, if you have other data sources connected to your mobile app, such as a wearable, you can use your mobile app to facilitate the data transfer from the wearable to Health Connect and correspondingly from Health Connect to the wearable.

**Note:** Health Connect is not well-suited for providing live data, but rather storing and unifying data across apps and devices.

At this time, **Health Services** is only available for Wear OS devices running Wear OS 3 or higher. For all other devices, including phones, you should consult the documentation for .

 and [Bluetooth connectivity](https://developer.android.com/guide/topics/connectivity/bluetooth) are additional options to connect companion devices that don't run Wear OS.

To plan out which APIs to use, you should consult the following data types guides to understand what data you could potentially read from Health Connect and what data you could use Health Services to read from Wear OS devices:

The most complete multidevice experiences use both Health Services and Health Connect to offer the most value for users.

**Note:** In order to read a particular data type from Health Connect back to your app, your user must have at least one app on-device that is writing that particular data type. For example, if you want to use heart rate in your mobile app and your app doesn't already measure heart rate, you need to rely on another app writing heart rate values to the Health Connect datastore in order to read heart rate data back.

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.