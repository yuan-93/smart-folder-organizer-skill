# Smart Folder Organizer Skill

Automatically organizes cluttered folders by categorizing files, identifying duplicates, and renaming PDF documents like invoices and receipts based on their content.

## Features

- **Smart Folder Recognition**: Detects well-organized subdirectories (git repos, project roots like `package.json` or `Cargo.toml`, and macOS app bundles) and moves them to `Others/` instead of breaking them apart.
- **Duplicate Detection**: Deterministically finds and moves identical files to a `to_remove/duplicates/` folder using SHA-256 hashing.
- **Categorization**: Automatically sorts files into structured directories:
  - **Media**: `Photos/` (with `Screenshots/` subfolder), `Videos/`, and `Audio/`.
  - **Documents**: `Documents/Writing/`, `Documents/Spreadsheets/`, and `Documents/Presentations/`.
  - **System**: `Installers/` (`.dmg`, `.pkg`, `.exe`, `.msi`) and `Archives/` (`.zip`, `.rar`, etc.).
- **Deep PDF Analysis**: Uses modern AI (via `docling`) for universal semantic reasoning to categorize and rename documents:
  - **Invoices**: `yyyy-mm-dd-[Vendor]-[Inv#]-[Amount].pdf`
  - **Bills**: `yyyy-mm-dd-[Provider]-[Service]-[Account#].pdf`
  - **Receipts**: `yyyy-mm-dd-[Store]-[TotalAmount].pdf`
  - **Travel**: `yyyy-mm-dd-[Transport/Hotel]-[Confirmation#].pdf`
- **Safety First**:
  - Never deletes files; moves candidates to `to_remove/`.
  - Files larger than 20MB are moved to `Needs_Review/LargeFiles/` to ensure performance.
  - Ambiguous files are moved to `Needs_Review/` instead of guessing.
- **Multilingual Support**: Extracts vendor names and details in their original script (e.g., Chinese, Spanish) while maintaining standard date formats.

## Installation

You can add this skill to your workspace using the `skills-cli`:

```bash
npx skills add https://github.com/yuan-93/smart-folder-organizer-skill
```

## Requirements

- Python 3.x
- `docling` (installed automatically via `requirements.txt`)

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

- [x] **Smart Folder Recognition**: Detect subfolders that are already well-organized (e.g., project directories, self-contained apps) and move them to an `Others/` directory.
- [x] **Detailed Documentation**: Comprehensive breakdown of logic in `SKILL.md` and `classification.md`.
- [ ] **Git Integration for Safe Rollbacks**: Automatically initialize a local git repository before organizing, allowing users to easily undo changes if they are unhappy with the result.
- [ ] **Test Data Repository**: Create a `data/` folder containing sample files and test data in various languages to thoroughly test and improve multi-language file categorization and PDF text extraction.

## License

MIT
