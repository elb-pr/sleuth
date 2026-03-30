# MarkItDown API Reference

## Core Classes

### MarkItDown

The main class for converting files to Markdown.

```python
from markitdown import MarkItDown

md = MarkItDown(
    llm_client=None,
    llm_model=None,
    llm_prompt=None,
    docintel_endpoint=None,
    enable_plugins=False
)
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `llm_client` | OpenAI client | `None` | OpenAI-compatible client for AI image descriptions |
| `llm_model` | str | `None` | Model name (e.g., "anthropic/claude-opus-4.5") for image descriptions |
| `llm_prompt` | str | `None` | Custom prompt for image description |
| `docintel_endpoint` | str | `None` | Azure Document Intelligence endpoint |
| `enable_plugins` | bool | `False` | Enable 3rd-party plugins |

#### Methods

##### convert()

Convert a file to Markdown.

```python
result = md.convert(
    source,
    file_extension=None
)
```

**Parameters**:
- `source` (str): Path to the file to convert
- `file_extension` (str, optional): Override file extension detection

**Returns**: `DocumentConverterResult` object

**Example**:
```python
result = md.convert("document.pdf")
print(result.text_content)
```

##### convert_stream()

Convert from a file-like binary stream.

```python
result = md.convert_stream(
    stream,
    file_extension
)
```

**Parameters**:
- `stream` (BinaryIO): Binary file-like object (e.g., file opened in `"rb"` mode)
- `file_extension` (str): File extension to determine conversion method (e.g., ".pdf")

**Returns**: `DocumentConverterResult` object

**Example**:
```python
with open("document.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
    print(result.text_content)
```

**Important**: The stream must be opened in binary mode (`"rb"`), not text mode.

## Result Object

### DocumentConverterResult

The result of a conversion operation.

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `text_content` | str | The converted Markdown text |
| `title` | str | Document title (if available) |

#### Example

```python
result = md.convert("paper.pdf")

# Access content
content = result.text_content

# Access title (if available)
title = result.title
```

## Custom Converters

You can create custom document converters by implementing the `DocumentConverter` interface.

### DocumentConverter Interface

```python
from markitdown import DocumentConverter

class CustomConverter(DocumentConverter):
    def convert(self, stream, file_extension):
        """
        Convert a document from a binary stream.
        
        Parameters:
            stream (BinaryIO): Binary file-like object
            file_extension (str): File extension (e.g., ".custom")
            
        Returns:
            DocumentConverterResult: Conversion result
        """
        # Your conversion logic here
        pass
```

### Registering Custom Converters

```python
from markitdown import MarkItDown, DocumentConverter, DocumentConverterResult

class MyCustomConverter(DocumentConverter):
    def convert(self, stream, file_extension):
        content = stream.read().decode('utf-8')
        markdown_text = f"# Custom Format\n\n{content}"
        return DocumentConverterResult(
            text_content=markdown_text,
            title="Custom Document"
        )

# Create MarkItDown instance
md = MarkItDown()

# Register custom converter for .custom files
md.register_converter(".custom", MyCustomConverter())

# Use it
result = md.convert("myfile.custom")
```

## Plugin System

### Finding Plugins

Search GitHub for `#markitdown-plugin` tag.

### Using Plugins

```python
from markitdown import MarkItDown

# Enable plugins
md = MarkItDown(enable_plugins=True)
result = md.convert("document.pdf")
```

### Creating Plugins

Plugins are Python packages that register converters with MarkItDown.

**Plugin Structure**:
```
my-markitdown-plugin/
├── setup.py
├── my_plugin/
│   ├── __init__.py
│   └── converter.py
└── README.md
```

**setup.py**:
```python
from setuptools import setup

setup(
    name="markitdown-my-plugin",
    version="0.1.0",
    packages=["my_plugin"],
    entry_points={
        "markitdown.plugins": [
            "my_plugin = my_plugin.converter:MyConverter",
        ],
    },
)
```

**converter.py**:
```python
from markitdown import DocumentConverter, DocumentConverterResult

class MyConverter(DocumentConverter):
    def convert(self, stream, file_extension):
        # Your conversion logic
        content = stream.read()
        markdown = self.process(content)
        return DocumentConverterResult(
            text_content=markdown,
            title="My Document"
        )
    
    def process(self, content):
        # Process content
        return "# Converted Content\n\n..."
```

## AI-Enhanced Conversions

### Using OpenRouter for Image Descriptions

```python
from markitdown import MarkItDown
from openai import OpenAI

# Initialize OpenRouter client (OpenAI-compatible API)
client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

# Create MarkItDown with AI support
md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-opus-4.5",  # recommended for scientific vision
    llm_prompt="Describe this image in detail for scientific documentation"
)

# Convert files with images
result = md.convert("presentation.pptx")
```

### Available Models via OpenRouter

Popular models with vision support:
- `anthropic/claude-opus-4.5` - **Recommended for scientific vision**
- `google/gemini-3-pro-preview` - Gemini Pro Vision

See https://openrouter.ai/models for the complete list.

### Custom Prompts

```python
# For scientific diagrams
scientific_prompt = """
Analyze this scientific diagram or chart. Describe:
1. The type of visualization (graph, chart, diagram, etc.)
2. Key data points or trends
3. Labels and axes
4. Scientific significance
Be precise and technical.
"""

md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-opus-4.5",
    llm_prompt=scientific_prompt
)
```

## Azure Document Intelligence

### Setup

1. Create Azure Document Intelligence resource
2. Get endpoint URL
3. Set authentication

### Usage

```python
from markitdown import MarkItDown

md = MarkItDown(
    docintel_endpoint="https://YOUR-RESOURCE.cognitiveservices.azure.com/"
)

result = md.convert("complex_document.pdf")
```

### Authentication

Set environment variables:
```bash
export AZURE_DOCUMENT_INTELLIGENCE_KEY="your-key"
```

Or pass credentials programmatically.

## Error Handling

```python
from markitdown import MarkItDown

md = MarkItDown()

try:
    result = md.convert("document.pdf")
    print(result.text_content)
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print(f"Invalid file format: {e}")
except Exception as e:
    print(f"Conversion error: {e}")
```

## Performance Tips

### 1. Reuse MarkItDown Instance

```python
# Good: Create once, use many times
md = MarkItDown()

for file in files:
    result = md.convert(file)
    process(result)
```

### 2. Use Streaming for Large Files

```python
# For large files
with open("large_file.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
```

### 3. Batch Processing

```python
from concurrent.futures import ThreadPoolExecutor

md = MarkItDown()

def convert_file(filepath):
    return md.convert(filepath)

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(convert_file, file_list)
```

## Breaking Changes (v0.0.1 to v0.1.0)

1. **Dependencies**: Now organized into optional feature groups
   ```bash
   # Old
   pip install markitdown
   
   # New
   pip install 'markitdown[all]'
   ```

2. **convert_stream()**: Now requires binary file-like object
   ```python
   # Old (also accepted text)
   with open("file.pdf", "r") as f:  # text mode
       result = md.convert_stream(f)
   
   # New (binary only)
   with open("file.pdf", "rb") as f:  # binary mode
       result = md.convert_stream(f, file_extension=".pdf")
   ```

3. **DocumentConverter Interface**: Changed to read from streams instead of file paths
   - No temporary files created
   - More memory efficient
   - Plugins need updating

## Version Compatibility

- **Python**: 3.10 or higher required
- **Dependencies**: Check `setup.py` for version constraints
- **OpenAI**: Compatible with OpenAI Python SDK v1.0+

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENROUTER_API_KEY` | OpenRouter API key for image descriptions | `sk-or-v1-...` |
| `AZURE_DOCUMENT_INTELLIGENCE_KEY` | Azure DI authentication | `key123...` |
| `AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT` | Azure DI endpoint | `https://...` |

-e 

---

# MarkItDown Example Usage

This document provides practical examples of using MarkItDown in various scenarios.

## Basic Examples

### 1. Simple File Conversion

```python
from markitdown import MarkItDown

md = MarkItDown()

# Convert a PDF
result = md.convert("research_paper.pdf")
print(result.text_content)

# Convert a Word document
result = md.convert("manuscript.docx")
print(result.text_content)

# Convert a PowerPoint
result = md.convert("presentation.pptx")
print(result.text_content)
```

### 2. Save to File

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")

with open("output.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)
```

### 3. Convert from Stream

```python
from markitdown import MarkItDown

md = MarkItDown()

with open("document.pdf", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
    print(result.text_content)
```

## Scientific Workflows

### Convert Research Papers

```python
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()

# Convert all papers in a directory
papers_dir = Path("research_papers/")
output_dir = Path("markdown_papers/")
output_dir.mkdir(exist_ok=True)

for paper in papers_dir.glob("*.pdf"):
    result = md.convert(str(paper))
    
    # Save with original filename
    output_file = output_dir / f"{paper.stem}.md"
    output_file.write_text(result.text_content)
    
    print(f"Converted: {paper.name}")
```

### Extract Tables from Excel

```python
from markitdown import MarkItDown

md = MarkItDown()

# Convert Excel to Markdown tables
result = md.convert("experimental_data.xlsx")

# The result contains Markdown-formatted tables
print(result.text_content)

# Save for further processing
with open("data_tables.md", "w") as f:
    f.write(result.text_content)
```

### Process Presentation Slides

```python
from markitdown import MarkItDown
from openai import OpenAI

# With AI descriptions for images
client = OpenAI()
md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-sonnet-4.5",
    llm_prompt="Describe this scientific slide, focusing on data and key findings"
)

result = md.convert("conference_talk.pptx")

# Save with metadata
output = f"""# Conference Talk

{result.text_content}
"""

with open("talk_notes.md", "w") as f:
    f.write(output)
```

## AI-Enhanced Conversions

### Detailed Image Descriptions

```python
from markitdown import MarkItDown
from openai import OpenAI

# Initialize OpenRouter client
client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

# Scientific diagram analysis
scientific_prompt = """
Analyze this scientific figure. Describe:
- Type of visualization (graph, microscopy, diagram, etc.)
- Key data points and trends
- Axes, labels, and legends
- Scientific significance
Be technical and precise.
"""

md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-sonnet-4.5",  # recommended for scientific vision
    llm_prompt=scientific_prompt
)

# Convert paper with figures
result = md.convert("paper_with_figures.pdf")
print(result.text_content)
```

### Different Prompts for Different Files

```python
from markitdown import MarkItDown
from openai import OpenAI

# Initialize OpenRouter client
client = OpenAI(
    api_key="your-openrouter-api-key",
    base_url="https://openrouter.ai/api/v1"
)

# Scientific papers - use Claude for technical analysis
scientific_md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-sonnet-4.5",
    llm_prompt="Describe scientific figures with technical precision"
)

