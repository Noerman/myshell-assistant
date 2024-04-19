-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Guides](https://developer.android.com/guide)

# Android for Cars overview

Stay organized with collections Save and categorize content based on your preferences.

Bring your app to vehicles running either Android Auto or Android Automotive OS. Use one app architecture that works for both cases so every user can enjoy your app.

## Android Auto

Android Auto provides a driver-optimized app experience for users who have an Android phone with the Android Auto app and a compatible [car or aftermarket stereo system](https://www.android.com/auto/compatibility/). They can use your app directly on their car's display by connecting their phone. You enable Android Auto to connect with your phone app by creating services that Android Auto uses to display a driver-optimized interface to the driver.

**Note:** Android Auto is only compatible with phones running Android 6.0 (API level 23) or higher.

!

**Figure 1.** Android Auto—powered by a phone and running on a car.

## Android Automotive OS

Android Automotive OS is an Android-based infotainment system that is built into vehicles. The car's system is a standalone Android-powered device that is optimized for driving. With Android Automotive OS, users install your app directly onto the car instead of their phones.

!

**Figure 2.** Android Automotive OS running on an emulator.

## Supported app categories

Due to considerations unique to cars, Android Auto and Android Automotive OS only support certain types of apps as described in the following table:

| Category | Description | Platforms | Usage | Publishing |
| --- | --- | --- | --- | --- |
| Media - audio | 
Media apps let users browse and play music, radio, audiobooks, and other audio content in the car. See  for more information.

**Important:** the Media category does not include video content - see the separate  for details on apps that play videos.

_Built using:_ `MediaBrowserService` and `MediaSession`. On Android Automotive OS, you can also build sign-in and settings screens (for use while parked) using Views or Compose.

 | Android Auto and Android Automotive OS | While driving or parked | All track types |
| Messaging | 

Messaging apps let users receive incoming notifications, read messages aloud using text-to-speech, and send replies using voice input in the car. See  for more information.

_Built using_: `MessagingStyle` notifications, a `Service` for handling reply and mark-as-read actions.

 | Android Auto | While driving or parked | All track types |
| Navigation | 

Navigation apps, including providers of driver and delivery services, help users get where they want to go by providing turn-by-turn directions.

_Built using_: The . See  for additional information specific to navigation apps.

 | Android Auto and Android Automotive OS | While driving or parked | All track types |
| Point of Interest (POI) | 

POI apps let the user discover and navigate to points of interest and take relevant actions, such as parking, charging, and fuel apps.

_Built using:_ The . See  for additional information specific to POI apps.

 | Android Auto and Android Automotive OS | While driving or parked | All track types |
| Internet of Things (IOT) | 

IOT apps let users take relevant actions on connected devices from within the car. Examples include controlling the state of certain devices, such as opening a garage door, flipping home light switches, or enabling home security.

_Built using:_ The . See  for additional information specific to IOT apps.

 | Android Auto and Android Automotive OS | While driving or parked | All track types |
| Video | 

Video apps let users view streaming videos while the car is parked. The core purpose of these apps is to display streaming videos.

_Built using:_ Views and/or Compose. See  for more information.

 | Android Automotive OS | Only while parked | All track types |
| Games | 

Game apps let users play games while the car is parked. The core purpose of these apps is to play games.

_Built using:_ Views and/or Compose. See  for more information.

 | Android Automotive OS | Only while parked | Internal Testing tracks |
| Browsers | 

Browser apps let users access web pages while the car is parked.

_Built using:_ Views and/or Compose. See  for more information.

 | Android Automotive OS | Only while parked | Internal Testing tracks |

## Additional resources

To learn more about Android for Cars, see the following additional resources.

### Design

### Samples

### Codelabs

### Blogs

### Videos

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.