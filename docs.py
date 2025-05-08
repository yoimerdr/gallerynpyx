import os

input_folder = 'gallerynpyx'
output_folder = 'docs/source/modules'
new_extension = '.rst'

for dirpath, _, filenames in os.walk(input_folder):
    for filename in filenames:
        if filename.startswith('_'):
            continue

        input_path = os.path.join(dirpath, filename)

        if not os.path.isfile(input_path):
            continue

        relative_path = os.path.relpath(dirpath, input_folder)
        output_dir = os.path.join(output_folder, relative_path)

        os.makedirs(output_dir, exist_ok=True)

        name_base, _ = os.path.splitext(filename)
        new_filename = name_base + new_extension
        output_path = os.path.join(output_dir, new_filename)

        if not os.path.exists(output_path):
            with open(output_path, 'w') as f:
                f.write(f"{name_base}\n{'-' * len(name_base)}\n")
            print(f'Archivo creado: {output_path}')
        else:
            print(f'Ya existe: {output_path}')