# Presentations - use GPT-4o for visual understanding
presentation_md = MarkItDown(
    llm_client=client,
    llm_model="anthropic/claude-sonnet-4.5",
    llm_prompt="Summarize slide content and key visual elements"
)

# Use appropriate instance for each file
paper_result = scientific_md.convert("research.pdf")
slides_result = presentation_md.convert("talk.pptx")
```

## Batch Processing

### Process Multiple Files

```python
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()

files_to_convert = [
    "paper1.pdf",
    "data.xlsx",
    "presentation.pptx",
    "notes.docx"
]

for file in files_to_convert:
    try:
        result = md.convert(file)
        output = Path(file).stem + ".md"
        
        with open(output, "w") as f:
            f.write(result.text_content)
        
        print(f"✓ {file} -> {output}")
    except Exception as e:
        print(f"✗ Error converting {file}: {e}")
```

### Parallel Processing

```python
from markitdown import MarkItDown
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def convert_file(filepath):
    md = MarkItDown()
    result = md.convert(filepath)
    
    output = Path(filepath).stem + ".md"
    with open(output, "w") as f:
        f.write(result.text_content)
    
    return filepath, output

files = list(Path("documents/").glob("*.pdf"))

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(convert_file, [str(f) for f in files])
    
    for input_file, output_file in results:
        print(f"Converted: {input_file} -> {output_file}")
