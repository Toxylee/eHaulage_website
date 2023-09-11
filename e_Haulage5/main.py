# Import the create_app function from the 'website' package.
from website import create_app

# Create a Flask application instance using the create_app function.
app = create_app()

# Check if this script is being run as the main program.
if __name__ == '__main__':
    app.run(debug=True)
