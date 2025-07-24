

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
   git clone https://github.com/your-repo/course-analysis-service.git
   cd course-analysis-service
   ```

2. Create a `.env` file in the root directory of the project with the following content:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=your_database_url
   SECRET_KEY=your_secret_key
   ```

## Running the Service

To run the service using Docker Compose, execute the following command:
```sh
docker-compose up --build
```

## Environment Variables

The following environment variables are required for the service to function correctly:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: The URL of your database.
- `SECRET_KEY`: A secret key for JWT authentication.

## API Endpoints

### Create User

- **Endpoint**: `POST /users`
- **Description**: Creates a new user.
- **Authentication**: Not required.
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

### Create Course

- **Endpoint**: `POST /courses`
- **Description**: Creates a new course.
- **Authentication**: Required.
- **Request Body**:
  ```json
  {
    "course_name": "Course Name",
    "course_description": "Course Description"
  }
  ```

### Summarize Course

- **Endpoint**: `POST /courses/summarize`
- **Description**: Summarizes the description of an existing course.
- **Authentication**: Required.
- **Request Body**:
  ```json
  {
    "course_id": "course_id"
  }
  ```

## Authentication

For endpoints that require authentication, include the JWT token in the `Authorization` header of your request:
```http
Authorization: Bearer your_jwt_token
```

## License

This project is licensed under the MIT License.