```

## Integration Examples

### Literature Review Pipeline

```python
from markitdown import MarkItDown
from pathlib import Path
import json

md = MarkItDown()

# Convert papers and create metadata
papers_dir = Path("literature/")
output_dir = Path("literature_markdown/")
output_dir.mkdir(exist_ok=True)

catalog = []

for paper in papers_dir.glob("*.pdf"):
    result = md.convert(str(paper))
    
    # Save Markdown
    md_file = output_dir / f"{paper.stem}.md"
    md_file.write_text(result.text_content)
    
    # Store metadata
    catalog.append({
        "title": result.title or paper.stem,
        "source": paper.name,
        "markdown": str(md_file),
        "word_count": len(result.text_content.split())
    })

# Save catalog
with open(output_dir / "catalog.json", "w") as f:
    json.dump(catalog, f, indent=2)
```

### Data Extraction Pipeline

```python
from markitdown import MarkItDown
import re

md = MarkItDown()

# Convert Excel data to Markdown
result = md.convert("experimental_results.xlsx")

# Extract tables (Markdown tables start with |)
tables = []
current_table = []
in_table = False

for line in result.text_content.split('\n'):
    if line.strip().startswith('|'):
        in_table = True
        current_table.append(line)
    elif in_table:
        if current_table:
            tables.append('\n'.join(current_table))
            current_table = []
        in_table = False

