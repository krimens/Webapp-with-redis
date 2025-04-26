# Use the official Nginx base image
FROM nginx:alpine

# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy your static HTML files into the container
COPY index.html /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Nginx will automatically start using its default command
