## CHAIN OF CUSTODY TOOL

Purpose: The Chain of Custody Tool records critical information about evidence gathered during
an investigation, documenting details about each piece of evidence, including whenever the
evidence is transferred or changes hands. The chain of custody is an important part of the
structured and transparent and fair principles in SEAH investigations.

How to use this tool: When investigators gather evidence (physical evidence, documents,
electronic records etc.), they must record the name of the person from whom the item was
obtained, and the name of the person who obtained it, along with the signature of both); the
date it was obtained; and the investigation case number. As many details about the piece of
evidence should be included. Additional information on the chain of custody can be found in
section 3.2.1.1 of the Sexual Exploitation, Abuse, and Harassment Investigation Guide .

Definition of key components

- Substantiated: The individual from whom investigators received the evidence.

- Temporary disposition of item: The location where the item is stored during the investigation.

- Released by: When evidence is transferred, moved, or changes hands, the individual who
provides the evidence or releases the evidence.

- Released to: When evidence is transferred, moved, or changes hands, the individual to whom
the evidence is provided.

| Description of item (model, serial number, type, and name of document) WhatsApp and SMS messages from December 2021, January 2022, February 2022 Android phone, model 11223344. |  |  |
| --- | --- | --- |
| Obtained from: (Name, title, office, location) Adam Mee, IT Manager, ThriveBridge NGO Regional Office, Escar |  |  |
| Printed name of investigator: Kamran Bee | Signature of investigator: | Date obtained: |
| Case number: 123456789 |  |  |
| Temporary disposition of item(s) (where stored): |  |  |
| Released by: (printed name and signature) | Released to: (printed name and signature) | Date: |

---

<!-- Page 2 -->
| Temporary disposition of item(s): (where stored) |  |  |
| --- | --- | --- |
| Released by: (printed name and signature) | Released to: (printed name and signature) | Date: |
| Temporary disposition of item(s): (where stored) |  |  |
| Released by: (printed name and signature) | Released to: (printed name and signature) | Date: |-e 

---

## EVIDENCE EVALUATION MATRIX TOOL

Purpose: The Evidence Evaluation Matrix Tool helps investigators compile and organize different
sources and types of evidence related in one structured table. Investigators use this tool to
validate the logic of evidence and highlight alignment and contradictions where they become
apparent.

How to use this tool: Investigators should outline the complaint in the first column. As evidence
related to the complaint is gathered, it should be described and divided by the type of evidence
as demonstrated in the table below. More information about the evidence evaluation tool
can be found in section 3.2.1 of the Sexual Exploitation, Abuse and Harassment (SEAH)
Investigation Guide.

| Complaint | Evidence |  |  |  |
| --- | --- | --- | --- | --- |
|  | Testimony | Documentary | Physical | Digital |
| 1. Subject of Complaint threatened to withhold aid if survivor did not agree to engage in sexual acts with the Subject of Complaint. If the survivor engaged in sexual acts the Subject of Complaint offered to provide extra food vouchers to the survivor. | Survivor, Rachel Phee: “He approached me the week of January 20 2022, as I was waiting in line to receive my food vouchers. He pulled me aside and told me he would make sure I did not receive any more vouchers unless I had sex with him. He also mentioned if I did have sex with him, he would give me four additional food vouchers per month and add different family members to the distribution list so no one would suspect we were getting four times the vouchers that other families were.” | Distribution records show that the December and January distributions contain one verified entry for the Phee family household. February distribution records contain five verified entries for the Phee family. | None | Survivor provided WhatsApp messages between herself and Subject of Complaint. Messages stated: 26/01/2022: “You need to meet me at the place we agreed by 8pm. Remember, don’t tell anyone and I will make sure your family gets extra vouchers.” 03/02/2022 “Meet me on the west side of the distribution site to get the food vouchers. Do not tell anyone you are meeting me and make sure no one sees you.” |-e 

---

## TABLE OF FINDINGS TOOL

Purpose: The Table of Findings Tool helps investigators organise evidence according to whether
it supports the complaint or does not support the complaint. Once categorised, investigators
can determine to what extent the evidence meets the standard of proof required for the
investigation.

How to use this tool: Investigators compile all evidence gathered during the investigation and
categorise it according to whether it is inculpatory or exculpatory. Depending on the standard of
proof required, investigators will then determine the findings and conclude that the complaint is
one of the following:

