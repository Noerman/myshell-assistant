-   [Android Developers](https://developer.android.com/)
-   [Develop](https://developer.android.com/develop)
-   [Guides](https://developer.android.com/guide)

# Add a sign-in workflow

Stay organized with collections Save and categorize content based on your preferences.

Add a sign-in workflow to your Android app to protect user data and control access to app features and data, helping to keep your app, your data, and your users safe.

!

-   **Protect user data**. Authentication protects your app's user data from unauthorized access. By requiring users to sign in, you can help ensure your users unlock only the information they're entitled to.
-   **Help prevent fraud**. Authentication coupled with identity verification makes it more difficult for an attacker to create fraudulent accounts or gain unauthorized access to existing accounts.
-   **Improve user experience**. A streamlined authentication workflow reduces complexity for your users to sign up and sign in to access their data and services.
-   **Comply with regulations**. A sign-in workflow complies with regulations that require authentication to protect data.

## Authentication

To add authentication to your app, most Android projects should use . Credential Manager is a modern Jetpack library that lets you integrate most major authentication methods into your app, including passkeys, passwords, and federated solutions like Sign in with Google. The benefits of Credential Manager over legacy authentication APIs such as One Tap include:

-   **Simpler integration**: Credential Manager lets you implement most major authentication options with a single, unified API.
-   **Improved user experience**: Credential Manager's unified sign-in interface gives your users a clear, familiar, and consistent experience, reduces churn, and improves registration and sign-in speeds.
-   **Single-tap Google sign in and sign up**: Credential Manager can be configured to prompt your users to create or sign in to a Google Account with a dialog that's inline with your app's content, so they're never taken out of context by a sign-up screen. Reduced sign-up or login friction improves success rates for your users as they register or log into your app.
-   **Enhanced security**: Migrating from passwords to passwordless authentication helps reduce attack vectors, simplifies user onboarding, and enhances your app's security. Credential Manager enables support for passwordless authentication using .
-   **Improved flexibility**: Credential Manager integrates with existing authentication providers, or you can develop your own authentication process.

Credential Manager automatically displays a unified bottom sheet for modern authentication methods, and is the modern replacement for existing authentication implementations, including , and [One Tap](https://developers.google.com/identity/one-tap/android/overview).

**Note:** Sign in with Google can be called as an option in the following ways:

1.  As a Credential Manager bottom sheet that automatically appears when the sign-in screen loads,
2.  As a distinct button that is selected by users on your sign-in screen should they actively choose to Sign in with Google.

Don't call the Credential Manager bottom sheet from the Sign in with Google button. Read  to learn more.

Learn more about how to build authentication in your Android app with Credential Manager:

-   
-   
-   
-   
-   

Learn how to migrate your current authentication flows to Credential Manager:

-   
-   
-   

Learn how to streamline your existing identity and authentication APIs to support passkeys and improved usability with the Credential Manager API:

-   
-   

## Autofill

Some apps, such as password managers, fill out the views in other apps with data provided by the user. Apps that fill out other apps' views are called autofill services. The autofill framework manages the communication between an app and an autofill service and helps improve the user experience by saving time spent filling in fields and minimizing user input errors. Since autofill supports password managers, users can be encouraged to select stronger credentials such as passkeys or unique, machine-generated passwords that can be stored and retrieved securely and with less friction.

Learn more about Android's autofill framework:

-   
-   
-   
-   

## Biometrics

Integrate biometric authentication into your app to further strengthen security. Biometric authentication, especially as part of multi-factor authentication schemes, reduces fraud exposure by ensuring the credential is authentic and verifiably belongs to the intended user. Biometric authentication can improve the user experience in the following ways:

-   Enables faster logins
-   Provides opportunities for reduced-friction credential verification
-   Reduces password usage
-   Potentially aids with regulatory compliance.

Learn more about .

Content and code samples on this page are subject to the licenses described in the . Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.