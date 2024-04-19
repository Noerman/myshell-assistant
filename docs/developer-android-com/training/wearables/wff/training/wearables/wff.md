-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Guides](https://developer.android.com/guide)

# Watch Face Format

Stay organized with collections Save and categorize content based on your preferences.

!

A watch face is the first thing that a user sees when they take a look at their watch, making it the most frequently-used surface of Wear OS. Users rely on watch faces to customize their watch to suit their style and meet their needs.

Created in partnership with Samsung, the Watch Face Format is a declarative XML format to configure the appearance and behavior of watch faces. This means that there's no executable code involved in creating a watch face, and there's no code embedded in your watch face APK.

The Wear OS platform takes care of the logic needed to render the watch face so you can focus on your creative ideas, rather than code optimizations or battery performance.

Watch faces that are built with this new format require less maintenance and fewer updates than the ones built using the Jetpack Watch Face libraries. For example, you don't need to update your watch face to benefit from improvements in performance or battery consumption, or to get the latest bug fixes.

## About the format

Attributes are strongly typed and have guidelines around frequency and valid values to avoid most sources of errors when creating a watch face from scratch. You can create a watch face directly using the format, or create tooling to support the creation of watch faces. One such example of tooling is , which supports the ability to export watch face designs to the Watch Face Format.

Like Watch Face Studio, the Watch Face Format offers the following capabilities:

-   **Style editing:** Customize the watch face, including its color, background image, and font.
    
-   **Groups and complications:** Group components so that you can control or move those components with a single action. You can also handle an entire  as one group.
    
-   **Tag expressions:** Add tags with date, time, battery, step count information, and more.
    

## Learn more

Learn more about the Watch Face Format in these guides:

-   : Learn best practices for your watch face's layout and user experience.
-   : Configure an Android App Bundle that supports the Watch Face Format.
-   : Learn how to configure your watch face so that the system consumes as little memory as possible when rendering your watch face.
-   : Explore the individual elements that are parts of a Watch Face Format file. The root element is always `WatchFace`.
-   [**Publishing guide**](https://support.google.com/googleplay/android-developer/answer/13560201): Learn how to upload your watch face to the Play Store.
-   [**GitHub samples**](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat): Get started through building sample watch faces and deploy them on the Wear OS emulator or your physical device.
-   [**WFF and memory validator**](https://github.com/google/watchface): Use these open source tools to check your Watch Face Format file for errors and confirm acceptable memory usage before submitting to Google Play.

## Recommended for you

-   Note: link text is displayed when JavaScript is off
-   
-   

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.