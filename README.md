# 📦 Bellande Step Models & Executables

# Demo of Bellande Step Executable

![Demo GIF](executable/bellande_step.gif)

## 🧙 Organization Website
- [![Organization Website](https://img.shields.io/badge/Explore%20Our-Website-0099cc?style=for-the-badge)](https://robotics-sensors.github.io)

## 🧙 Organization Github
- [![Organization Github ](https://img.shields.io/badge/Explore%20Our-Github-0099cc?style=for-the-badge)](https://github.com/Robotics-Sensors)

# Author, Creator and Maintainer
- **Ronaldson Bellande**

## Usage

```
./Bellande_Step passcode coord1 coord2 limit dimensions
```

### Arguments

1. `passcode`: The access key for the Bellande Step Executable (must be "bellande_step_executable_access_key")
2. `coord1`: The first coordinate as a Python list (e.g., "[0, 0, 0]" for 3D)
3. `coord2`: The second coordinate as a Python list (e.g., "[1, 1, 1]" for 3D)
4. `limit`: An integer representing the limit for the algorithm
5. `dimensions`: An integer specifying the number of dimensions for the coordinates

### Example

```
./Bellande_Step "bellande_step_executable_access_key" "[0, 0, 0]" "[1, 1, 1]" 10 3
```

### Notes

- The passcode must be exactly "bellande_step_executable_access_key" to run the script.
- Ensure that the number of values in each coordinate matches the specified dimensions.
- Use proper Python list syntax for the coordinates (square brackets and comma-separated values).
- The `limit` and `dimensions` arguments must be integers.
- The script supports infinite dimensions, limited only by system resources.

### Error Handling

The script includes error handling for:
- Incorrect number of arguments
- Invalid passcode
- Mismatched dimensions between coordinates and specified dimensions
- Invalid input format (syntax errors in coordinate lists)
- Other unexpected errors

If an error occurs, an appropriate error message will be displayed.

### Research Organization for Open-source/Semi-open-source API

- The API documentation for the Bellande Step Models can be found on [Bellande Robotics & Sensors Research Innovation Center](https://robotics-sensors.github.io), a platform dedicated to open-source and semi-open-source APIs.

### Model Downloads

- For downloading the Bellande Step Models, please visit [Bellande Artificial Intelligence & Computer Vision Research Innovation Center Website](https://artificial-intelligence-computer-vision.github.io)

### Models Information

#### Open-Source Models to Download

- **2D Space**: Users can download the 2D model from [Hugging Face - Bellande Artificial Intelligence & Computer Vision Research Innovation Center](https://huggingface.co/Artificial-Intelligence-Computer-Vision) with precision of 1 decimal.

#### Close-Source Models to Download

- Visit the research organization website to see how to obtain a Close-Source Model
- **2D Space - Infinite Dimensions**: Downloadable resources related to different dimensions can be accessed from [Bellande Artificial Intelligence & Computer Vision Research Innovation Center](https://artificial-intelligence-computer-vision.github.io) with precision of 10 decimals.

## License

This Algorithm or Models is distributed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/), see [LICENSE](https://github.com/RonaldsonBellande/bellande_step_models/blob/main/LICENSE) and [NOTICE](https://github.com/RonaldsonBellande/bellande_step_models/blob/main/LICENSE) for more information.
