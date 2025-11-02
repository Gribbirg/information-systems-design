# Information Systems Design Project Structure

## Project Guidelines

**IMPORTANT: All project-related communication, documentation, code comments, commit messages, and file content MUST be strictly in English.**

## Description
This project contains materials and practical assignments for the "Information Systems Design" course.

**Project Theme:** SportRent - Sports Equipment Rental Management System

See [Project Overview](docs/project-overview.md) for detailed information about the SportRent system.

## Directory Structure

### Root Directory
- `README.md` - main project description
- `CLAUDE.md` - project structure documentation (this file)
- `.gitignore` - files and directories ignored by Git

### `/common`
Shared resources and tools for all laboratory works:
- `plantuml/` - PlantUML tools for diagram generation
  - `plantuml.jar` - PlantUML JAR file
- `style_source.docx` - style template for reports

### `/docs`
Documentation and guidelines:
- `project-overview.md` - SportRent system description and objectives
- `plantuml-diagram-generation.md` - diagram generation instructions
- `report-formatting-guidelines.md` - report formatting guidelines

### `/lab1` - `/lab8`
Directories for practical assignments (laboratory works 1-8).

Each laboratory work has the following structure:
```
labN/
├── task/
│   └── README.md
├── solutions/
│   ├── diagrams/
│   └── report-draft.md
└── report/
    ├── report.md
    └── report.docx
```

- `task/` - directory with assignment requirements, implementation process, and working materials
  - `README.md` - assignment description, implementation details, and results
- `solutions/` - directory for work-in-progress materials and solutions
  - `diagrams/` - all created diagrams (PlantUML source files and generated images)
  - `report-draft.md` - draft report in plain Markdown style (without Pandoc formatting)
- `report/` - directory for final formatted reports ready for submission
  - `report.md` - final report with Pandoc formatting and metadata
  - `report.docx` - converted Word document ready for submission

## Workflow

When working on a laboratory assignment, follow these steps in order:

### Step 1: Create Diagrams
1. Create all necessary diagrams in `labN/solutions/diagrams/` directory
2. Use PlantUML from `/common/plantuml/` to create UML diagrams
3. Generate PNG/SVG images from PlantUML source files
4. Save both source files (`.puml`) and generated images (`.png`) in `solutions/diagrams/`

### Step 2: Create Report Draft
1. Create `labN/solutions/report-draft.md` in plain Markdown style
2. Include all content: theoretical part, practical part, descriptions, glossary, answers
3. Use standard Markdown syntax without Pandoc-specific features
4. Reference diagrams using relative paths: `![Diagram](diagrams/diagram-name.png)`

### Step 3: Create Final Report with Pandoc
1. Create `labN/report/report.md` with Pandoc formatting
2. Add YAML metadata header with title, author, date, and formatting options
3. Follow recommendations from `/docs/report-formatting-guidelines.md`
4. Use Pandoc-specific features (page breaks, custom styles, etc.)
5. Reference diagrams from `../solutions/diagrams/`
6. **IMPORTANT:** Use only ONE first-level heading (H1) with the lab work title at the beginning of the report
   - All other sections MUST use second-level headings (H2) or lower
   - This ensures proper structure when reports are combined into a single document
   - Example: `# Практическая работа № 2` (only once), then `## Цель работы`, `## Теоретическая часть`, etc.

### Step 4: Convert to DOCX
1. Use Pandoc to convert `labN/report/report.md` to `labN/report/report.docx`
2. Apply style template from `/common/style_source.docx` if needed
3. Verify formatting in the generated DOCX file
4. The DOCX file is ready for submission

### Step 5: Commit Changes
1. Commit all changes to Git with descriptive commit message in English
2. Push changes to remote repository

## Tools

- **PlantUML** - for creating UML diagrams
- **Git** - version control system
- Style templates for consistent documentation formatting

## Language Policy

**Git Commit Messages:** All commit messages MUST be written in English to maintain professional standards.

**Laboratory Work Documentation:** All practical work documentation, reports, diagrams, and content within `labN/task/` and `labN/report/` directories MUST be written in Russian. This includes:
- Requirements documentation
- Technical specifications
- PlantUML diagrams (labels, descriptions, comments)
- Reports and analyses
- Any working materials

**Project Documentation:** General project documentation in `/docs/` directory should be in English for consistency.

**Communication Language:** All communication with the user and task execution MUST be strictly in Russian. Claude should respond to the user in Russian and discuss implementation details in Russian.
