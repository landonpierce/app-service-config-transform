# app-service-config-transform

Input is provided with the "INPUT_FILE" environment variable. Defaults to `input.json` if not specified.

## To run:

(Required) Docker installation

### Build Docker Image

1. Clone this repo
 
2. CD to code directory

3. `docker build -t app-service-config-transform .`

### Run Script Using Docker

1. Copy your appsettings.json file into a folder

2. Run `docker run -e INPUT_FILE=input.json -it --rm -v ${pwd}:/src app-service-config-transform`

3. File should be output to the output.json file in your working directory.