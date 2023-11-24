# Flask Web API on Render

This repository contains a simple Flask web application with two routes deployed on Render. The application serves as a fulfillment API for use with Dialogflow.

## Features

- **`/` Route:** Returns the student number in properly formatted JSON.
- **`/webhook` Route:** Returns the text for Dialogflow integration.

## Deployment

The application is deployed on [Render](https://render.com/), a cloud platform for building and running web applications.

### Prerequisites

- Python
- [Render Account](https://render.com/)
- [Render CLI](https://render.com/docs/cli)

### Local Development

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:

    ```bash
    python test.py
    ```

   The app will be accessible at `http://localhost:5000`.

### Deployment on Render

1. Connect your Git repository to Render.
2. Configure the build and start commands in the Render dashboard.
3. Trigger a manual deploy or set up automatic deployments.

The deployed app will be accessible at the provided Render URL.

## Dialogflow Integration

Update your Dialogflow agent's fulfillment webhook URL with the Render app's `/webhook` route.

## Project Structure

- `test.py`: Flask application with defined routes.
- `requirements.txt`: List of Python dependencies.
- `render.yaml`: Render configuration file.

## Author

[Semal Shastri]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

