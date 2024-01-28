# Encryption and Decryption Flask App

This is a simple Flask web application for encrypting and decrypting images using the Fernet symmetric encryption scheme from the `cryptography` library. The application uses a password-based key derivation function (PBKDF2) to generate a secure key from the user's password.

## Getting Started

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/your-username/encryption-flask-app.git
    cd encryption-flask-app
    ```

2. Install the required Python packages using `pip`.

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application.

    ```bash
    python image.py
    ```

    The application should now be running locally. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the web interface.

## Usage

### 1. Encryption

- Navigate to the home page [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- Upload an image file and enter a password.
- Click the "Encrypt" button.
- The encrypted image will be downloaded as `encrypted_image.enc`.

### 2. Decryption

- Navigate to the home page [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- Upload the encrypted image file (`encrypted_image.enc`) and enter the same password used for encryption.
- Click the "Decrypt" button.
- The decrypted image will be downloaded as `decrypted_image.png`.

## Security Considerations

- The application uses a static salt value (`b'123456'`) for key derivation. In a production environment, it is crucial to use a random and unique salt for each user to enhance security.
- Ensure that the application is deployed over HTTPS to encrypt data transmitted between the user's browser and the server.

## Dependencies

- Flask
- cryptography

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
