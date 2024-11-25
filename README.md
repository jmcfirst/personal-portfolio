# Personal Portfolio Website

## Image Management Instructions

### Setting up your profile image:

1. **Image Location**:
   - Place your profile image in the `static/images` directory
   - Recommended image size: 200x200 pixels
   - Supported formats: JPG, PNG, SVG
   - Default placeholder image is provided at `static/images/placeholder.svg`

2. **Updating Image Path**:
   - Open `config.py`
   - Locate the `profile_image` variable in the `PersonalInfo` class
   - Update the path to match your image file name:
     ```python
     self.profile_image = "/static/images/your-image-filename.extension"
     ```
   
3. **Image Guidelines**:
   - Use a professional headshot or avatar
   - Ensure good lighting and clear visibility
   - Keep the file size under 1MB for optimal loading

Note: The image will be displayed in a circular format on the website, so center-aligned square images work best.