- Substantiated: a complaint is substantiated when there is sufficient evidence that it is more
likely than not that the behaviour occurred.

- Unsubstantiated: a complaint is unsubstantiated when the investigation cannot meet the
burden of proof to substantiate the complaint, or the investigation proves that the behaviour
did not occur.

- Inconclusive: a complaint is inconclusive if the investigation is unable to determine whether
the complaint can be substantiated.

Definition of key components

- Inculpatory evidence: Evidence that supports the complaint.

- Exculpatory evidence: Evidence that does not support the complaint.

| Relevant policy or code of conduct: United Nations Secretary General’s Bulletin, Special measures for protection from sexual exploitation and abuse | Inculpatory evidence | Exculpatory evidence |
| --- | --- | --- |
| Complaint: Subject of Complaint threatened to withhold aid if survivor did not agree to engage in sexual acts with the Subject of Complaint. If the survivor engaged in sexual acts the Subject of Complaint offered to provide extra food vouchers to the survivor. | Interview with driver at ThriveBridge NGO: Driver stated that he witnessed the Subject of Complaint speaking with and touching the survivor during a distribution in January 2022. | Interview with Subject of Complaint: Repeatedly stated during the interview that he had no contact with the survivor and did not engage in exploitative behaviour. |
|  | Interview with Survivor: Survivor stated the Subject of Complaint approached her in January 2022 and offered additional food vouchers for her family if she had sex with him. |  |

---

<!-- Page 2 -->
| Relevant policy or code of conduct: United Nations Secretary General’s Bulletin, Special measures for protection from sexual exploitation and abuse | Inculpatory evidence | Exculpatory evidence |
| --- | --- | --- |
|  | WhatsApp Messages: Messages between the survivor and Subject of Complaint indicate that there was an arrangement to meet at an agreed location at 8pm on 26 January 2021. On 3 February 2022, the Subject of Complaint messaged the survivor telling her to meet him to obtain the extra food vouchers. |  |
|  | Food Distribution Records: Distribution records show that the December and January distributions contain a verified entry for the survivor’s family household. February distribution records contain five verified entries for the survivor’s family. |  |-e 

---

# MarkItDown - File to Markdown Conversion

## Overview

MarkItDown is a Python tool developed by Microsoft for converting various file formats to Markdown. It's particularly useful for converting documents into LLM-friendly text format, as Markdown is token-efficient and well-understood by modern language models.

**Key Benefits**:
- Convert documents to clean, structured Markdown
- Token-efficient format for LLM processing
- Supports 15+ file formats
- Optional AI-enhanced image descriptions
- OCR for images and scanned documents
- Speech transcription for audio files

## Visual Enhancement with Scientific Schematics

**When creating documents with this skill, always consider adding scientific diagrams and schematics to enhance visual communication.**

If your document does not already contain schematics or diagrams:
- Use the **scientific-schematics** skill to generate AI-powered publication-quality diagrams
- Simply describe your desired diagram in natural language
- Nano Banana Pro will automatically generate, review, and refine the schematic

**For new documents:** Scientific schematics should be generated by default to visually represent key concepts, workflows, architectures, or relationships described in the text.

**How to generate schematics:**
```bash
python scripts/generate_schematic.py "your diagram description" -o figures/output.png
```

The AI will automatically:
- Create publication-quality images with proper formatting
- Review and refine through multiple iterations
- Ensure accessibility (colorblind-friendly, high contrast)
- Save outputs in the figures/ directory

**When to add schematics:**
- Document conversion workflow diagrams
- File format architecture illustrations
- OCR processing pipeline diagrams
- Integration workflow visualizations
- System architecture diagrams
- Data flow diagrams
- Any complex concept that benefits from visualization

For detailed guidance on creating schematics, refer to the scientific-schematics skill documentation.

---

## Supported Formats

| Format | Description | Notes |
|--------|-------------|-------|
| **PDF** | Portable Document Format | Full text extraction |
| **DOCX** | Microsoft Word | Tables, formatting preserved |
| **PPTX** | PowerPoint | Slides with notes |
| **XLSX** | Excel spreadsheets | Tables and data |
| **Images** | JPEG, PNG, GIF, WebP | EXIF metadata + OCR |
| **Audio** | WAV, MP3 | Metadata + transcription |
| **HTML** | Web pages | Clean conversion |
| **CSV** | Comma-separated values | Table format |
| **JSON** | JSON data | Structured representation |
| **XML** | XML documents | Structured format |
| **ZIP** | Archive files | Iterates contents |
| **EPUB** | E-books | Full text extraction |
| **YouTube** | Video URLs | Fetch transcriptions |

