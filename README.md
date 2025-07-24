

# Course Analysis Service

This service provides functionality to create and summarize online courses. It uses OpenAI's API to generate summaries for course descriptions.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Service](#running-the-service)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
  - [Create User](#create-user)
  - [Create Course](#create-course)
  - [Summarize Course](#summarize-course)

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/MrBlueSkyFox/AiCourseSummaraizer.git
   cd AiCourseSummaraizer
   ```

2. Create a `.env` file in the root directory of the project with the following content:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   SECRET_KEY=your_secret_key
   ...
   ```

## Running the Service

To run the service using Docker Compose, execute the following command:
```sh
docker-compose up --build
```

## Environment Variables

The following environment variables are required for the service to function correctly:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `POSTGRES_USER`: The username for the PostgreSQL database.
- `POSTGRES_PASSWORD`: The password for the PostgreSQL database.
- `POSTGRES_DB`: The name of the PostgreSQL database.
- `POSTGRES_HOST`: The host of the PostgreSQL database.
- `POSTGRES_PORT`: The port of the PostgreSQL database.
- `SECRET_KEY`: A secret key for JWT authentication.


## API Endpoints

### Create User

- **Endpoint**: `POST /users`
- **Description**: Creates a new user.
- **Authentication**: Not required.


### Create Course

- **Endpoint**: `POST /courses`
- **Description**: Creates a new course.
- **Authentication**: Required.


### Summarize Course

- **Endpoint**: `POST /courses/summarize`
- **Description**: Summarizes the description of an existing course.
- **Authentication**: Required.


## Authentication

For endpoints that require authentication, include the JWT token in the `Authorization` header of your request:
```http
Authorization: Bearer your_jwt_token
```

## License

This project is licensed under the MIT License.


## Limitations and Future Improvements

Due to time constraints, the following features have not been implemented in this version of the service:

- **Task Management**: Implementation of task management for asynchronous processing.
- **Rate Limiting**: Rate limiting to control the number of requests to the API.
- **Edit on Fly**: Real-time editing and updating of course descriptions.
- **Other Minor Features**: Various other minor features and improvements.

These features are planned for future releases and will be added as time permits.