# Organize Folder Skill

Automatically organizes cluttered folders by categorizing files, identifying duplicates, and renaming PDF documents like invoices and receipts based on their content.

## Features

- **Duplicate Detection**: Deterministically finds and moves identical files to a `to_remove/` folder.
- **Categorization**: Automatically sorts files into `Photos/`, `Videos/`, `Installers/`, `Archives/`, etc.
- **Deep PDF Analysis**: Extracts metadata from PDFs (invoices, bills, receipts) and renames them using a standard format (`yyyy-mm-dd-[Vendor]-[Inv#]-[Amount].pdf`).
- **Safety First**: Never deletes files; moves candidates for deletion to `to_remove/`.

## Installation

You can add this skill to your workspace using the `skills-cli`:

```bash
npx skills add https://github.com/congyuan/organise-folder-skill
```

## Requirements

- Python 3.x
- `pypdf` (installed automatically via `requirements.txt`)

## Usage

Once added, your agent can use this skill to organize any directory. The core mandates ensure that it only operates within the target directory and prioritizes data safety.

## License

MIT
