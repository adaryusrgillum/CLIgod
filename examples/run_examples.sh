#!/bin/bash
# Example 1: Basic usage
echo "Example 1: Basic content creation"
cligod create "Artificial Intelligence in Education"

echo -e "\n\n"

# Example 2: With citation style
echo "Example 2: Using MLA citation style"
cligod create "Climate Change Impact on Coastal Cities" --citation-style MLA

echo -e "\n\n"

# Example 3: Platform-specific
echo "Example 3: LinkedIn content"
cligod create "Professional Development in Tech Industry" --platform linkedin

echo -e "\n\n"

# Example 4: Save to file
echo "Example 4: Save output to file"
cligod create "The Future of Cryptocurrency" --output examples/crypto-content.json

echo -e "\n\n"

# Example 5: Verbose mode
echo "Example 5: Verbose mode (all stages)"
cligod create "Remote Work Best Practices" --verbose --output examples/remote-work.json

echo -e "\n\n"

# Example 6: Complete example with all options
echo "Example 6: Complete example"
cligod create "Sustainable Technology Solutions for Smart Cities" \
  --citation-style APA \
  --platform linkedin \
  --output examples/smart-cities.json \
  --verbose
