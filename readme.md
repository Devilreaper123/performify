
# 🎉 **GNG5120 Final Project: System's Integration - Performify** 🎉

**Welcome to the GitHub Repository of [Ronit Shahu](#)!**  
This repository houses the code for our innovative project **"Performify"**.  
Whether you're looking to contribute, explore, or simply understand more about our project, we're thrilled to have you here! 🚀

---

## 📌 **Table of Contents**
1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
3. [Prerequisites](#prerequisites)
4. [Setting Up the Virtual Environment](#setting-up-a-virtual-environment)
5. [Running the Application](#running-the-application)
6. [Testing the Application](#testing-the-application)
7. [Supported Platforms](#supported-platforms)
8. [Contributing](#contributing)
9. [License](#license)

---

## 💡 **Project Overview**

**Performify** is a state-of-the-art application designed to perform audio and video processing from various platforms like YouTube, Twitch, and more. With its cutting-edge backend, our project offers seamless integrations and a user-friendly interface to elevate your multimedia experience.

---

## 🚀 **Getting Started**

These instructions will guide you through setting up a copy of the project on your local machine for development and testing purposes. Follow the steps below to get started:

---

## 🔧 **Prerequisites**

Before you begin, ensure you have the following installed on your system:

- **Python 3.9 or Higher**: Essential for running the Python-based application.
- **pip**: The Python package installer, used for managing Python packages.

---

## ⚙️ **Setting Up a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies for your project. This keeps your project's dependencies separate from your system-wide Python packages, reducing potential conflicts.

### 1. **Install virtualenv**

If you haven't installed `virtualenv` yet, install it using pip:

```bash
pip install virtualenv
```

### 2. **Create a Virtual Environment**

Navigate to the project directory and create a virtual environment named `venv`:

```bash
virtualenv venv
```

### 3. **Activate the Virtual Environment**

- **On Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **On Unix or macOS:**

  ```bash
  source venv/bin/activate
  ```

> Once activated, you should see `(venv)` appear at the beginning of your command line prompt, indicating that the virtual environment is active.

### 4. **Install Dependencies**

With the virtual environment active, install the project dependencies:

```bash
pip install -r Requirements.txt
```

---

## ▶️ **Running the Application**

With your virtual environment set up and dependencies installed, you're ready to run the application:

```bash
python api.py
```

Next, launch the front-end interface with:

```bash
streamlit run app.py
```

This will start the Streamlit app, and you should be able to interact with it through your web browser.

---

## 🔍 **Testing the Application**

To test the model, use the file named `beta2.json`.  
The data has been carefully extracted from YouTube and other supported platforms to meet our specific needs.

---

## 🌐 **Supported Platforms**

Performify currently supports the following video and audio platforms:

- **YouTube**
- **Dailymotion**
- **Facebook**
- **Mixcloud**
- **SoundCloud**
- **Streamable**
- **Twitch**
- **Vimeo**
- **Wistia**

> Note: Support for additional platforms may be added in future updates. Contributions are always welcome!

---

## 🤝 **Contributing**

Your contributions are what make our community such an amazing place to learn, inspire, and create! 🎨✨  
We value any contributions you can make, from code enhancements to bug fixes and documentation improvements. To contribute, simply:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

**Thank you for helping us improve Performify!** 😊

---

## 📄 **License**

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute this project, but please give appropriate credit to the original author.

---

We hope this guide helps you get started with **Performify**.  
Happy coding! 👩‍💻👨‍💻✨

---
