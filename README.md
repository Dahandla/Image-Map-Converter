# Image Map Converter v1.0

A powerful tool for generating various texture maps from 2D images, with real-time 3D preview capabilities.

## Features
1. Generate multiple texture maps from a single image:
   - Normal Maps
   - Specular Maps
   - Roughness Maps
   - Ambient Occlusion Maps
   - Height Maps
   - Bump Maps
   - Displacement Maps
   - Metallic Maps

2. Real-time 3D Preview:
   - Interactive WebGL-based 3D viewer
   - Support for multiple 3D model formats (OBJ, GLB, PLY)
   - Basic shape previews (Sphere, Cube, Cylinder, Torus)
   - Dynamic material property adjustments

3. Advanced Controls:
   - Adjustable material properties
   - Dynamic specular map generation
   - Customizable threshold values
   - Real-time preview updates

## Installation
1. `conda create -n CcodeImageMap python=3.10`

`conda activate CcodeImageMap`

`pip install -r requirements.txt`
   
2. Run the application:
   ```
Texture_Map_start.bat
   ```

## Usage
1. Load an Image:
   - Click "Load Image" to select your source image
   - Supported formats: PNG, JPG, BMP, TIFF

2. Generate Maps:
   - Click "Convert to Maps" to generate texture maps
   - Select output directory for the generated maps
   - Adjust material properties using the sliders

3. 3D Preview:
   - Switch to "3D Viewer" tab to preview results
   - Load custom 3D models or use basic shapes
   - Adjust material properties in real-time

## Material Controls
- Brightness Boost: Adjusts overall brightness of generated maps
- Normal Map Strength: Controls the intensity of surface details
- Height Map Strength: Adjusts the displacement effect
- Specular Brightness: Controls reflective highlights
- Roughness Contrast: Adjusts surface smoothness
- AO Intensity: Controls ambient occlusion strength
- Metalness Threshold: Determines metallic vs non-metallic areas

## Tips
1. For best results, use high-resolution source images
2. Experiment with different material property combinations
3. Use the 3D viewer to fine-tune your maps
4. Save your preferred settings for future use

## Support
For help, documentation, and updates, visit:
[GitHub Repository](https://github.com/Dahandla/Image-Map-Converter) 

Video Tutorials:
[Video Tutorials Playlist](https://www.youtube.com/playlist?list=PLNkqxVhFvsiRaZ7qJTcRNk--yqdihuuM2)

## Contact
Email: [saraintelai@gmail.com](mailto:saraintelai@gmail.com)

## License
This software is provided as-is under the MIT License.

Created by Andre Dickinson
© 2024 
