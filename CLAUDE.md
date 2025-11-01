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
└── task/
    └── README.md
```

- `task/` - directory with assignment and solution
- `README.md` - assignment description, implementation process, and results

## Workflow

1. For each laboratory work, materials are placed in the corresponding `labN/task/` directory
2. Use PlantUML from `/common/plantuml/` to create diagrams
3. Follow the recommendations from `/docs/` for work formatting
4. All changes are committed through Git

## Tools

- **PlantUML** - for creating UML diagrams
- **Git** - version control system
- Style templates for consistent documentation formatting

## Language Policy

All content in this project (documentation, code, comments, commit messages) must be written in English to maintain consistency and professional standards.
