-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Guides](https://developer.android.com/guide)

# Principles of navigation

Stay organized with collections Save and categorize content based on your preferences.

Navigation between different screens and apps is a core part of the user experience. The following principles set a baseline for a consistent and intuitive user experience across apps. The  is designed to implement these principles by default, ensuring that users can apply the same heuristics and patterns in navigation as they move between apps.

**Note:** Even if you aren't using the Navigation component in your project, your app should follow these design principles.

## Fixed start destination

Every app you build has a fixed start destination. This is the first screen the user sees when they launch your app from the launcher. This destination is also the last screen the user sees when they return to the launcher after pressing the Back button. Let’s take a look at the [Sunflower app](https://github.com/android/sunflower/tree/main/app) as an example.

!

**Figure 1.** The List Screen is the Sunflower app's start destination.

When launching the Sunflower app from the launcher, the first screen that a user sees is the **List Screen**, the list of plants in their garden. This is also the last screen they see before exiting the app. If they press the Back button from the list screen, they navigate back to the launcher.

**Note:** An app might have a one-time setup or series of login screens. These  should not be considered start destinations because users see these screens only in certain cases.

## Navigation state is represented as a stack of destinations

When your app is first launched, a  is created for the user, and app displays its start destination. This becomes the base destination of what is known as the _back stack_ and is the basis for your app’s navigation state. The top of the stack is the current screen, and the previous destinations in the stack represent the history of where you've been. The back stack always has the start destination of the app at the bottom of the stack.

Operations that change the back stack always operate on the top of the stack, either by pushing a new destination onto the top of the stack or popping the top-most destination off the stack. Navigating to a destination pushes that destination on top of the stack.

The  manages all of your back stack ordering for you, though you can also choose to manage the back stack yourself.

## Up and Back are identical within your app's task

!

**Figure 2.** The Up and Back buttons

The Back button appears in the system navigation bar at the bottom of the screen and is used to navigate in reverse-chronological order through the history of screens the user has recently worked with. When you press the Back button, the current destination is popped off the top of the back stack, and you then navigate to the previous destination.

The Up button appears in the  at the top of the screen. Within your app's task, the Up and Back buttons behave identically.

## The Up button never exits your app

If a user is at the app's start destination, then the Up button does not appear, because the Up button never exits the app. The Back button, however, is shown and does exit the app.

When your app is launched using a  on another app's task, Up transitions users back to your app’s task and through a  and not to the app that triggered the deep link. The Back button, however, does take you back to the other app.

## Deep linking simulates manual navigation

Whether  or manually navigating to a specific destination, you can use the Up button to navigate through destinations back to the start destination.

When deep linking to a destination within your app’s task, any existing back stack for your app’s task is removed and replaced with the deep-linked back stack.

Using the Sunflower app again as an example, let’s assume that the user had previously launched the app from the launcher screen and navigated to the detail screen for an apple. Looking at the Recents screen would indicate that a task exists with the top most screen being the detail screen for the Apple.

!

**Figure 3.** User navigation through the Sunflower app and the resulting back stack.

At this point, the user can tap the Home button to put the app in the background. Next, let’s say this app has a deep link feature that allows users to launch directly into a specific plant detail screen by name. Opening the app via this deep link completely replaces the current Sunflower back stack shown in figure 3 with a new back stack, as shown in figure 4:

!

**Figure 4.** Following a deep link replaces the existing back stack for the Sunflower app.

Notice that the Sunflower back stack is replaced by a _synthetic back stack_ with the avocado detail screen at the top. The _My Garden_ screen, which is the start destination, was also added to the back stack. The original Sunflower back stack is gone, including the app's knowledge that the user was on the Apple details screen before. All of this is important because the synthetic back stack must be realistic. It should match a back stack that could have been achieved by organically navigating through the app.

To meet this need, the synthetic back stack that is created is a simplified one based on the `NavGraph`. For a simple `NavGraph` without nesting, this will consist of the start destination and the deep link destination. For more complex, , the synthetic back stack will also contain the start destinations of any nested graphs that are ancestors of the deep link destination.

The Navigation component  and recreates a realistic back stack for you when linking to any destination in your navigation graph.

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.