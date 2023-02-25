from pathlib import Path

def main() -> None:
    print(f'Current working directory: {Path.cwd()}')
    print(f'Home diretory: {Path.home()}')
    
    path = Path('Makefile')

    print(path.exists())
    print(path.read_text())
    print(path.resolve())
    print(path.resolve().parent)
    print(path.resolve().parent.name)

    newfile = Path.cwd() / './bla/ble/newfile.txt'
    
    newfile.parent.mkdir(parents=True, exist_ok=True)
    newfile.write_text('dafsdfasdfasdf')

if __name__ == "__main__":

    main()