-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Core areas](https://developer.android.com/develop/core-areas)
-   [Background work](https://developer.android.com/develop/background-work)

# About Background work

Stay organized with collections Save and categorize content based on your preferences.

Android applications should use background tasks when appropriate, and avoid doing everything on the app's main thread. In order to make the app both responsive for your users as well as a good citizen on the Android platform, take any blocking or long-running tasks off the main (UI) thread, and run them in the background instead. This includes tasks like decoding a bitmap, accessing storage, working on a machine learning (ML) model, or performing network requests.

Things to understand about background work include:

-   Understand . This document explains asynchronous work, and helps you understand the difference between asynchronous and persistent work.
    
-    is background work that remains scheduled through app restarts and system reboots.
    
-   Effective use of . Much like the publish-subscribe design pattern, Android apps can send or receive broadcast messages from the Android system and other Android apps.
    
-   How to use the different techniques necessary to  versus .
    

## Videos

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.