import config
from app import App

def main():
    app = App(config.file_info)
    app.select_method()

if __name__ == '__main__':
    main()
