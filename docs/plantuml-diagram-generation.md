# PlantUML Diagram Generation Guide

This guide explains how to generate PNG diagrams from PlantUML source files using the PlantUML JAR included in this repository.

## Prerequisites

- Java Runtime Environment (JRE) installed on your system
- PlantUML JAR file located at `common/plantuml/plantuml.jar`

## Basic Usage

### Generate PNG from PUML file

```bash
java -jar common/plantuml/plantuml.jar path/to/diagram.puml
```

This will create a PNG file in the same directory as the source file with the same name (e.g., `diagram.png`).

### Generate PNG with custom output directory

```bash
java -jar common/plantuml/plantuml.jar -o output_directory path/to/diagram.puml
```

### Generate PNG with custom output name

```bash
java -jar common/plantuml/plantuml.jar path/to/diagram.puml -o path/to/output.png
```

## Advanced Options

### Specify output format explicitly

```bash
java -jar common/plantuml/plantuml.jar -tpng path/to/diagram.puml
```

Available formats: `-tpng`, `-tsvg`, `-tpdf`, `-ttxt`

### Generate multiple diagrams at once

```bash
java -jar common/plantuml/plantuml.jar directory/**/*.puml
```

### Set DPI for higher resolution

```bash
java -DPLANTUML_LIMIT_SIZE=8192 -jar common/plantuml/plantuml.jar path/to/diagram.puml
```

### Generate with verbose output

```bash
java -jar common/plantuml/plantuml.jar -v path/to/diagram.puml
```

## Common Workflows

### Workflow 1: Generate diagram for PR assignment

```bash
# Example: Generate C4 Context diagram for PR1
cd pr1/diagrams
java -jar ../../common/plantuml/plantuml.jar context.puml
```

This creates `context.png` in the `pr1/diagrams/` directory.

### Workflow 2: Regenerate all diagrams in a PR

```bash
# Example: Regenerate all PlantUML diagrams for PR2
java -jar common/plantuml/plantuml.jar pr2/diagrams/*.puml
```

### Workflow 3: Generate with specific resolution

For high-quality diagrams suitable for reports:

```bash
java -DPLANTUML_LIMIT_SIZE=16384 -jar common/plantuml/plantuml.jar -tpng path/to/diagram.puml
```

## Troubleshooting

### Error: "Cannot find or load main class"

Ensure Java is installed and in your PATH:

```bash
java -version
```

### Error: "File not found"

Check that the PlantUML JAR exists:

```bash
ls -l common/plantuml/plantuml.jar
```

### Diagram is cut off or incomplete

Increase the size limit:

```bash
java -DPLANTUML_LIMIT_SIZE=16384 -jar common/plantuml/plantuml.jar path/to/diagram.puml
```

## Integration with Project Workflow

After generating PNG diagrams:

1. **Review**: Check the generated PNG for correctness
2. **Include in report**: Reference the PNG in your Word document
3. **Commit**: Add both `.puml` source and `.png` output to git

```bash
git add pr*/diagrams/*.puml pr*/diagrams/*.png
git commit -m "Add/Update PlantUML diagrams for PR*"
git push
```

## PlantUML Syntax Resources

- Official documentation: https://plantuml.com/
- C4 Model extension: https://github.com/plantuml-stdlib/C4-PlantUML
- Real World PlantUML examples: https://real-world-plantuml.com/

## Tips

1. **Keep source files**: Always commit `.puml` source files alongside generated `.png` files
2. **Use meaningful names**: Name diagrams descriptively (e.g., `c4-context.puml`, `use-case-diagram.puml`)
3. **Version control**: Regenerate PNGs after any changes to PUML sources
4. **Resolution**: Use higher DPI for final report submissions
5. **Preview**: Use online PlantUML editors for quick syntax validation before generating locally