## Quick Start

### Installation

```bash
# Install with all features
pip install 'markitdown[all]'

# Or from source
git clone https://github.com/microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

### Command-Line Usage

```bash
# Basic conversion
markitdown document.pdf > output.md

# Specify output file
markitdown document.pdf -o output.md

# Pipe content
cat document.pdf | markitdown > output.md

# Enable plugins
markitdown --list-plugins  # List available plugins
markitdown --use-plugins document.pdf -o output.md
```

### Python API

```python
from markitdown import MarkItDown

# Basic usage
md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)

# Convert from stream
with open("document.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
    print(result.text_content)
```

## Advanced Features

### 1. AI-Enhanced Image Descriptions

Use LLMs via OpenRouter to generate detailed image descriptions (for PPTX and image files):

```python
from markitdown import MarkItDown
from openai import OpenAI

# Initialize OpenRouter client (OpenAI-compatible API)
client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-opus-4.5",  # recommended for scientific vision
    llm_prompt="Describe this image in detail for scientific documentation"
)

result = md.convert("presentation.pptx")
print(result.text_content)
```

### 2. Azure Document Intelligence

For enhanced PDF conversion with Microsoft Document Intelligence:

```bash
# Command line
markitdown document.pdf -o output.md -d -e "<document_intelligence_endpoint>"
```

```python
# Python API
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert("complex_document.pdf")
print(result.text_content)
```

### 3. Plugin System

MarkItDown supports 3rd-party plugins for extending functionality:

```bash
# List installed plugins
markitdown --list-plugins

# Enable plugins
markitdown --use-plugins file.pdf -o output.md
```

Find plugins on GitHub with hashtag: `#markitdown-plugin`

## Optional Dependencies

Control which file formats you support:

```bash
# Install specific formats
pip install 'markitdown[pdf, docx, pptx]'

# All available options:
# [all]                  - All optional dependencies
# [pptx]                 - PowerPoint files
# [docx]                 - Word documents
# [xlsx]                 - Excel spreadsheets
# [xls]                  - Older Excel files
# [pdf]                  - PDF documents
# [outlook]              - Outlook messages
# [az-doc-intel]         - Azure Document Intelligence
# [audio-transcription]  - WAV and MP3 transcription
# [youtube-transcription] - YouTube video transcription
```

## Common Use Cases

### 1. Convert Scientific Papers to Markdown

```python
from markitdown import MarkItDown

md = MarkItDown()

# Convert PDF paper
result = md.convert("research_paper.pdf")
with open("paper.md", "w") as f:
    f.write(result.text_content)
```

### 2. Extract Data from Excel for Analysis

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("data.xlsx")

# Result will be in Markdown table format
print(result.text_content)
```

### 3. Process Multiple Documents

```python
from markitdown import MarkItDown
import os
from pathlib import Path

md = MarkItDown()

# Process all PDFs in a directory
pdf_dir = Path("papers/")
output_dir = Path("markdown_output/")
output_dir.mkdir(exist_ok=True)

for pdf_file in pdf_dir.glob("*.pdf"):
    result = md.convert(str(pdf_file))
    output_file = output_dir / f"{pdf_file.stem}.md"
    output_file.write_text(result.text_content)
    print(f"Converted: {pdf_file.name}")
```

### 4. Convert PowerPoint with AI Descriptions

```python
from markitdown import MarkItDown
from openai import OpenAI

# Use OpenRouter for access to multiple AI models
client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-opus-4.5",  # recommended for presentations
    llm_prompt="Describe this slide image in detail, focusing on key visual elements and data"
)

result = md.convert("presentation.pptx")
with open("presentation.md", "w") as f:
    f.write(result.text_content)
```

### 5. Batch Convert with Different Formats

```python
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()

# Files to convert
files = [
    "document.pdf",
    "spreadsheet.xlsx",
    "presentation.pptx",
    "notes.docx"
]

for file in files:
    try:
        result = md.convert(file)
        output = Path(file).stem + ".md"
        with open(output, "w") as f:
            f.write(result.text_content)
        print(f"✓ Converted {file}")
    except Exception as e:
        print(f"✗ Error converting {file}: {e}")
