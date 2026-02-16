# CLIgod Examples

This directory contains example usage and output files for CLIgod.

## Running Examples

Make the script executable and run it:

```bash
chmod +x examples/run_examples.sh
./examples/run_examples.sh
```

## Example Commands

### 1. Basic Usage
```bash
cligod create "Artificial Intelligence in Education"
```

### 2. Specify Citation Style
```bash
cligod create "Climate Change Impact" --citation-style MLA
```

### 3. Target Specific Platform
```bash
cligod create "Professional Development" --platform linkedin
```

### 4. Save Output
```bash
cligod create "Cryptocurrency Future" --output crypto-content.json
```

### 5. Verbose Mode
```bash
cligod create "Remote Work Tips" --verbose
```

### 6. Complete Example
```bash
cligod create "Smart Cities Technology" \
  --citation-style APA \
  --platform linkedin \
  --output smart-cities.json \
  --verbose
```

## Sample Topics

Try these trending topics:

- "AI Ethics and Responsible AI Development"
- "Quantum Computing Applications in 2024"
- "Sustainable Energy Solutions for Urban Areas"
- "The Future of Work: Hybrid vs Remote"
- "Blockchain Technology Beyond Cryptocurrency"
- "Mental Health in the Digital Age"
- "5G Technology and IoT Innovation"
- "Cybersecurity Trends for Small Businesses"
- "Green Technology in Manufacturing"
- "EdTech Tools for Modern Classrooms"

## Output Files

After running examples, this directory will contain:

- `*.json` - Full pipeline output with all stages
- `*.md` - Final polished content only

## Tips

1. **Start Simple**: Begin with basic commands to understand the flow
2. **Use Verbose**: Add `--verbose` to see how each stage transforms content
3. **Experiment**: Try different citation styles and platforms
4. **Compare**: Save outputs and compare different approaches
5. **Iterate**: Use failed quality gates as learning opportunities