# Process each table
for i, table in enumerate(tables):
    print(f"Table {i+1}:")
    print(table)
    print("\n" + "="*50 + "\n")
```

### YouTube Transcript Analysis

```python
from markitdown import MarkItDown

md = MarkItDown()

# Get transcript
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"
result = md.convert(video_url)

# Save transcript
with open("lecture_transcript.md", "w") as f:
    f.write(f"# Lecture Transcript\n\n")
    f.write(f"**Source**: {video_url}\n\n")
    f.write(result.text_content)
```

## Error Handling

### Robust Conversion

```python
from markitdown import MarkItDown
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

md = MarkItDown()

def safe_convert(filepath):
    """Convert file with error handling."""
    try:
        result = md.convert(filepath)
        output = Path(filepath).stem + ".md"
        
        with open(output, "w") as f:
            f.write(result.text_content)
        
        logger.info(f"Successfully converted {filepath}")
        return True
    
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return False
    
    except ValueError as e:
        logger.error(f"Invalid file format for {filepath}: {e}")
        return False
    
    except Exception as e:
        logger.error(f"Unexpected error converting {filepath}: {e}")
        return False

# Use it
files = ["paper.pdf", "data.xlsx", "slides.pptx"]
results = [safe_convert(f) for f in files]

print(f"Successfully converted {sum(results)}/{len(files)} files")
```

## Advanced Use Cases

### Custom Metadata Extraction

```python
from markitdown import MarkItDown
import re
from datetime import datetime

md = MarkItDown()

def convert_with_metadata(filepath):
    result = md.convert(filepath)
    
    # Extract metadata from content
    metadata = {
        "file": filepath,
        "title": result.title,
        "converted_at": datetime.now().isoformat(),
        "word_count": len(result.text_content.split()),
        "char_count": len(result.text_content)
    }
    
    # Try to find author
    author_match = re.search(r'(?:Author|By):\s*(.+?)(?:\n|$)', result.text_content)
    if author_match:
        metadata["author"] = author_match.group(1).strip()
    
    # Create formatted output
    output = f"""---
title: {metadata['title']}
author: {metadata.get('author', 'Unknown')}
source: {metadata['file']}
converted: {metadata['converted_at']}
words: {metadata['word_count']}
---

{result.text_content}
"""
    
    return output, metadata

# Use it
content, meta = convert_with_metadata("paper.pdf")
print(meta)
```

### Format-Specific Processing

```python
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()

def process_by_format(filepath):
    path = Path(filepath)
    result = md.convert(filepath)
    
    if path.suffix == '.pdf':
        # Add PDF-specific metadata
        output = f"# PDF Document: {path.stem}\n\n"
        output += result.text_content
    
    elif path.suffix == '.xlsx':
        # Add table count
        table_count = result.text_content.count('|---')
        output = f"# Excel Data: {path.stem}\n\n"
        output += f"**Tables**: {table_count}\n\n"
        output += result.text_content
    
    elif path.suffix == '.pptx':
        # Add slide count
        slide_count = result.text_content.count('## Slide')
        output = f"# Presentation: {path.stem}\n\n"
        output += f"**Slides**: {slide_count}\n\n"
        output += result.text_content
    
    else:
        output = result.text_content
    
    return output

# Use it
content = process_by_format("presentation.pptx")
print(content)
```

-e 

---

# File Format Support

This document provides detailed information about each file format supported by MarkItDown.

## Document Formats

### PDF (.pdf)

**Capabilities**:
- Text extraction
- Table detection
- Metadata extraction
- OCR for scanned documents (with dependencies)

**Dependencies**:
```bash
pip install 'markitdown[pdf]'
```

**Best For**:
- Scientific papers
- Reports
- Books
- Forms

**Limitations**:
- Complex layouts may not preserve perfect formatting
- Scanned PDFs require OCR setup
- Some PDF features (annotations, forms) may not convert

**Example**:
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("research_paper.pdf")
print(result.text_content)
```

