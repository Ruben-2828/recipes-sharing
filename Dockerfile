FROM python:3.13.1-bookworm

# Disable pip auto checks for updates
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# To not buffer console output
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .