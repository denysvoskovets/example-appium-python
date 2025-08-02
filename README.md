# Appium Pytest Example

This project demonstrates a test automation framework using **Appium** and **pytest** for mobile app testing on Android and iOS devices.

---

## Prerequisites

Before running tests, ensure you have the following installed and configured on your machine:

- **Python 3.8 or higher**  
  Used to run the test scripts and manage dependencies.

- **pip** (Python package manager)  
  Comes bundled with Python; used to install required Python packages.

- **Appium Server**  
  Download and install Appium from [https://appium.io/](https://appium.io/). This is required to interact with mobile devices/emulators during testing.

- **Android SDK and Java JDK 11 or higher** (for Android testing)  
  Install Android SDK and Java (at least JDK 11) to run Android emulators. You can install Android Studio which bundles both.

- (Not needed. In Framework not whole setup for iOS)**Xcode and iOS Simulator** (for iOS testing, macOS only)  
  If you want to test on iOS simulators, you need a Mac with Xcode installed.

- **Node.js** 
  Required if you want to install and run Appium via npm.

---

## Setup and Installation

1. **Get the project files**  
   To get started, clone the project repository using Git:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Create and activate a Python virtual environment (recommended)**

   On Linux/macOS terminal:

```bash
   python3 -m venv venv
   source venv/bin/activate
```
   
3. **Install Python dependencies**  
   From the project root directory run:
    
```bash
    pip install --upgrade pip
    pip install -r requirements.txt
```

4. **Start the Appium server**  
   In a separate terminal window, launch Appium by running:
```bash
    appium
```
This will start the server that listens for test commands.

---
### Running Tests

Run tests locally on Android emulator or device

Make sure you have an Android emulator running (e.g., Pixel 9) or a connected Android device. Then run:

```bash
    pytest --platform=android --device="Pixel 9" --alluredir=allure-results
```

and for allure report generation

```bash
    allure serve allure-results
```

---

## Using Markers

You can use pytest markers in your tests to group and selectively run specific sets of tests.

The following markers are available:

 - Run all tests
```bash
    pytest --platform=android --device="Pixel 9" --alluredir=allure-results
```
 - Smoke
```bash
    pytest -m smoke --platform=android --device="Pixel 9" --alluredir=allure-results
```
 - Authorization
```bash
    pytest -m authorization --platform=android --device="Pixel 9"
```
- Long(full onboarding flow)
```bash
    pytest -m long --platform=android --device="Pixel 9"
```