**Enhanced with Azure Document Intelligence**:
```python
md = MarkItDown(docintel_endpoint="https://YOUR-ENDPOINT.cognitiveservices.azure.com/")
result = md.convert("complex_layout.pdf")
```

---

### Microsoft Word (.docx)

**Capabilities**:
- Text extraction
- Table conversion
- Heading hierarchy
- List formatting
- Basic text formatting (bold, italic)

**Dependencies**:
```bash
pip install 'markitdown[docx]'
```

**Best For**:
- Research papers
- Reports
- Documentation
- Manuscripts

**Preserved Elements**:
- Headings (converted to Markdown headers)
- Tables (converted to Markdown tables)
- Lists (bulleted and numbered)
- Basic formatting (bold, italic)
- Paragraphs

**Example**:
```python
result = md.convert("manuscript.docx")
```

---

### PowerPoint (.pptx)

**Capabilities**:
- Slide content extraction
- Speaker notes
- Table extraction
- Image descriptions (with AI)

**Dependencies**:
```bash
pip install 'markitdown[pptx]'
```

**Best For**:
- Presentations
- Lecture slides
- Conference talks

**Output Format**:
```markdown
# Slide 1: Title

Content from slide 1...

**Notes**: Speaker notes appear here

---

# Slide 2: Next Topic

...
```

**With AI Image Descriptions**:
```python
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("presentation.pptx")
```

---

### Excel (.xlsx, .xls)

**Capabilities**:
- Sheet extraction
- Table formatting
- Data preservation
- Formula values (calculated)

**Dependencies**:
```bash
pip install 'markitdown[xlsx]'  # Modern Excel
pip install 'markitdown[xls]'   # Legacy Excel
```

**Best For**:
- Data tables
- Research data
- Statistical results
- Experimental data

**Output Format**:
```markdown
# Sheet: Results

| Sample | Control | Treatment | P-value |
|--------|---------|-----------|---------|
| 1      | 10.2    | 12.5      | 0.023   |
| 2      | 9.8     | 11.9      | 0.031   |
```

**Example**:
```python
result = md.convert("experimental_data.xlsx")
```

---

## Image Formats

### Images (.jpg, .jpeg, .png, .gif, .webp)

**Capabilities**:
- EXIF metadata extraction
- OCR text extraction
- AI-powered image descriptions

**Dependencies**:
```bash
pip install 'markitdown[all]'  # Includes image support
```

**Best For**:
- Scanned documents
- Charts and graphs
- Scientific diagrams
- Photographs with text

**Output Without AI**:
```markdown
![Image](image.jpg)

**EXIF Data**:
- Camera: Canon EOS 5D
- Date: 2024-01-15
- Resolution: 4000x3000
```

**Output With AI**:
```python
from openai import OpenAI

client = OpenAI()
md = MarkItDown(
    llm_client=client,
    llm_model="gpt-4o",
    llm_prompt="Describe this scientific diagram in detail"
)
result = md.convert("graph.png")
```

**OCR for Text Extraction**:
Requires Tesseract OCR:
```bash
# macOS
brew install tesseract

# Ubuntu
sudo apt-get install tesseract-ocr
```

---

## Audio Formats

### Audio (.wav, .mp3)

**Capabilities**:
- Metadata extraction
- Speech-to-text transcription
- Duration and technical info

**Dependencies**:
```bash
pip install 'markitdown[audio-transcription]'
```

**Best For**:
- Lecture recordings
- Interviews
- Podcasts
- Meeting recordings

**Output Format**:
```markdown
# Audio: interview.mp3

**Metadata**:
- Duration: 45:32
- Bitrate: 320kbps
- Sample Rate: 44100Hz

**Transcription**:
[Transcribed text appears here...]
```

**Example**:
```python
result = md.convert("lecture.mp3")
```

---

## Web Formats

### HTML (.html, .htm)

**Capabilities**:
- Clean HTML to Markdown conversion
- Link preservation
- Table conversion
- List formatting

**Best For**:
- Web pages
- Documentation
- Blog posts
- Online articles

**Output Format**: Clean Markdown with preserved links and structure

**Example**:
```python
result = md.convert("webpage.html")
```

---

### YouTube URLs

