# the-bleed-edgemaxxer

An application for generating bleed edges in custom Magic: The Gathering (MTG) cards.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

The `the-bleed-edgemaxxer` application is designed to help you generate bleed edges for custom MTG cards. Bleed edges are essential for ensuring that your cards look professional and are printed correctly without any white borders.

## Features

- Resize images to specified dimensions.
- Add simple black borders or replicate edges for bleed.
- Automatically detects borderless cards
- Process multiple images in a directory.
- Supports common image formats like PNG, JPG, and JPEG.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/the-bleed-edgemaxxer.git
    cd the-bleed-edgemaxxer
    ```

2. **Create and activate the virtual environment:**

    - On Windows:
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        python -m venv .venv
        source .venv/bin/activate
        ```

3. **Install Requirements:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your images:**
    - Place your custom MTG card images in the [cards](http://_vscodecontentref_/1) folder.

2. **Run the application:**

    application.exe

3. **Output:**
    - The processed images with bleed edges will be saved in the [output](http://_vscodecontentref_/2) directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.