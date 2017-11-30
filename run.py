# Main application run script that imports the dtrwebhook app.

from dtrwebhook import app

if __name__ == '__main__':
    app.run(debug=True)