```

### 6. Extract YouTube Video Transcription

```python
from markitdown import MarkItDown

md = MarkItDown()

# Convert YouTube video to transcript
result = md.convert("https://www.youtube.com/watch?v=VIDEO_ID")
print(result.text_content)
```

## Docker Usage

```bash
# Build image
docker build -t markitdown:latest .

# Run conversion
docker run --rm -i markitdown:latest < ~/document.pdf > output.md
```

## Best Practices

### 1. Choose the Right Conversion Method

- **Simple documents**: Use basic `MarkItDown()`
- **Complex PDFs**: Use Azure Document Intelligence
- **Visual content**: Enable AI image descriptions
- **Scanned documents**: Ensure OCR dependencies are installed

### 2. Handle Errors Gracefully

```python
from markitdown import MarkItDown

md = MarkItDown()

try:
    result = md.convert("document.pdf")
    print(result.text_content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Conversion error: {e}")
```

### 3. Process Large Files Efficiently

```python
from markitdown import MarkItDown

md = MarkItDown()

# For large files, use streaming
with open("large_file.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
    
    # Process in chunks or save directly
    with open("output.md", "w") as out:
        out.write(result.text_content)
```

### 4. Optimize for Token Efficiency

Markdown output is already token-efficient, but you can:
- Remove excessive whitespace
- Consolidate similar sections
- Strip metadata if not needed

```python
from markitdown import MarkItDown
import re

md = MarkItDown()
result = md.convert("document.pdf")

# Clean up extra whitespace
clean_text = re.sub(r'\n{3,}', '\n\n', result.text_content)
clean_text = clean_text.strip()

print(clean_text)
```

## Integration with Scientific Workflows

### Convert Literature for Review

```python
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()

# Convert all papers in literature folder
papers_dir = Path("literature/pdfs")
output_dir = Path("literature/markdown")
output_dir.mkdir(exist_ok=True)

for paper in papers_dir.glob("*.pdf"):
    result = md.convert(str(paper))
    
    # Save with metadata
    output_file = output_dir / f"{paper.stem}.md"
    content = f"# {paper.stem}\n\n"
    content += f"**Source**: {paper.name}\n\n"
    content += "---\n\n"
    content += result.text_content
    
    output_file.write_text(content)

# For AI-enhanced conversion with figures
from openai import OpenAI

client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

md_ai = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-opus-4.5",
    llm_prompt="Describe scientific figures with technical precision"
)
```

### Extract Tables for Analysis

```python
from markitdown import MarkItDown
import re

md = MarkItDown()
result = md.convert("data_tables.xlsx")

# Markdown tables can be parsed or used directly
print(result.text_content)
```

## Troubleshooting

### Common Issues

1. **Missing dependencies**: Install feature-specific packages
   ```bash
   pip install 'markitdown[pdf]'  # For PDF support
   ```

2. **Binary file errors**: Ensure files are opened in binary mode
   ```python
   with open("file.pdf", "rb") as f:  # Note the "rb"
       result = md.convert_stream(f, file_extension=".pdf")
   ```

3. **OCR not working**: Install tesseract
   ```bash
   # macOS
   brew install tesseract
   
   # Ubuntu
   sudo apt-get install tesseract-ocr
   ```

## Performance Considerations

- **PDF files**: Large PDFs may take time; consider page ranges if supported
- **Image OCR**: OCR processing is CPU-intensive
- **Audio transcription**: Requires additional compute resources
- **AI image descriptions**: Requires API calls (costs may apply)

## Next Steps

- See `references/api_reference.md` for complete API documentation
- Check `references/file_formats.md` for format-specific details
- Review `scripts/batch_convert.py` for automation examples
- Explore `scripts/convert_with_ai.py` for AI-enhanced conversions

## Resources

- **MarkItDown GitHub**: https://github.com/microsoft/markitdown
- **PyPI**: https://pypi.org/project/markitdown/
- **OpenRouter**: https://openrouter.ai (for AI-enhanced conversions)
- **OpenRouter API Keys**: https://openrouter.ai/keys
- **OpenRouter Models**: https://openrouter.ai/models
- **MCP Server**: markitdown-mcp (for Claude Desktop integration)
- **Plugin Development**: See `packages/markitdown-sample-plugin`


