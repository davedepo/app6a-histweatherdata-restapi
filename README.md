![Static Badge](https://img.shields.io/badge/Project_Status-Complete-brightgreen) ![Static Badge](https://img.shields.io/badge/Build-Passing-brightgreen) ![Static Badge](https://img.shields.io/badge/Open_to_Collaboration-Yes-orange)

<h1> Project: RESTful API for Temperature Data </h1>

This project implements a RESTful API to provide access to temperature data. 
The API retrieves data from external sources, currently in CSV format, and delivers the processed information in a structured JSON format. 
This structured format, a list of dictionaries, facilitates easy integration with various applications and web service.

Hence, leveraging RESTful Design for a Temperature Data API

**RESTful Design Principles in Action:**

Client-Server Architecture: Your code separates the concerns of the client (user) and the server (data provider). The client interacts with the API through well-defined endpoints to request data, and the server processes those requests and delivers the temperature data.

Stateless Communication: Each API request from the client includes all necessary information (station ID, date, etc.) for the server to process the request. The server doesn't maintain any session state about the client between requests.

Standardized Resource Identification: Your API uses URLs to uniquely identify specific temperature data resources (e.g., /api/v1/123456/2023-07-04 for station 123456 on July 4th, 2023).

Uniform Interface: The API uses a consistent approach to handle data access using HTTP methods (likely GET in this case) across different endpoints.

Representation of Resources: Temperature data is delivered in a well-structured JSON format (list of dictionaries), which is a common and easily interpretable representation for data exchanged over web APIs.

<h3> Table of Contents </h3>

- System Details
- Installation
- Usage
- Screenshots
- Features
- Licence
- Authors and acknowledgment

<h3> System Details </h3>

- **Language:** Built with Python 3.12.
- **Development Environment:** Developed using PyCharm IDE.
- **Version Control:** Managed with Git.

<h3> Installation </h3>

* Clone the repository:
    ```bash
    git clone https://github.com/davedepo/app6a-histweatherdata-restapi.git
    ```
* Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

<h3> Usage </h3>
 
This section outlines two ways to interact with the temperature data API:

**A. Running the API locally (for development and testing):**

- This method is ideal for users familiar with running Python programs with Flask.

  - **Steps:**
    - Ensure you have Python and Flask installed on your system. You can install them using pip install Flask.

    - Open a terminal or command prompt and navigate to the directory containing the project files (including main.py).

    - Run the program using the following command:

    ```
      python main.py
    ```

- **Note** This will start the API server, typically on port 5000 by default. You can then access the API endpoints based on examples shared on homepage.

**B. Deploying the API as a web service (for production):**

- This method is ideal for users familiar with cloud hosting services and allows you to make the API accessible over the internet.

  - **Steps:**
    - Choose a cloud hosting platform that supports Python web applications, such as PythonAnywhere or Heroku. Refer to their documentation for specific deployment instructions.

    - Deploy the project files (including main.py) to your chosen cloud platform.

    - Configure a scheduled task on your hosting platform to run the program at regular intervals (e.g., daily, hourly) to keep the data updated.

<h3> Screenshots </h3>

- API Homepage

   ![hist weather API](/app_screenprint/hist_weather_api_1.png?raw=true "sample")
   
- url end-point 1: 1 Station, 1 Date
   ![hist weather API](/app_screenprint/hist_weather_api_2.png?raw=true "sample")
- url end-point 2: 1 Station (All dates)
   ![hist weather API](/app_screenprint/hist_weather_api_3.png?raw=true "sample")
- url end-point 3: 1 Station (Yearly data)
   ![hist weather API](/app_screenprint/hist_weather_api_4.png?raw=true "sample")

<h3> Features </h3>

The feature set includes;

- Data Access: Offers endpoints for retrieving temperature data in JSON format.
- Station and Date: Retrieve temperature data for a specific station on a particular date. (URL endpoint 1)
- All Station Data: Retrieve all temperature data for a specified station. (URL endpoint 2)
- Station Yearly Data: Retrieve temperature data for a specific station for a given year. (URL endpoint 3)
- Data Format: Delivers data in a well-structured JSON format (list of dictionaries) for ease of use in various applications.
- Versioning: The API endpoints are designed with versioning in mind. This allows for future enhancements and potential breaking changes while maintaining compatibility with existing users. The current version is v1 (reflected in the URL structure)..

Further, it has the potential to become a full-fledged API service with additions such as;

- Data Enhancements - to support more data formats, validations, pagination, filtering capabilities
- Funcitionality Enhancements - to cover authentication, caching, metrics & monitoring, scalability etc.
- Documentation Enhancements - to cover logic & detailed API reference documentation to improve readability and maintainability

<h3> Licence </h3>

This project is licensed under the MIT License.

<h3> Authors and Acknowledgment </h3>

- **Udemy**: For providing a platform to learn.
- **Ardit Sulce** (https://github.com/arditsulceteaching) : Created a code-along learning module for building this app.
- **Python Developers & Community**: Provided extensive documentation and examples to support this learning.
- **OpenAI and Copilot**: For providing support, assistance, and encouragement in this learning journey.
- **PyCharm Team:** Making it easy to learn with all embedded features for beginners.
