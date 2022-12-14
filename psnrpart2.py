# Import the necessary libraries
import numpy as np
import cv2

# Read the original and reconstructed images
original = cv2.imread('kupu-kupu.jpg')
reconstructed = cv2.imread('resultKupu.png')

# Calculate the MSE between the two images
mse = np.mean((original - reconstructed) ** 2)

# Calculate the PSNR
psnr = 10 * np.log10(255**2 / mse)

# Print the result
print('MSE:', mse)
print('PSNR:', psnr)
