from pathlib import Path

dir_path = Path.cwd()
with open('config.yaml', encoding='UTF-8') as yaml:
    for line in yaml:
        path_line = line.split('/')
        path = str(Path(dir_path, *path_line)).rstrip()
        if path.find('.') == -1 and not Path(path).exists():
            Path(path).mkdir()
        elif path.find('.') != -1:
            open(path, 'w').close()