**Capabilities**:
- Fetch video transcriptions
- Extract video metadata
- Caption download

**Dependencies**:
```bash
pip install 'markitdown[youtube-transcription]'
```

**Best For**:
- Educational videos
- Lectures
- Talks
- Tutorials

**Example**:
```python
result = md.convert("https://www.youtube.com/watch?v=VIDEO_ID")
```

---

## Data Formats

### CSV (.csv)

**Capabilities**:
- Automatic table conversion
- Delimiter detection
- Header preservation

**Output Format**: Markdown tables

**Example**:
```python
result = md.convert("data.csv")
```

**Output**:
```markdown
| Column1 | Column2 | Column3 |
|---------|---------|---------|
| Value1  | Value2  | Value3  |
```

---

### JSON (.json)

**Capabilities**:
- Structured representation
- Pretty formatting
- Nested data visualization

**Best For**:
- API responses
- Configuration files
- Data exports

**Example**:
```python
result = md.convert("data.json")
```

---

### XML (.xml)

**Capabilities**:
- Structure preservation
- Attribute extraction
- Formatted output

**Best For**:
- Configuration files
- Data interchange
- Structured documents

**Example**:
```python
result = md.convert("config.xml")
```

---

## Archive Formats

### ZIP (.zip)

**Capabilities**:
- Iterates through archive contents
- Converts each file individually
- Maintains directory structure in output

**Best For**:
- Document collections
- Project archives
- Batch conversions

**Output Format**:
```markdown
# Archive: documents.zip

## File: document1.pdf
[Content from document1.pdf...]

---

## File: document2.docx
[Content from document2.docx...]
```

**Example**:
```python
result = md.convert("archive.zip")
```

---

## E-book Formats

### EPUB (.epub)

**Capabilities**:
- Full text extraction
- Chapter structure
- Metadata extraction

**Best For**:
- E-books
- Digital publications
- Long-form content

**Output Format**: Markdown with preserved chapter structure

**Example**:
```python
result = md.convert("book.epub")
```

---

## Other Formats

### Outlook Messages (.msg)

**Capabilities**:
- Email content extraction
- Attachment listing
- Metadata (from, to, subject, date)

**Dependencies**:
```bash
pip install 'markitdown[outlook]'
```

**Best For**:
- Email archives
- Communication records

**Example**:
```python
result = md.convert("message.msg")
```

---

## Format-Specific Tips

### PDF Best Practices

1. **Use Azure Document Intelligence for complex layouts**:
   ```python
   md = MarkItDown(docintel_endpoint="endpoint_url")
   ```

2. **For scanned PDFs, ensure OCR is set up**:
   ```bash
   brew install tesseract  # macOS
   ```

3. **Split very large PDFs before conversion** for better performance

### PowerPoint Best Practices

1. **Use AI for visual content**:
   ```python
   md = MarkItDown(llm_client=client, llm_model="gpt-4o")
   ```

2. **Check speaker notes** - they're included in output

3. **Complex animations won't be captured** - static content only

### Excel Best Practices

1. **Large spreadsheets** may take time to convert

2. **Formulas are converted to their calculated values**

3. **Multiple sheets** are all included in output

4. **Charts become text descriptions** (use AI for better descriptions)

### Image Best Practices

1. **Use AI for meaningful descriptions**:
   ```python
   md = MarkItDown(
       llm_client=client,
       llm_model="gpt-4o",
       llm_prompt="Describe this scientific figure in detail"
   )
   ```

2. **For text-heavy images, ensure OCR dependencies** are installed

3. **High-resolution images** may take longer to process

### Audio Best Practices

1. **Clear audio** produces better transcriptions

2. **Long recordings** may take significant time

3. **Consider splitting long audio files** for faster processing

---

## Unsupported Formats

If you need to convert an unsupported format:

1. **Create a custom converter** (see `api_reference.md`)
2. **Look for plugins** on GitHub (#markitdown-plugin)
3. **Pre-convert to supported format** (e.g., convert .rtf to .docx)

---

## Format Detection

MarkItDown automatically detects format from:

1. **File extension** (primary method)
2. **MIME type** (fallback)
3. **File signature** (magic bytes, fallback)

**Override detection**:
```python
# Force specific format
result = md.convert("file_without_extension", file_extension=".pdf")

# With streams
with open("file", "rb") as f:
    result = md.convert_stream(f, file_extension=".pdf")
```

