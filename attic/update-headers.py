import click

@click.command()
@click.argument('template_file', type=click.Path(exists=True))
@click.argument('files_to_modify', type=click.Path(exists=True), nargs=-1)
def modify_files(template_file, files_to_modify):
    # Read the template file and extract the variables
    with open(template_file, 'r') as f:
        template_lines = f.readlines()
    template_variables = {}
    for line in template_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            template_variables[key.strip().lower()] = value.strip()

    # Modify the files
    for file_to_modify in files_to_modify:
        with open(file_to_modify, 'r') as f:
            file_lines = f.readlines()
        modified_lines = []
        for line in file_lines:
            if not line.strip():
                break
            if ':' in line:
                key, value = line.split(':', 1)
                if key.strip().lower() in template_variables:
                    line = f"{key}: {template_variables[key.strip().lower()]}\n"
            modified_lines.append(line)
        modified_lines.extend(file_lines[len(modified_lines):])
        with open(file_to_modify, 'w') as f:
            f.writelines(modified_lines)

if __name__ == '__main__':
    modify_files()
