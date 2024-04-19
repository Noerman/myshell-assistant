-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Android Studio](https://developer.android.com/studio)
-   [SDK tools](https://developer.android.com/tools)

# Command-line tools

Stay organized with collections Save and categorize content based on your preferences.

The Android SDK is composed of multiple packages that are required for app development. This page lists the most important command-line tools that are available, organized by the packages in which they're delivered.

You can install and update each package using Android Studio's  or the  command-line tool. All of the packages are downloaded into your Android SDK directory, which you can locate as follows:

1.  In Android Studio, click **File > Project Structure**.
2.  Select **SDK Location** in the left pane. The path is shown under **Android SDK location**.

### Set environment variables

We recommend setting the environment variable for  when using the command line. Also, set your command search path to include `ANDROID_HOME/tools`, `ANDROID_HOME/tools/bin`, and `ANDROID_HOME/platform-tools` to find the most common tools. The steps vary depending on your OS, but read  for general guidance.

## Android SDK Command-Line Tools

Located in: `android_sdk/cmdline-tools/version/bin/`  

Note: The Android SDK Command-Line Tools package, located in `cmdline-tools`, replaces the SDK Tools package, located in `tools`. With the new package, you can select the version of the command line tools you want to install, and you can install multiple versions at a time. With the old package, you can only install the latest version of the tools. Thus, the new package lets you depend on specific versions of the command-line tools without having your code break when new versions are released. For information about the deprecated SDK Tools package, see the .

If you are not using Android Studio, you can download the command-line tools package .

``

Provides insight into the composition of your APK after the build process completes.

``

Lets you create and manage Android Virtual Devices (AVDs) from the command line.

``

Scans code to help you identify and correct problems with the structural quality of your code.

For applications compiled by R8, `retrace` decodes an obfuscated stack trace that maps back to your original source code.

``

Lets you view, install, update, and uninstall packages for the Android SDK

## Android SDK Build Tools

Located in: `android_sdk/build-tools/version/`  
See  for more information.

This package is required to build Android apps. Most of the tools in this package are invoked by the build tools and not intended for you. However, the following command-line tools might be useful:

Parses, indexes, and compiles Android resources into a binary format that is optimized for the Android platform and packages the compiled resources into a single output.

Signs APKs and checks whether APK signatures will be verified successfully on all platform versions that a given APK supports.

Optimizes APK files by ensuring that all uncompressed data starts with a particular alignment relative to the start of the file.

**Note:** You can have multiple versions of the build tools to build your app for different Android versions.

## Android SDK Platform Tools

Located in: `android_sdk/platform-tools/`  
See  for more information.

These tools are updated for every new version of the Android platform to support new features and fix or improve the tools, and each update is backward compatible with earlier platform versions.

In addition to downloading from the SDK Manager, you can download the SDK Platform Tools .

Android Debug Bridge (adb) is a versatile tool that lets you manage the state of an emulator instance or Android-powered device. You can also use it to install an APK on a device.

A command-line utility that lets you encode PNG images to the ETC1 compression standard and decode ETC1 compressed images back to PNG.

`fastboot`

Flashes a device with platform and other system images. For flashing instructions, see [Factory Images for Nexus and Pixel Devices](https://developers.google.com/android/images).

Invoked by adb to view app and system logs.

## Android Emulator

Located in: `android_sdk/emulator/`  
See  for more information.

This package is required to use the Android Emulator. It includes the following:

``

A QEMU-based device-emulation tool that you can use to debug and test your applications in an actual Android run-time environment.

``

Helps you create a disk image that you can use with the emulator to simulate the presence of an external storage card, such as an SD card.

**Note:** Prior to revision 25.3.0, the emulator tools were included with the SDK Tools package.

## Jetifier

 reads a library that uses Support Library classes and outputs an equivalent library that uses the newer AndroidX classes.

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.