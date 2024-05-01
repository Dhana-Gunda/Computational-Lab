# Read the image
[img, map] = imread("/home/rguktrkvaleey/dhana.jpeg");

# Extract RGB channels
red = img(:,:,1);
green = img(:,:,2);
blue = img(:,:,3);

# Combine RGB channels into a matrix
rgb_values = [red(:), green(:), blue(:)];

# Save RGB values to CSV
csvwrite("rgb_values.csv", rgb_values);