```dockerfile
# Stage 1: Build dependencies (using Python 3.11-alpine for minimal base)
FROM python:3.11-alpine AS build

# Install necessary dependencies for building
RUN apk add --no-cache gcc musl-dev

# Set work directory
WORKDIR /app

# Copy app code
COPY app.py .

# Install Flask in the build stage (this is used for testing the code in stage 2)
RUN pip install --no-cache-dir flask

# Stage 2: Minimal runtime image
FROM python:3.11-alpine

# Create non-root user
RUN adduser -D appuser

# Set working directory
WORKDIR /app

# Copy app code from build stage (including installed flask)
COPY --from=build /app /app

# Install Flask in the runtime image (to ensure it's available for app execution)
RUN pip install --no-cache-dir flask

# Set permissions (optional but good practice)
RUN chown -R appuser:appuser /app

# Use non-root user
USER appuser

EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```