# Smart Folder Organizer Skill

Automatically organizes cluttered folders by categorizing files, identifying duplicates, and renaming PDF documents like invoices and receipts based on their content.

## Features

- **Smart Folder Recognition**: Detects well-organized subdirectories (git repos, project roots, app bundles) and moves them to `Others/` instead of breaking them apart.
- **Duplicate Detection**: Deterministically finds and moves identical files to a `to_remove/` folder.
- **Categorization**: Automatically sorts files into `Photos/`, `Videos/`, `Installers/`, `Archives/`, etc.
- **Deep PDF Analysis**: Extracts metadata from PDFs (invoices, bills, receipts) and renames them using a standard format (`yyyy-mm-dd-[Vendor]-[Inv#]-[Amount].pdf`).
- **Safety First**: Never deletes files; moves candidates for deletion to `to_remove/`.

## Installation

You can add this skill to your workspace using the `skills-cli`:

```bash
npx skills add https://github.com/congyuan/smart-folder-organizer-skill
```

## Requirements

- Python 3.x
- `pypdf` (installed automatically via `requirements.txt`)

## Usage

Once added, your agent can use this skill to organize any directory. The core mandates ensure that it only operates within the target directory and prioritizes data safety.

### Using with Gemini CLI

After adding the skill to your project, you can use it directly from your terminal. Simply navigate to the folder you want to tidy up and run:

```bash
gemini "organise this folder"
```

You can also run `gemini` in interactive mode and use prompts like:

- "Please organize my current folder."
- "Categorize the files in the Downloads directory."
- "Find and remove duplicates in this folder."

The agent will automatically utilize the smart-folder-organizer skill to complete your request safely.

## Roadmap

- [ ] **Git Integration for Safe Rollbacks**: Automatically initialize a local git repository before organizing, allowing users to easily undo changes if they are unhappy with the result.
- [x] **Smart Folder Recognition**: Detect subfolders that are already well-organized (e.g., project directories, self-contained apps) and move them to an `Others/` directory.
- [ ] **Detailed Documentation**: Further explain the tool's inner workings, detailing exactly how each file type (especially PDFs) is processed and categorized.
- [ ] **Test Data Repository**: Create a `data/` folder containing sample files and test data in various languages to thoroughly test and improve multi-language file categorization and PDF text extraction.

## License

MIT
