-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Android Studio](https://developer.android.com/studio)
-   [Android Gradle Plugin](https://developer.android.com/build)

# Configure your build

Stay organized with collections Save and categorize content based on your preferences.

The Android build system compiles app resources and source code and packages them into APKs or Android App Bundles that you can test, deploy, sign, and distribute.

Android Studio uses , an advanced build toolkit, to automate and manage the build process while letting you define flexible, custom build configurations. Each build configuration can define its own set of code and resources while reusing the parts common to all versions of your app. The Android Gradle plugin works with the build toolkit to provide processes and configurable settings that are specific to building and testing Android apps.

Gradle and the Android Gradle plugin run independent of Android Studio. This means that you can build your Android apps from within Android Studio, the command line on your machine, or on machines where Android Studio is not installed, such as continuous integration servers.

If you aren't using Android Studio, you can learn how to . The output of the build is the same whether you are building a project from the command line, on a remote machine, or using Android Studio.

**Note:** Because Gradle and the Android Gradle plugin run independently from Android Studio, you need to update the build tools separately. Read the release notes to learn how to .

The flexibility of the Android build system lets you create custom build configurations without modifying your app's core source files. This page helps you understand how the Android build system works and how it can help you customize and automate multiple build configurations. If you want to learn more about deploying your app, see . To start creating custom build configurations right away using Android Studio, see .

## The build process

The build process involves many tools and processes that convert your project into an Android Application Package (APK) or Android App Bundle (AAB).

The Android Gradle plugin does much of the build process for you, but it can be useful to understand certain aspects of the build process so you can adjust the build to meet your requirements.

Different projects may have different build goals. For example, the build for a third-party library produces Android Archive (AAR) or Java Archive (JAR) libraries. However, an app is the most common type of project, and the build for an app project produces a debug or release APK or AAB of your app that you can deploy, test, or release to external users.

This page focuses on app development, but many of the build steps and concepts are common to most build types.

## Android build glossary

Gradle and the Android Gradle plugin help you configure the following aspects of your build:

_Build types_

Build types define certain properties that Gradle uses when building and packaging your app. Build types are typically configured for different stages of your development lifecycle.

For example, the debug build type enables debug options and signs the app with the debug key, while the release build type may shrink, obfuscate, and sign your app with a release key for distribution.

You must define at least one build type to build your app. Android Studio creates the debug and release build types by default. To start customizing packaging settings for your app, learn how to .

_Product flavors_

Product flavors represent different versions of your app that you can release to users, such as free and paid versions. You can customize product flavors to use different code and resources while sharing and reusing the parts that are common to all versions of your app. Product flavors are optional, and you must create them manually. To start creating different versions of your app, learn how to .

_Build variants_

A build variant is a cross-product of build type and product flavor and is the configuration Gradle uses to build your app. Using build variants, you can build the debug version of your product flavors during development and signed release versions of your product flavors for distribution. Although you don't configure build variants directly, you configure the build types and product flavors that form them. Creating additional build types or product flavors also creates additional build variants. To learn how to create and manage build variants, read the  overview.

_Manifest entries_

You can specify values for some properties of the manifest file in the build variant configuration. These build values override the existing values in the manifest file. This is useful if you want to generate multiple variants of your app with a different application name, minimum SDK version, or target SDK version. When multiple manifests are present, the manifest merger tool .

_Dependencies_

The build system manages project dependencies from your local file system and from remote repositories. This means you don't have to manually search, download, and copy binary packages of your dependencies into your project directory. To find out more, see .

_Signing_

The build system lets you specify signing settings in the build configuration, and it can automatically sign your app during the build process. The build system signs the debug version with a default key and certificate using known credentials to avoid a password prompt at build time. The build system does not sign the release version unless you explicitly define a signing configuration for this build. If you don't have a release key, you can generate one as described in . Signed release builds are required for distributing apps through most app stores.

_Code and resource shrinking_

The build system lets you specify a different ProGuard rules file for each build variant. When building your app, the build system applies the appropriate set of rules to  using its built-in shrinking tools, such as R8. Shrinking your code and resources can help reduce your APK or AAB size.

_Multiple APK support_

The build system lets you automatically build different APKs that each contain only the code and resources needed for a specific screen density or Application Binary Interface (ABI). For more information see . However, releasing a single AAB is the recommended approach, as it offers splitting by language in addition to screen density and ABI, while avoiding the need to upload multiple artifacts to Google Play. All new apps submitted after August 2021 are required to use AABs.

## Java versions in Android builds

Whether your source code is written in Java, Kotlin, or both, there are several places you must choose a JDK or Java language version for your build. See  for details.

## Build configuration files

Creating custom build configurations requires you to make changes to one or more build configuration files. These plain-text files use Domain Specific Language (DSL) to describe and manipulate the build logic using [Kotlin script](https://kotlinlang.org/docs/command-line.html#run-scripts), which is a flavor of the Kotlin language. You can also use , which is a dynamic language for the Java Virtual Machine (JVM), to configure your builds.

You don't need to know Kotlin script or Groovy to start configuring your build, because the Android Gradle plugin introduces most of the DSL elements you need. To learn more about the Android Gradle plugin DSL, read the . Kotlin script also relies on the [underlying Gradle Kotlin DSL](https://docs.gradle.org/current/userguide/kotlin_dsl.html#kotlin_dsl).

When starting a new project, Android Studio automatically creates some of these files for you and populates them based on sensible defaults. The project file structure has the following layout:

└── MyApp/  # Project
    ├── gradle/
    │   └── wrapper/
    │       └── gradle-wrapper.properties
    ├── build.gradle(.kts)
    ├── settings.gradle(.kts)
    └── app/  # Module
        ├── build.gradle(.kts)
        └── build/
            ├── libs/
            └── src/
                └── main/  # Source set
                    ├── java/
                    │   └── com.example.myapp
                    ├── res/
                    │   ├── drawable/
                    │   ├── values/
                    │   └── ...
                    └── AndroidManifest.xml

There are a few Gradle build configuration files that are part of the standard project structure for an Android app. Before you can start configuring your build, it's important to understand the scope and purpose of each of these files and the basic DSL elements they define.

### The Gradle Wrapper file

The Gradle wrapper (`gradlew`) is a small application included with your source code that downloads and launches Gradle itself. This creates more-consistent build execution. Developers download the application source and run `gradlew`. This downloads the required Gradle distribution, and launches Gradle to build your application.

The `gradle/wrapper/gradle-wrapper.properties` file contains a property, `distributionUrl`, that describes which version of Gradle is used to run your build.

**Tip:** If simultaneously working on multiple projects, if possible, ensure that all of the projects use the same Gradle version. Otherwise, Gradle creates copies of the Gradle daemon for each Gradle version, in addition to separate copies for each . This increases memory and CPU usage, potentially slowing your builds or impacting other work on the machine.

```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.0-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

### The Gradle settings file

The `settings.gradle.kts` file (for the Kotlin DSL) or `settings.gradle` file (for the Groovy DSL) is located in the root project directory. This settings file defines project-level repository settings and informs Gradle which modules it should include when building your app. Multi-module projects need to specify each module that should go into the final build.

For most projects, the file looks like the following by default:

### Kotlin

pluginManagement {

    /\*\*
      \* The pluginManagement.repositories block configures the
      \* repositories Gradle uses to search or download the Gradle plugins and
      \* their transitive dependencies. Gradle pre-configures support for remote
      \* repositories such as JCenter, Maven Central, and Ivy. You can also use
      \* local repositories or define your own remote repositories. The code below
      \* defines the [Gradle Plugin Portal](https://plugins.gradle.org/), ,
      \* and the [Maven Central Repository](https://search.maven.org/) as the repositories Gradle should use to look for its
      \* dependencies.
      \*/

    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}
dependencyResolutionManagement {

    /\*\*
      \* The dependencyResolutionManagement.repositories
      \* block is where you configure the repositories and dependencies used by
      \* all modules in your project, such as libraries that you are using to
      \* create your application. However, you should configure module-specific
      \* dependencies in each module-level build.gradle file. For new projects,
      \* Android Studio includes Google's Maven repository and the Maven Central
      \* Repository by default, but it does not configure any dependencies (unless
      \* you select a template that requires some).
      \*/

  repositoriesMode.set(RepositoriesMode.FAIL\_ON\_PROJECT\_REPOS)
  repositories {
      google()
      mavenCentral()
  }
}
rootProject.name = "My Application"
include(":app")

### Groovy

pluginManagement {

    /\*\*
      \* The pluginManagement.repositories block configures the
      \* repositories Gradle uses to search or download the Gradle plugins and
      \* their transitive dependencies. Gradle pre-configures support for remote
      \* repositories such as JCenter, Maven Central, and Ivy. You can also use
      \* local repositories or define your own remote repositories. The code below
      \* defines the [Gradle Plugin Portal](https://plugins.gradle.org/), ,
      \* and the [Maven Central Repository](https://search.maven.org/) as the repositories Gradle should use to look for its
      \* dependencies.
      \*/

    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}
dependencyResolutionManagement {

    /\*\*
      \* The dependencyResolutionManagement.repositories
      \* block is where you configure the repositories and dependencies used by
      \* all modules in your project, such as libraries that you are using to
      \* create your application. However, you should configure module-specific
      \* dependencies in each module-level build.gradle file. For new projects,
      \* Android Studio includes Google's Maven repository and the Maven Central
      \* Repository by default, but it does not configure any dependencies (unless
      \* you select a template that requires some).
      \*/

    repositoriesMode.set(RepositoriesMode.FAIL\_ON\_PROJECT\_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "My Application"
include ':app'

### The top-level build file

The top-level `build.gradle.kts` file (for the Kotlin DSL) or `build.gradle` file (for the Groovy DSL) is located in the root project directory. It typically defines the common versions of plugins used by modules in your project.

The following code sample describes the default settings and DSL elements in the top-level build script after creating a new project:

### Kotlin

plugins {

    /\*\*
     \* Use \`apply false\` in the top-level build.gradle file to add a Gradle
     \* plugin as a build dependency but not apply it to the current (root)
     \* project. Don't use \`apply false\` in sub-projects. For more information,
     \* see [Applying external plugins with same version to subprojects](https://docs.gradle.org/current/userguide/plugins.html#sec:subprojects_plugins_dsl).
     \*/

    id("com.android.application") version "8.3.0" apply false
    id("com.android.library") version "8.3.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.23" apply false
}

### Groovy

plugins {

    /\*\*
     \* Use \`apply false\` in the top-level build.gradle file to add a Gradle
     \* plugin as a build dependency but not apply it to the current (root)
     \* project. Don't use \`apply false\` in sub-projects. For more information,
     \* see [Applying external plugins with same version to subprojects](https://docs.gradle.org/current/userguide/plugins.html#sec:subprojects_plugins_dsl).
     \*/

    id 'com.android.application' version '8.3.0' apply false
    id 'com.android.library' version '8.3.0' apply false
    id 'org.jetbrains.kotlin.android' version '1.9.23' apply false
}

### The module-level build file

The module-level `build.gradle.kts` (for the Kotlin DSL) or `build.gradle` file (for the Groovy DSL) is located in each `project/module/` directory. It lets you configure build settings for the specific module it is located in. Configuring these build settings lets you provide custom packaging options, such as additional build types and product flavors, and override settings in the `main/` app manifest or top-level build script.

#### Android SDK Settings

The module-level build file for your application includes settings that indicate Android SDK versions used when compiling, selecting platform behaviors, and specifying the minimum version that your application runs on.

!

_`compileSdk`_

The `compileSdk` determines which Android and Java APIs are available when compiling your source code. To use the latest Android features, use the latest Android SDK when compiling.

Some Android platform APIs might not be available in older API levels. You can  or use  to use newer features with lower Android API levels.

Each Android SDK provides a subset of Java APIs for use in your application. The table at  shows which Java API level is available based on the Android SDK version. The newer Java APIs are supported on earlier versions of Android through , which must be enabled in your build.

Android Studio displays warnings if your `compileSdk` conflicts with the current version of Android Studio, AGP, or your project's library dependency requirements.

_`minSdk`_

The `minSdk` specifies the lowest version of Android that you want your app to support. Setting `minSdk` restricts which devices can install your app.

Supporting lower versions of Android might require more conditional checks in your code or more use of AndroidX compatibility libraries. You should weigh the maintenance cost of supporting lower versions against the percentage of users that are still using those lower versions. See the version chart in the **New project wizard** of Android Studio for the current version-use percentages.

When editing your code in Android Studio or running checks during your build, lint will warn about APIs that you use that are not available in the `minSdk`. You should fix these by  or by using  for backward compatibility.

_`targetSdk`_

The `targetSdk` serves two purposes:

1.  It sets runtime behavior of your application.
2.  It attests which version of Android you've tested against.

If you run on a device that's using a higher version of Android than your `targetSdk`, Android runs your app in a compatibility mode that behaves similarly to the lower version indicated in your `targetSdk`. For example, when API 23 introduced the runtime permissions model, not all apps were ready to immediately adopt it. By setting `targetSdk` to 22, those apps could run on API 23 devices without using runtime permissions, and could use features included in the latest `compileSdk` version. Google Play distribution policy enforces .

The value of `targetSdk` must be less than or equal to that of `compileSdk`.

**Note:** The values of `compileSdk` and `targetSdk` don't need to be the same. Keep the following basic principles in mind:

-   `compileSdk` gives you access to new APIs
-   `targetSdk` sets the runtime behavior of your app
-   `targetSdk` must be less than or equal to `compileSdk`

#### Sample app-module build script

This sample Android app module build script outlines some of the basic DSL elements and settings:

### Kotlin

/\*\*
 \* The first section in the build configuration applies the Android Gradle plugin
 \* to this build and makes the android block available to specify
 \* Android-specific build options.
 \*/

plugins {
    id("com.android.application")
}

/\*\*
 \* Locate (and possibly download) a JDK used to build your kotlin
 \* source code. This also acts as a default for sourceCompatibility,
 \* targetCompatibility and jvmTarget. Note that this does not affect which JDK
 \* is used to run the Gradle build itself, and does not need to take into
 \* account the JDK version required by Gradle plugins (such as the
 \* Android Gradle Plugin)
 \*/
kotlin {
    jvmToolchain(11)
}

/\*\*
 \* The android block is where you configure all your Android-specific
 \* build options.
 \*/

android {

    /\*\*
     \* The app's . Used primarily to access app resources.
     \*/

    namespace = "com.example.myapp"

    /\*\*
     \* compileSdk specifies the Android API level Gradle should use to
     \* compile your app. This means your app can use the API features included in
     \* this API level and lower.
     \*/

    compileSdk = 33

    /\*\*
     \* The defaultConfig block encapsulates default settings and entries for all
     \* build variants and can override some attributes in main/AndroidManifest.xml
     \* dynamically from the build system. You can configure product flavors to override
     \* these values for different versions of your app.
     \*/

    defaultConfig {

        // Uniquely identifies the package for publishing.
        applicationId = "com.example.myapp"

        // Defines the minimum API level required to run the app.
        minSdk = 21

        // Specifies the API level used to test the app.
        targetSdk = 33

        // Defines the version number of your app.
        versionCode = 1

        // Defines a user-friendly version name for your app.
        versionName = "1.0"
    }

    /\*\*
     \* The buildTypes block is where you can configure multiple .
     \* By default, the build system defines two build types: debug and release. The
     \* debug build type is not explicitly shown in the default build configuration,
     \* but it includes debugging tools and is signed with the debug key. The release
     \* build type applies ProGuard settings and is not signed by default.
     \*/

    buildTypes {

        /\*\*
         \* By default, Android Studio configures the release build type to enable code
         \* shrinking, using minifyEnabled, and specifies the default ProGuard rules file.
         \*/

        getByName("release") {
            isMinifyEnabled = true // Enables code shrinking for the release build type.
            proguardFiles(
                getDefaultProguardFile("proguard-android.txt"),
                "proguard-rules.pro"
            )
        }
    }

    /\*\*
     \* The productFlavors block is where you can configure multiple .
     \* This lets you create different versions of your app that can
     \* override the defaultConfig block with their own settings. Product flavors
     \* are optional, and the build system does not create them by default.
     \*
     \* This example creates a free and paid product flavor. Each product flavor
     \* then specifies its own application ID, so that they can exist on the Google
     \* Play Store, or an Android device, simultaneously.
     \*
     \* If you declare product flavors, you must also declare flavor dimensions
     \* and assign each flavor to a flavor dimension.
     \*/

     += "tier"
    productFlavors {
        create("free") {
            dimension = "tier"
            applicationId = "com.example.myapp.free"
        }

        create("paid") {
            dimension = "tier"
            applicationId = "com.example.myapp.paid"
        }
    }

    /\*\*
     \* To override source and target compatibility (if different from the
     \* toolchain JDK version), add the following. All of these
     \* default to the same value as kotlin.jvmToolchain. If you're using the
     \* same version for these values and kotlin.jvmToolchain, you can
     \* remove these blocks.
     \*/
    //compileOptions {
    //    sourceCompatibility = JavaVersion.VERSION\_11
    //    targetCompatibility = JavaVersion.VERSION\_11
    //}
    //kotlinOptions {
    //    jvmTarget = "11"
    //}
}

/\*\*
 \* The dependencies block in the module-level build configuration file
 \* specifies dependencies required to build only the module itself.
 \* To learn more, go to .
 \*/

dependencies {
    implementation(project(":lib"))
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation(fileTree(mapOf("dir" to "libs", "include" to listOf("\*.jar"))))
}

### Groovy

/\*\*
 \* The first line in the build configuration applies the Android Gradle plugin
 \* to this build and makes the android block available to specify
 \* Android-specific build options.
 \*/

plugins {
    id 'com.android.application'
}

/\*\*
 \* Locate (and possibly download) a JDK used to build your kotlin
 \* source code. This also acts as a default for sourceCompatibility,
 \* targetCompatibility and jvmTarget. Note that this does not affect which JDK
 \* is used to run the Gradle build itself, and does not need to take into
 \* account the JDK version required by Gradle plugins (such as the
 \* Android Gradle Plugin)
 \*/
kotlin {
    jvmToolchain 11
}

/\*\*
 \* The android block is where you configure all your Android-specific
 \* build options.
 \*/

android {

    /\*\*
     \* The app's . Used primarily to access app resources.
     \*/

    namespace 'com.example.myapp'

    /\*\*
     \* compileSdk specifies the Android API level Gradle should use to
     \* compile your app. This means your app can use the API features included in
     \* this API level and lower.
     \*/

    compileSdk 33

    /\*\*
     \* The defaultConfig block encapsulates default settings and entries for all
     \* build variants and can override some attributes in main/AndroidManifest.xml
     \* dynamically from the build system. You can configure product flavors to override
     \* these values for different versions of your app.
     \*/

    defaultConfig {

        // Uniquely identifies the package for publishing.
        applicationId 'com.example.myapp'

        // Defines the minimum API level required to run the app.
        minSdk 21

        // Specifies the API level used to test the app.
        targetSdk 33

        // Defines the version number of your app.
        versionCode 1

        // Defines a user-friendly version name for your app.
        versionName "1.0"
    }

    /\*\*
     \* The buildTypes block is where you can configure multiple .
     \* By default, the build system defines two build types: debug and release. The
     \* debug build type is not explicitly shown in the default build configuration,
     \* but it includes debugging tools and is signed with the debug key. The release
     \* build type applies ProGuard settings and is not signed by default.
     \*/

    buildTypes {

        /\*\*
         \* By default, Android Studio configures the release build type to enable code
         \* shrinking, using minifyEnabled, and specifies the default ProGuard rules file.
         \*/

        release {
              minifyEnabled true // Enables code shrinking for the release build type.
              proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }

    /\*\*
     \* The productFlavors block is where you can configure multiple .
     \* This lets you create different versions of your app that can
     \* override the defaultConfig block with their own settings. Product flavors
     \* are optional, and the build system does not create them by default.
     \*
     \* This example creates a free and paid product flavor. Each product flavor
     \* then specifies its own application ID, so that they can exist on the Google
     \* Play Store, or an Android device, simultaneously.
     \*
     \* If you declare product flavors, you must also declare flavor dimensions
     \* and assign each flavor to a flavor dimension.
     \*/

     "tier"
    productFlavors {
        free {
            dimension "tier"
            applicationId 'com.example.myapp.free'
        }

        paid {
            dimension "tier"
            applicationId 'com.example.myapp.paid'
        }
    }

    /\*\*
     \* To override source and target compatibility (if different from the
     \* tool chain JDK version), add the following. All of these
     \* default to the same value as kotlin.jvmToolchain. If you're using the
     \* same version for these values and kotlin.jvmToolchain, you can
     \* remove these blocks.
     \*/
    //compileOptions {
    //    sourceCompatibility JavaVersion.VERSION\_11
    //    targetCompatibility JavaVersion.VERSION\_11
    //}
    //kotlinOptions {
    //    jvmTarget = '11'
    //}
}

/\*\*
 \* The dependencies block in the module-level build configuration file
 \* specifies dependencies required to build only the module itself.
 \* To learn more, go to .
 \*/

dependencies {
    implementation project(":lib")
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation fileTree(dir: 'libs', include: \['\*.jar'\])
}

### Gradle properties files

Gradle also includes two properties files, located in your root project directory, that you can use to specify settings for the Gradle build toolkit itself:

`gradle.properties`

This is where you can configure project-wide Gradle settings, such as the Gradle daemon's maximum heap size. For more information, see [Build Environment](https://docs.gradle.org/current/userguide/build_environment.html).

`local.properties`

Configures local environment properties for the build system, including the following:

-   `ndk.dir` - Path to the NDK. This property has been deprecated. Any downloaded versions of the NDK are installed in the `ndk` directory within the Android SDK directory.
-   `sdk.dir` - Path to the Android SDK.
-   `cmake.dir` - Path to CMake.
-   `ndk.symlinkdir` - In Android Studio 3.5 and higher, creates a symlink to the NDK that can be shorter than the installed NDK path.

**Caution:** The `local.properties` file is reserved for properties specific to the Android Gradle plugin. Putting your own values in this file can cause problems. If you need to define your own local properties, .

### Remap the NDK to a shorter path (Windows only)

In Windows, tools in the installed NDK folder, such as `ld.exe`, end up with long paths. The tools don't support long paths well.

To create a shorter path, in `local.properties`, set the property `ndk.symlinkdir` to request that the Android Gradle plugin create a symlink to the NDK. The path of that symlink can be shorter than the existing NDK folder. For example, `ndk.symlinkdir = C:\` results in the following symlink: `C:\ndk\19.0.5232133`

### Sync project with Gradle files

When you make changes to the build configuration files in your project, Android Studio requires that you sync your project files so that it can import your build configuration changes and run some checks to make sure your configuration doesn't create build errors.

To sync your project files, click **Sync Now** in the notification bar that appears when you make a change, as shown in figure 1, or click **Sync Project** ! from the menu bar. If Android Studio finds any errors with your configuration — for example, your source code uses API features that are only available in an API level higher than your `compileSdkVersion` — the **Messages** window describes the issue.

!

**Figure 1.** Sync the project with build configuration files in Android Studio.

### Source sets

Android Studio logically groups source code and resources for each module into _source sets_. When you create a new module, Android Studio creates a `main/` source set within the module. A module's `main/` source set includes the code and resources used by all its build variants.

Additional source set directories are optional, and Android Studio doesn't automatically create them for you when you configure new build variants. However, creating source sets, similar to `main/`, helps organize files and resources that Gradle should only use when building certain versions of your app:

`src/main/`

This source set includes code and resources common to all build variants.

`src/buildType/`

Create this source set to include code and resources only for a specific build type.

`src/productFlavor/`

Create this source set to include code and resources only for a specific product flavor.

**Note:** If you configure your build to , you can create source set directories for each _combination_ of product flavors between the flavor dimensions: `src/productFlavor1ProductFlavor2/`.

`src/productFlavorBuildType/`

Create this source set to include code and resources only for a specific build variant.

For example, to generate the "fullDebug" version of your app, the build system merges code, settings, and resources from following source sets:

-   `src/fullDebug/` (the build variant source set)
-   `src/debug/` (the build type source set)
-   `src/full/` (the product flavor source set)
-   `src/main/` (the main source set)

**Note:** When you create a new file or directory in Android Studio, use the **File > New** menu options to create it for a specific source set. The source sets you can choose from are based on your build configurations, and Android Studio automatically creates the required directories if they don't already exist.

If different source sets contain different versions of the same file, Gradle uses the following priority order when deciding which file to use. Source sets on the left override the files and settings of source sets to the right:

> build variant > build type > product flavor > main source set > library dependencies

This allows Gradle to use files that are specific to the build variant you are trying to build while reusing activities, application logic, and resources that are common to other versions of your app.

When , Gradle uses the same priority order so each build variant can define different components or permissions in the final manifest. To learn more about creating custom source sets, read .

## Version catalogs

If your build contains multiple modules with common dependencies, or you have multiple independent projects with common dependencies, we recommend that you use a [version catalog or bill of materials (BOM)](https://docs.gradle.org/current/userguide/platforms.html) to specify the common versions.

## Other build systems

Building Android apps with [Bazel](https://bazel.build/) is possible but not officially supported. Android Studio does not officially support Bazel projects.

To better understand the current limitations of building with Bazel, see the [known issues](https://github.com/bazelbuild/bazel/issues?q=is%3Aissue+is%3Aopen+label%3Ateam-Android).

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.