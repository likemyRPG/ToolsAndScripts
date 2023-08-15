# Cookie Converter

Welcome to the Cookie Converter tool. This script allows you to convert browser cookies from the JSON format to the Netscape HTTP Cookie File format (commonly known as the "cookies.txt" format). This conversion can be beneficial when you need to use these cookies with tools or platforms that support only the Netscape format.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x

## Installation

1. Navigate to the root of the `ToolsAndScripts`:

   ```bash
   cd path_to_ToolsAndScripts
   ```

2. If there are any additional Python dependencies (specified in the `requirements.txt` file), you can install them using:

   ```bash
   pip install -r tools/cookie_converter/requirements.txt
   ```

## Usage

To use the Cookie Converter:

1. Navigate to the `cookie_converter` directory:

   ```bash
   cd tools/cookie_converter
   ```

2. Run the script:

   ```bash
   python cookie_converter.py --input path_to_json_file --output path_to_output_txt
   ```

Make sure to replace `path_to_json_file` with the path to your JSON cookie file and `path_to_output_txt` with your desired output file name.

## Contributing

Your contributions are always welcome! If you have improvements to propose, features to add, or bugs to report, please:

1. Fork the `ToolsAndScripts`.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to your branch.
5. Create a new Pull Request targeting the `master` branch of the original `ToolsAndScripts`.

## License

This tool is part of the `ToolsAndScripts` and is licensed under its respective license. Please see the main repository's `LICENSE` file for more details.