# Matplotlib

## Overview

Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. This skill provides guidance on using matplotlib effectively, covering both the pyplot interface (MATLAB-style) and the object-oriented API (Figure/Axes), along with best practices for creating publication-quality visualizations.

## Usage

- Creating any type of plot or chart (line, scatter, bar, histogram, heatmap, contour, etc.)
- Generating scientific or statistical visualizations
- Customizing plot appearance (colors, styles, labels, legends)
- Creating multi-panel figures with subplots
- Exporting visualizations to various formats (PNG, PDF, SVG, etc.)
- Building interactive plots or animations
- Working with 3D visualizations
- Integrating plots into Jupyter notebooks or GUI applications

## Core Concepts

### The Matplotlib Hierarchy

Matplotlib uses a hierarchical structure of objects:

1. **Figure** - The top-level container for all plot elements
2. **Axes** - The actual plotting area where data is displayed (one Figure can contain multiple Axes)
3. **Artist** - Everything visible on the figure (lines, text, ticks, etc.)
4. **Axis** - The number line objects (x-axis, y-axis) that handle ticks and labels

### Two Interfaces

**1. pyplot Interface (Implicit, MATLAB-style)**
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```
- Convenient for quick, simple plots
- Maintains state automatically
- Good for interactive work and simple scripts

**2. Object-Oriented Interface (Explicit)**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])
ax.set_ylabel('some numbers')
plt.show()
```
- **Recommended for most use cases**
- More explicit control over figure and axes
- Better for complex figures with multiple subplots
- Easier to maintain and debug

## Common Workflows

### 1. Basic Plot Creation

**Single plot workflow:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes (OO interface - RECOMMENDED)
fig, ax = plt.subplots(figsize=(10, 6))

# Generate and plot data
x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')

# Customize
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trigonometric Functions')
ax.legend()
ax.grid(True, alpha=0.3)

# Save and/or display
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 2. Multiple Subplots

**Creating subplot layouts:**
```python
# Method 1: Regular grid
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data, bins=30)

# Method 2: Mosaic layout (more flexible)
fig, axes = plt.subplot_mosaic([['left', 'right_top'],
                                 ['left', 'right_bottom']],
                                figsize=(10, 8))
axes['left'].plot(x, y)
axes['right_top'].scatter(x, y)
axes['right_bottom'].hist(data)

# Method 3: GridSpec (maximum control)
from matplotlib.gridspec import GridSpec
fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])  # Top row, all columns
ax2 = fig.add_subplot(gs[1:, 0])  # Bottom two rows, first column
ax3 = fig.add_subplot(gs[1:, 1:])  # Bottom two rows, last two columns
```

### 3. Plot Types and Use Cases

**Line plots** - Time series, continuous data, trends
```python
ax.plot(x, y, linewidth=2, linestyle='--', marker='o', color='blue')
```

**Scatter plots** - Relationships between variables, correlations
```python
ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')
```

**Bar charts** - Categorical comparisons
```python
ax.bar(categories, values, color='steelblue', edgecolor='black')
# For horizontal bars:
ax.barh(categories, values)
```

**Histograms** - Distributions
```python
ax.hist(data, bins=30, edgecolor='black', alpha=0.7)
```

**Heatmaps** - Matrix data, correlations
```python
im = ax.imshow(matrix, cmap='coolwarm', aspect='auto')
plt.colorbar(im, ax=ax)
```

**Contour plots** - 3D data on 2D plane
```python
contour = ax.contour(X, Y, Z, levels=10)
ax.clabel(contour, inline=True, fontsize=8)
```

**Box plots** - Statistical distributions
```python
ax.boxplot([data1, data2, data3], labels=['A', 'B', 'C'])
```

**Violin plots** - Distribution densities
```python
ax.violinplot([data1, data2, data3], positions=[1, 2, 3])
```

For comprehensive plot type examples and variations, refer to `references/plot_types.md`.

### 4. Styling and Customization

**Color specification methods:**
- Named colors: `'red'`, `'blue'`, `'steelblue'`
- Hex codes: `'#FF5733'`
- RGB tuples: `(0.1, 0.2, 0.3)`
- Colormaps: `cmap='viridis'`, `cmap='plasma'`, `cmap='coolwarm'`

**Using style sheets:**
```python
plt.style.use('seaborn-v0_8-darkgrid')  # Apply predefined style
# Available styles: 'ggplot', 'bmh', 'fivethirtyeight', etc.
print(plt.style.available)  # List all available styles
```

**Customizing with rcParams:**
```python
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 18
```

**Text and annotations:**
```python
ax.text(x, y, 'annotation', fontsize=12, ha='center')
ax.annotate('important point', xy=(x, y), xytext=(x+1, y+1),
            arrowprops=dict(arrowstyle='->', color='red'))
```

For detailed styling options and colormap guidelines, see `references/styling_guide.md`.

### 5. Saving Figures

**Export to various formats:**
```python
# High-resolution PNG for presentations/papers
plt.savefig('figure.png', dpi=300, bbox_inches='tight', facecolor='white')

# Vector format for publications (scalable)
plt.savefig('figure.pdf', bbox_inches='tight')
plt.savefig('figure.svg', bbox_inches='tight')

# Transparent background
plt.savefig('figure.png', dpi=300, bbox_inches='tight', transparent=True)
```

**Important parameters:**
- `dpi`: Resolution (300 for publications, 150 for web, 72 for screen)
- `bbox_inches='tight'`: Removes excess whitespace
- `facecolor='white'`: Ensures white background (useful for transparent themes)
- `transparent=True`: Transparent background

### 6. Working with 3D Plots

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
ax.plot_surface(X, Y, Z, cmap='viridis')

# 3D scatter
ax.scatter(x, y, z, c=colors, marker='o')

# 3D line plot
ax.plot(x, y, z, linewidth=2)

# Labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
```

## Best Practices

### 1. Interface Selection
- **Use the object-oriented interface** (fig, ax = plt.subplots()) for production code
- Reserve pyplot interface for quick interactive exploration only
- Always create figures explicitly rather than relying on implicit state

### 2. Figure Size and DPI
- Set figsize at creation: `fig, ax = plt.subplots(figsize=(10, 6))`
- Use appropriate DPI for output medium:
  - Screen/notebook: 72-100 dpi
  - Web: 150 dpi
  - Print/publications: 300 dpi

### 3. Layout Management
- Use `constrained_layout=True` or `tight_layout()` to prevent overlapping elements
- `fig, ax = plt.subplots(constrained_layout=True)` is recommended for automatic spacing

### 4. Colormap Selection
- **Sequential** (viridis, plasma, inferno): Ordered data with consistent progression
- **Diverging** (coolwarm, RdBu): Data with meaningful center point (e.g., zero)
- **Qualitative** (tab10, Set3): Categorical/nominal data
- Avoid rainbow colormaps (jet) - they are not perceptually uniform

### 5. Accessibility
- Use colorblind-friendly colormaps (viridis, cividis)
- Add patterns/hatching for bar charts in addition to colors
- Ensure sufficient contrast between elements
- Include descriptive labels and legends

### 6. Performance
- For large datasets, use `rasterized=True` in plot calls to reduce file size
- Use appropriate data reduction before plotting (e.g., downsample dense time series)
- For animations, use blitting for better performance

### 7. Code Organization
```python
# Good practice: Clear structure
def create_analysis_plot(data, title):
    """Create standardized analysis plot."""
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    # Plot data
    ax.plot(data['x'], data['y'], linewidth=2)

    # Customize
    ax.set_xlabel('X Axis Label', fontsize=12)
    ax.set_ylabel('Y Axis Label', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    return fig, ax

# Use the function
fig, ax = create_analysis_plot(my_data, 'My Analysis')
plt.savefig('analysis.png', dpi=300, bbox_inches='tight')
```

## Quick Reference Scripts

This skill includes helper scripts in the `scripts/` directory:

### `plot_template.py`
Template script demonstrating various plot types with best practices. Use this as a starting point for creating new visualizations.

**Usage:**
```bash
python scripts/plot_template.py
```

### `style_configurator.py`
Interactive utility to configure matplotlib style preferences and generate custom style sheets.

**Usage:**
```bash
python scripts/style_configurator.py
```

## Detailed References

For comprehensive information, consult the reference documents:

- **`references/plot_types.md`** - Complete catalog of plot types with code examples and use cases
- **`references/styling_guide.md`** - Detailed styling options, colormaps, and customization
- **`references/api_reference.md`** - Core classes and methods reference
- **`references/common_issues.md`** - Troubleshooting guide for common problems

## Integration with Other Tools

Matplotlib integrates well with:
- **NumPy/Pandas** - Direct plotting from arrays and DataFrames
- **Seaborn** - High-level statistical visualizations built on matplotlib
- **Jupyter** - Interactive plotting with `%matplotlib inline` or `%matplotlib widget`
- **GUI frameworks** - Embedding in Tkinter, Qt, wxPython applications

## Common Gotchas

1. **Overlapping elements**: Use `constrained_layout=True` or `tight_layout()`
2. **State confusion**: Use OO interface to avoid pyplot state machine issues
3. **Memory issues with many figures**: Close figures explicitly with `plt.close(fig)`
4. **Font warnings**: Install fonts or suppress warnings with `plt.rcParams['font.sans-serif']`
5. **DPI confusion**: Remember that figsize is in inches, not pixels: `pixels = dpi * inches`

## Additional Resources

- Official documentation: https://matplotlib.org/
- Gallery: https://matplotlib.org/stable/gallery/index.html
- Cheatsheets: https://matplotlib.org/cheatsheets/
- Tutorials: https://matplotlib.org/stable/tutorials/index.html

-e 

---

# Matplotlib API Reference

This document provides a quick reference for the most commonly used matplotlib classes and methods.

## Core Classes

### Figure

The top-level container for all plot elements.

**Creation:**
```python
fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
```

**Key Methods:**
- `fig.add_subplot(nrows, ncols, index)` - Add a subplot
- `fig.add_axes([left, bottom, width, height])` - Add axes at specific position
- `fig.savefig(filename, dpi=300, bbox_inches='tight')` - Save figure
- `fig.tight_layout()` - Adjust spacing to prevent overlaps
- `fig.suptitle(title)` - Set figure title
- `fig.legend()` - Create figure-level legend
- `fig.colorbar(mappable)` - Add colorbar to figure
- `plt.close(fig)` - Close figure to free memory

**Key Attributes:**
- `fig.axes` - List of all axes in the figure
- `fig.dpi` - Resolution in dots per inch
- `fig.figsize` - Figure dimensions in inches (width, height)

### Axes

The actual plotting area where data is visualized.

**Creation:**
```python
fig, ax = plt.subplots()  # Single axes
ax = fig.add_subplot(111)  # Alternative method
```

**Plotting Methods:**

**Line plots:**
- `ax.plot(x, y, **kwargs)` - Line plot
- `ax.step(x, y, where='pre'/'mid'/'post')` - Step plot
- `ax.errorbar(x, y, yerr, xerr)` - Error bars

**Scatter plots:**
- `ax.scatter(x, y, s=size, c=color, marker='o', alpha=0.5)` - Scatter plot

**Bar charts:**
- `ax.bar(x, height, width=0.8, align='center')` - Vertical bar chart
- `ax.barh(y, width)` - Horizontal bar chart

**Statistical plots:**
- `ax.hist(data, bins=10, density=False)` - Histogram
- `ax.boxplot(data, labels=None)` - Box plot
- `ax.violinplot(data)` - Violin plot

**2D plots:**
- `ax.imshow(array, cmap='viridis', aspect='auto')` - Display image/matrix
- `ax.contour(X, Y, Z, levels=10)` - Contour lines
- `ax.contourf(X, Y, Z, levels=10)` - Filled contours
- `ax.pcolormesh(X, Y, Z)` - Pseudocolor plot

**Filling:**
- `ax.fill_between(x, y1, y2, alpha=0.3)` - Fill between curves
- `ax.fill_betweenx(y, x1, x2)` - Fill between vertical curves

**Text and annotations:**
- `ax.text(x, y, text, fontsize=12)` - Add text
- `ax.annotate(text, xy=(x, y), xytext=(x2, y2), arrowprops={})` - Annotate with arrow

**Customization Methods:**

**Labels and titles:**
- `ax.set_xlabel(label, fontsize=12)` - Set x-axis label
- `ax.set_ylabel(label, fontsize=12)` - Set y-axis label
- `ax.set_title(title, fontsize=14)` - Set axes title

**Limits and scales:**
- `ax.set_xlim(left, right)` - Set x-axis limits
- `ax.set_ylim(bottom, top)` - Set y-axis limits
- `ax.set_xscale('linear'/'log'/'symlog')` - Set x-axis scale
- `ax.set_yscale('linear'/'log'/'symlog')` - Set y-axis scale

**Ticks:**
- `ax.set_xticks(positions)` - Set x-tick positions
- `ax.set_xticklabels(labels)` - Set x-tick labels
- `ax.tick_params(axis='both', labelsize=10)` - Customize tick appearance

**Grid and spines:**
- `ax.grid(True, alpha=0.3, linestyle='--')` - Add grid
- `ax.spines['top'].set_visible(False)` - Hide top spine
- `ax.spines['right'].set_visible(False)` - Hide right spine

**Legend:**
- `ax.legend(loc='best', fontsize=10, frameon=True)` - Add legend
- `ax.legend(handles, labels)` - Custom legend

**Aspect and layout:**
- `ax.set_aspect('equal'/'auto'/ratio)` - Set aspect ratio
- `ax.invert_xaxis()` - Invert x-axis
- `ax.invert_yaxis()` - Invert y-axis

### pyplot Module

High-level interface for quick plotting.

**Figure creation:**
- `plt.figure()` - Create new figure
- `plt.subplots()` - Create figure and axes
- `plt.subplot()` - Add subplot to current figure

**Plotting (uses current axes):**
- `plt.plot()` - Line plot
- `plt.scatter()` - Scatter plot
- `plt.bar()` - Bar chart
- `plt.hist()` - Histogram
- (All axes methods available)

**Display and save:**
- `plt.show()` - Display figure
- `plt.savefig()` - Save figure
- `plt.close()` - Close figure

**Style:**
- `plt.style.use(style_name)` - Apply style sheet
- `plt.style.available` - List available styles

**State management:**
- `plt.gca()` - Get current axes
- `plt.gcf()` - Get current figure
- `plt.sca(ax)` - Set current axes
- `plt.clf()` - Clear current figure
- `plt.cla()` - Clear current axes

## Line and Marker Styles

### Line Styles
- `'-'` or `'solid'` - Solid line
- `'--'` or `'dashed'` - Dashed line
- `'-.'` or `'dashdot'` - Dash-dot line
- `':'` or `'dotted'` - Dotted line
- `''` or `' '` or `'None'` - No line

### Marker Styles
- `'.'` - Point marker
- `'o'` - Circle marker
- `'v'`, `'^'`, `'<'`, `'>'` - Triangle markers
- `'s'` - Square marker
- `'p'` - Pentagon marker
- `'*'` - Star marker
- `'h'`, `'H'` - Hexagon markers
- `'+'` - Plus marker
- `'x'` - X marker
- `'D'`, `'d'` - Diamond markers

### Color Specifications

**Single character shortcuts:**
- `'b'` - Blue
- `'g'` - Green
- `'r'` - Red
- `'c'` - Cyan
- `'m'` - Magenta
- `'y'` - Yellow
- `'k'` - Black
- `'w'` - White

**Named colors:**
- `'steelblue'`, `'coral'`, `'teal'`, etc.
- See full list: https://matplotlib.org/stable/gallery/color/named_colors.html

**Other formats:**
- Hex: `'#FF5733'`
- RGB tuple: `(0.1, 0.2, 0.3)`
- RGBA tuple: `(0.1, 0.2, 0.3, 0.5)`

## Common Parameters

### Plot Function Parameters

```python
ax.plot(x, y,
    color='blue',           # Line color
    linewidth=2,            # Line width
    linestyle='--',         # Line style
    marker='o',             # Marker style
    markersize=8,           # Marker size
    markerfacecolor='red',  # Marker fill color
    markeredgecolor='black',# Marker edge color
    markeredgewidth=1,      # Marker edge width
    alpha=0.7,              # Transparency (0-1)
    label='data',           # Legend label
    zorder=2,               # Drawing order
    rasterized=True         # Rasterize for smaller file size
)
```

### Scatter Function Parameters

```python
ax.scatter(x, y,
    s=50,                   # Size (scalar or array)
    c='blue',               # Color (scalar, array, or sequence)
    marker='o',             # Marker style
    cmap='viridis',         # Colormap (if c is numeric)
    alpha=0.5,              # Transparency
    edgecolors='black',     # Edge color
    linewidths=1,           # Edge width
    vmin=0, vmax=1,         # Color scale limits
    label='data'            # Legend label
)
```

### Text Parameters

```python
ax.text(x, y, text,
    fontsize=12,            # Font size
    fontweight='normal',    # 'normal', 'bold', 'heavy', 'light'
    fontstyle='normal',     # 'normal', 'italic', 'oblique'
    fontfamily='sans-serif',# Font family
    color='black',          # Text color
    alpha=1.0,              # Transparency
    ha='center',            # Horizontal alignment: 'left', 'center', 'right'
    va='center',            # Vertical alignment: 'top', 'center', 'bottom', 'baseline'
    rotation=0,             # Rotation angle in degrees
    bbox=dict(              # Background box
        facecolor='white',
        edgecolor='black',
        boxstyle='round'
    )
)
```

## rcParams Configuration

Common rcParams settings for global customization:

```python
# Font settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['font.size'] = 12

# Figure settings
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# Axes settings
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.grid.alpha'] = 0.3

# Line settings
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 8

# Tick settings
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['xtick.direction'] = 'in'  # 'in', 'out', 'inout'
plt.rcParams['ytick.direction'] = 'in'

# Legend settings
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.framealpha'] = 0.8

# Grid settings
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['grid.linestyle'] = '--'
```

## GridSpec for Complex Layouts

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

# Span multiple cells
ax1 = fig.add_subplot(gs[0, :])      # Top row, all columns
ax2 = fig.add_subplot(gs[1:, 0])     # Bottom two rows, first column
ax3 = fig.add_subplot(gs[1, 1:])     # Middle row, last two columns
ax4 = fig.add_subplot(gs[2, 1])      # Bottom row, middle column
ax5 = fig.add_subplot(gs[2, 2])      # Bottom row, right column
```

## 3D Plotting

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot types
ax.plot(x, y, z)                    # 3D line
ax.scatter(x, y, z)                 # 3D scatter
ax.plot_surface(X, Y, Z)            # 3D surface
ax.plot_wireframe(X, Y, Z)          # 3D wireframe
ax.contour(X, Y, Z)                 # 3D contour
ax.bar3d(x, y, z, dx, dy, dz)       # 3D bar

# Customization
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=30, azim=45)      # Set viewing angle
```

## Animation

```python
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [])

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return line,

def update(frame):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + frame/10)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, update, init_func=init,
                     frames=100, interval=50, blit=True)

# Save animation
anim.save('animation.gif', writer='pillow', fps=20)
anim.save('animation.mp4', writer='ffmpeg', fps=20)
```

## Image Operations

```python
# Read and display image
img = plt.imread('image.png')
ax.imshow(img)

# Display matrix as image
ax.imshow(matrix, cmap='viridis', aspect='auto',
          interpolation='nearest', origin='lower')

# Colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Values')

# Image extent (set coordinates)
ax.imshow(img, extent=[x_min, x_max, y_min, y_max])
```

## Event Handling

```python
# Mouse click event
def on_click(event):
    if event.inaxes:
        print(f'Clicked at x={event.xdata:.2f}, y={event.ydata:.2f}')

fig.canvas.mpl_connect('button_press_event', on_click)

# Key press event
def on_key(event):
    print(f'Key pressed: {event.key}')

fig.canvas.mpl_connect('key_press_event', on_key)
```

## Useful Utilities

```python
# Get current axis limits
xlims = ax.get_xlim()
ylims = ax.get_ylim()

# Set equal aspect ratio
ax.set_aspect('equal', adjustable='box')

# Share axes between subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Twin axes (two y-axes)
ax2 = ax1.twinx()

# Remove tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Scientific notation
ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

# Date formatting
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
```
-e 

---

# Matplotlib Plot Types Guide

Comprehensive guide to different plot types in matplotlib with examples and use cases.

## 1. Line Plots

**Use cases:** Time series, continuous data, trends, function visualization

### Basic Line Plot
```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, linewidth=2, label='Data')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.legend()
```

### Multiple Lines
```python
ax.plot(x, y1, label='Dataset 1', linewidth=2)
ax.plot(x, y2, label='Dataset 2', linewidth=2, linestyle='--')
ax.plot(x, y3, label='Dataset 3', linewidth=2, linestyle=':')
ax.legend()
```

### Line with Markers
```python
ax.plot(x, y, marker='o', markersize=8, linestyle='-',
        linewidth=2, markerfacecolor='red', markeredgecolor='black')
```

### Step Plot
```python
ax.step(x, y, where='mid', linewidth=2, label='Step function')
# where options: 'pre', 'post', 'mid'
```

### Error Bars
```python
ax.errorbar(x, y, yerr=error, fmt='o-', linewidth=2,
            capsize=5, capthick=2, label='With uncertainty')
```

## 2. Scatter Plots

**Use cases:** Correlations, relationships between variables, clusters, outliers

### Basic Scatter
```python
ax.scatter(x, y, s=50, alpha=0.6)
```

### Sized and Colored Scatter
```python
scatter = ax.scatter(x, y, s=sizes*100, c=colors,
                     cmap='viridis', alpha=0.6, edgecolors='black')
plt.colorbar(scatter, ax=ax, label='Color variable')
```

### Categorical Scatter
```python
for category in categories:
    mask = data['category'] == category
    ax.scatter(data[mask]['x'], data[mask]['y'],
               label=category, s=50, alpha=0.7)
ax.legend()
```

## 3. Bar Charts

**Use cases:** Categorical comparisons, discrete data, counts

### Vertical Bar Chart
```python
ax.bar(categories, values, color='steelblue',
       edgecolor='black', linewidth=1.5)
ax.set_ylabel('Values')
```

### Horizontal Bar Chart
```python
ax.barh(categories, values, color='coral',
        edgecolor='black', linewidth=1.5)
ax.set_xlabel('Values')
```

### Grouped Bar Chart
```python
x = np.arange(len(categories))
width = 0.35

ax.bar(x - width/2, values1, width, label='Group 1')
ax.bar(x + width/2, values2, width, label='Group 2')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
```

### Stacked Bar Chart
```python
ax.bar(categories, values1, label='Part 1')
ax.bar(categories, values2, bottom=values1, label='Part 2')
ax.bar(categories, values3, bottom=values1+values2, label='Part 3')
ax.legend()
```

### Bar Chart with Error Bars
```python
ax.bar(categories, values, yerr=errors, capsize=5,
       color='steelblue', edgecolor='black')
```

### Bar Chart with Patterns
```python
bars1 = ax.bar(x - width/2, values1, width, label='Group 1',
               color='white', edgecolor='black', hatch='//')
bars2 = ax.bar(x + width/2, values2, width, label='Group 2',
               color='white', edgecolor='black', hatch='\\\\')
```

## 4. Histograms

**Use cases:** Distributions, frequency analysis

### Basic Histogram
```python
ax.hist(data, bins=30, edgecolor='black', alpha=0.7)
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
```

### Multiple Overlapping Histograms
```python
ax.hist(data1, bins=30, alpha=0.5, label='Dataset 1')
ax.hist(data2, bins=30, alpha=0.5, label='Dataset 2')
ax.legend()
```

### Normalized Histogram (Density)
```python
ax.hist(data, bins=30, density=True, alpha=0.7,
        edgecolor='black', label='Empirical')

# Overlay theoretical distribution
from scipy.stats import norm
x = np.linspace(data.min(), data.max(), 100)
ax.plot(x, norm.pdf(x, data.mean(), data.std()),
        'r-', linewidth=2, label='Normal fit')
ax.legend()
```

### 2D Histogram (Hexbin)
```python
hexbin = ax.hexbin(x, y, gridsize=30, cmap='Blues')
plt.colorbar(hexbin, ax=ax, label='Counts')
```

### 2D Histogram (hist2d)
```python
h = ax.hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar(h[3], ax=ax, label='Counts')
```

## 5. Box and Violin Plots

**Use cases:** Statistical distributions, outlier detection, comparing distributions

### Box Plot
```python
ax.boxplot([data1, data2, data3],
           labels=['Group A', 'Group B', 'Group C'],
           showmeans=True, meanline=True)
ax.set_ylabel('Values')
```

### Horizontal Box Plot
```python
ax.boxplot([data1, data2, data3], vert=False,
           labels=['Group A', 'Group B', 'Group C'])
ax.set_xlabel('Values')
```

### Violin Plot
```python
parts = ax.violinplot([data1, data2, data3],
                      positions=[1, 2, 3],
                      showmeans=True, showmedians=True)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Group A', 'Group B', 'Group C'])
```

## 6. Heatmaps

**Use cases:** Matrix data, correlations, intensity maps

### Basic Heatmap
```python
im = ax.imshow(matrix, cmap='coolwarm', aspect='auto')
plt.colorbar(im, ax=ax, label='Values')
ax.set_xlabel('X')
ax.set_ylabel('Y')
```

### Heatmap with Annotations
```python
im = ax.imshow(matrix, cmap='coolwarm')
plt.colorbar(im, ax=ax)

# Add text annotations
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        text = ax.text(j, i, f'{matrix[i, j]:.2f}',
                       ha='center', va='center', color='black')
```

### Correlation Matrix
```python
corr = data.corr()
im = ax.imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1)
plt.colorbar(im, ax=ax, label='Correlation')

# Set tick labels
ax.set_xticks(range(len(corr)))
ax.set_yticks(range(len(corr)))
ax.set_xticklabels(corr.columns, rotation=45, ha='right')
ax.set_yticklabels(corr.columns)
```

## 7. Contour Plots

**Use cases:** 3D data on 2D plane, topography, function visualization

### Contour Lines
```python
contour = ax.contour(X, Y, Z, levels=10, cmap='viridis')
ax.clabel(contour, inline=True, fontsize=8)
plt.colorbar(contour, ax=ax)
```

### Filled Contours
```python
contourf = ax.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contourf, ax=ax)
```

### Combined Contours
```python
contourf = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.8)
contour = ax.contour(X, Y, Z, levels=10, colors='black',
                     linewidths=0.5, alpha=0.4)
ax.clabel(contour, inline=True, fontsize=8)
plt.colorbar(contourf, ax=ax)
```

## 8. Pie Charts

**Use cases:** Proportions, percentages (use sparingly)

### Basic Pie Chart
```python
ax.pie(sizes, labels=labels, autopct='%1.1f%%',
       startangle=90, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures circular pie
```

### Exploded Pie Chart
```python
explode = (0.1, 0, 0, 0)  # Explode first slice
ax.pie(sizes, explode=explode, labels=labels,
       autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
```

### Donut Chart
```python
ax.pie(sizes, labels=labels, autopct='%1.1f%%',
       wedgeprops=dict(width=0.5), startangle=90)
ax.axis('equal')
```

## 9. Polar Plots

**Use cases:** Cyclic data, directional data, radar charts

### Basic Polar Plot
```python
theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(2*theta))

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, linewidth=2)
```

### Radar Chart
```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 5, 2, 4]

# Add first value to the end to close the polygon
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
values_closed = np.concatenate((values, [values[0]]))
angles_closed = np.concatenate((angles, [angles[0]]))

ax = plt.subplot(111, projection='polar')
ax.plot(angles_closed, values_closed, 'o-', linewidth=2)
ax.fill(angles_closed, values_closed, alpha=0.25)
ax.set_xticks(angles)
ax.set_xticklabels(categories)
```

## 10. Stream and Quiver Plots

**Use cases:** Vector fields, flow visualization

### Quiver Plot (Vector Field)
```python
ax.quiver(X, Y, U, V, alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal')
```

### Stream Plot
```python
ax.streamplot(X, Y, U, V, density=1.5, color='k', linewidth=1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal')
```

## 11. Fill Between

**Use cases:** Uncertainty bounds, confidence intervals, areas under curves

### Fill Between Two Curves
```python
ax.plot(x, y, 'k-', linewidth=2, label='Mean')
ax.fill_between(x, y - std, y + std, alpha=0.3,
                label='±1 std dev')
ax.legend()
```

### Fill Between with Condition
```python
ax.plot(x, y1, label='Line 1')
ax.plot(x, y2, label='Line 2')
ax.fill_between(x, y1, y2, where=(y2 >= y1),
                alpha=0.3, label='y2 > y1', interpolate=True)
ax.legend()
```

## 12. 3D Plots

**Use cases:** Three-dimensional data visualization

### 3D Scatter
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=colors, cmap='viridis',
                     marker='o', s=50)
plt.colorbar(scatter, ax=ax)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
```

### 3D Surface Plot
```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',
                       edgecolor='none', alpha=0.9)
plt.colorbar(surf, ax=ax)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
```

### 3D Wireframe
```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
```

### 3D Contour
```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.contour(X, Y, Z, levels=15, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
```

## 13. Specialized Plots

### Stem Plot
```python
ax.stem(x, y, linefmt='C0-', markerfmt='C0o', basefmt='k-')
ax.set_xlabel('X')
ax.set_ylabel('Y')
```

### Filled Polygon
```python
vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
from matplotlib.patches import Polygon
polygon = Polygon(vertices, closed=True, edgecolor='black',
                  facecolor='lightblue', alpha=0.5)
ax.add_patch(polygon)
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
```

### Staircase Plot
```python
ax.stairs(values, edges, fill=True, alpha=0.5)
```

### Broken Barh (Gantt-style)
```python
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (10, 9),
               facecolors='tab:blue')
ax.broken_barh([(10, 20), (50, 50), (120, 30)], (20, 9),
               facecolors='tab:orange')
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('Time')
ax.set_yticks([15, 25])
ax.set_yticklabels(['Task 1', 'Task 2'])
```

## 14. Time Series Plots

### Basic Time Series
```python
import pandas as pd
import matplotlib.dates as mdates

ax.plot(dates, values, linewidth=2)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
plt.xticks(rotation=45)
ax.set_xlabel('Date')
ax.set_ylabel('Value')
```

### Time Series with Shaded Regions
```python
ax.plot(dates, values, linewidth=2)
# Shade weekends or specific periods
ax.axvspan(start_date, end_date, alpha=0.2, color='gray')
```

## Plot Selection Guide

| Data Type | Recommended Plot | Alternative Options |
|-----------|-----------------|---------------------|
| Single continuous variable | Histogram, KDE | Box plot, Violin plot |
| Two continuous variables | Scatter plot | Hexbin, 2D histogram |
| Time series | Line plot | Area plot, Step plot |
| Categorical vs continuous | Bar chart, Box plot | Violin plot, Strip plot |
| Two categorical variables | Heatmap | Grouped bar chart |
| Three continuous variables | 3D scatter, Contour | Color-coded scatter |
| Proportions | Bar chart | Pie chart (use sparingly) |
| Distributions comparison | Box plot, Violin plot | Overlaid histograms |
| Correlation matrix | Heatmap | Clustered heatmap |
| Vector field | Quiver plot, Stream plot | - |
| Function visualization | Line plot, Contour | 3D surface |
-e 

---

# Matplotlib Styling Guide

Comprehensive guide for styling and customizing matplotlib visualizations.

## Colormaps

### Colormap Categories

**1. Perceptually Uniform Sequential**
Best for ordered data that progresses from low to high values.
- `viridis` (default, colorblind-friendly)
- `plasma`
- `inferno`
- `magma`
- `cividis` (optimized for colorblind viewers)

**Usage:**
```python
im = ax.imshow(data, cmap='viridis')
scatter = ax.scatter(x, y, c=values, cmap='plasma')
```

**2. Sequential**
Traditional colormaps for ordered data.
- `Blues`, `Greens`, `Reds`, `Oranges`, `Purples`
- `YlOrBr`, `YlOrRd`, `OrRd`, `PuRd`
- `BuPu`, `GnBu`, `PuBu`, `YlGnBu`

**3. Diverging**
Best for data with a meaningful center point (e.g., zero, mean).
- `coolwarm` (blue to red)
- `RdBu` (red-blue)
- `RdYlBu` (red-yellow-blue)
- `RdYlGn` (red-yellow-green)
- `PiYG`, `PRGn`, `BrBG`, `PuOr`, `RdGy`

**Usage:**
```python
# Center colormap at zero
im = ax.imshow(data, cmap='coolwarm', vmin=-1, vmax=1)
```

**4. Qualitative**
Best for categorical/nominal data without inherent ordering.
- `tab10` (10 distinct colors)
- `tab20` (20 distinct colors)
- `Set1`, `Set2`, `Set3`
- `Pastel1`, `Pastel2`
- `Dark2`, `Accent`, `Paired`

**Usage:**
```python
colors = plt.cm.tab10(np.linspace(0, 1, n_categories))
for i, category in enumerate(categories):
    ax.plot(x, y[i], color=colors[i], label=category)
```

**5. Cyclic**
Best for cyclic data (e.g., phase, angle).
- `twilight`
- `twilight_shifted`
- `hsv`

### Colormap Best Practices

1. **Avoid `jet` colormap** - Not perceptually uniform, misleading
2. **Use perceptually uniform colormaps** - `viridis`, `plasma`, `cividis`
3. **Consider colorblind users** - Use `viridis`, `cividis`, or test with colorblind simulators
4. **Match colormap to data type**:
   - Sequential: increasing/decreasing data
   - Diverging: data with meaningful center
   - Qualitative: categories
5. **Reverse colormaps** - Add `_r` suffix: `viridis_r`, `coolwarm_r`

### Creating Custom Colormaps

```python
from matplotlib.colors import LinearSegmentedColormap

# From color list
colors = ['blue', 'white', 'red']
n_bins = 100
cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)

# From RGB values
colors = [(0, 0, 1), (1, 1, 1), (1, 0, 0)]  # RGB tuples
cmap = LinearSegmentedColormap.from_list('custom', colors)

# Use the custom colormap
ax.imshow(data, cmap=cmap)
```

### Discrete Colormaps

```python
import matplotlib.colors as mcolors

# Create discrete colormap from continuous
cmap = plt.cm.viridis
bounds = np.linspace(0, 10, 11)
norm = mcolors.BoundaryNorm(bounds, cmap.N)
im = ax.imshow(data, cmap=cmap, norm=norm)
```

## Style Sheets

### Using Built-in Styles

```python
# List available styles
print(plt.style.available)

# Apply a style
plt.style.use('seaborn-v0_8-darkgrid')

# Apply multiple styles (later styles override earlier ones)
plt.style.use(['seaborn-v0_8-whitegrid', 'seaborn-v0_8-poster'])

# Temporarily use a style
with plt.style.context('ggplot'):
    fig, ax = plt.subplots()
    ax.plot(x, y)
```

### Popular Built-in Styles

- `default` - Matplotlib's default style
- `classic` - Classic matplotlib look (pre-2.0)
- `seaborn-v0_8-*` - Seaborn-inspired styles
  - `seaborn-v0_8-darkgrid`, `seaborn-v0_8-whitegrid`
  - `seaborn-v0_8-dark`, `seaborn-v0_8-white`
  - `seaborn-v0_8-ticks`, `seaborn-v0_8-poster`, `seaborn-v0_8-talk`
- `ggplot` - ggplot2-inspired style
- `bmh` - Bayesian Methods for Hackers style
- `fivethirtyeight` - FiveThirtyEight style
- `grayscale` - Grayscale style

### Creating Custom Style Sheets

Create a file named `custom_style.mplstyle`:

```
# custom_style.mplstyle

# Figure
figure.figsize: 10, 6
figure.dpi: 100
figure.facecolor: white

# Font
font.family: sans-serif
font.sans-serif: Arial, Helvetica
font.size: 12

# Axes
axes.labelsize: 14
axes.titlesize: 16
axes.facecolor: white
axes.edgecolor: black
axes.linewidth: 1.5
axes.grid: True
axes.axisbelow: True

# Grid
grid.color: gray
grid.linestyle: --
grid.linewidth: 0.5
grid.alpha: 0.3

# Lines
lines.linewidth: 2
lines.markersize: 8

# Ticks
xtick.labelsize: 10
ytick.labelsize: 10
xtick.direction: in
ytick.direction: in
xtick.major.size: 6
ytick.major.size: 6
xtick.minor.size: 3
ytick.minor.size: 3

# Legend
legend.fontsize: 12
legend.frameon: True
legend.framealpha: 0.8
legend.fancybox: True

# Savefig
savefig.dpi: 300
savefig.bbox: tight
savefig.facecolor: white
```

Load and use:
```python
plt.style.use('path/to/custom_style.mplstyle')
```

## rcParams Configuration

### Global Configuration

```python
import matplotlib.pyplot as plt

# Configure globally
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14

# Or update multiple at once
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'lines.linewidth': 2
})
```

### Temporary Configuration

```python
# Context manager for temporary changes
with plt.rc_context({'font.size': 14, 'lines.linewidth': 2.5}):
    fig, ax = plt.subplots()
    ax.plot(x, y)
```

### Common rcParams

**Figure settings:**
```python
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['figure.edgecolor'] = 'white'
plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.constrained_layout.use'] = True
```

**Font settings:**
```python
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['font.size'] = 12
plt.rcParams['font.weight'] = 'normal'
```

**Axes settings:**
```python
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelweight'] = 'normal'
plt.rcParams['axes.spines.top'] = True
plt.rcParams['axes.spines.right'] = True
```

**Line settings:**
```python
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.linestyle'] = '-'
plt.rcParams['lines.marker'] = 'None'
plt.rcParams['lines.markersize'] = 6
```

**Save settings:**
```python
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.format'] = 'png'
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0.1
plt.rcParams['savefig.transparent'] = False
```

## Color Palettes

### Named Color Sets

```python
# Tableau colors
tableau_colors = plt.cm.tab10.colors

# CSS4 colors (subset)
css_colors = ['steelblue', 'coral', 'teal', 'goldenrod', 'crimson']

# Manual definition
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
```

### Color Cycles

```python
# Set default color cycle
from cycler import cycler
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
plt.rcParams['axes.prop_cycle'] = cycler(color=colors)

# Or combine color and line style
plt.rcParams['axes.prop_cycle'] = cycler(color=colors) + cycler(linestyle=['-', '--', ':', '-.'])
```

### Palette Generation

```python
# Evenly spaced colors from colormap
n_colors = 5
colors = plt.cm.viridis(np.linspace(0, 1, n_colors))

# Use in plot
for i, (x, y) in enumerate(data):
    ax.plot(x, y, color=colors[i])
```

## Typography

### Font Configuration

```python
# Set font family
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']

# Or sans-serif
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']

# Or monospace
plt.rcParams['font.family'] = 'monospace'
plt.rcParams['font.monospace'] = ['Courier New', 'DejaVu Sans Mono']
```

### Font Properties in Text

```python
from matplotlib import font_manager

# Specify font properties
ax.text(x, y, 'Text',
        fontsize=14,
        fontweight='bold',  # 'normal', 'bold', 'heavy', 'light'
        fontstyle='italic',  # 'normal', 'italic', 'oblique'
        fontfamily='serif')

# Use specific font file
prop = font_manager.FontProperties(fname='path/to/font.ttf')
ax.text(x, y, 'Text', fontproperties=prop)
```

### Mathematical Text

```python
# LaTeX-style math
ax.set_title(r'$\alpha > \beta$')
ax.set_xlabel(r'$\mu \pm \sigma$')
ax.text(x, y, r'$\int_0^\infty e^{-x} dx = 1$')

# Subscripts and superscripts
ax.set_ylabel(r'$y = x^2 + 2x + 1$')
ax.text(x, y, r'$x_1, x_2, \ldots, x_n$')

# Greek letters
ax.text(x, y, r'$\alpha, \beta, \gamma, \delta, \epsilon$')
```

### Using Full LaTeX

```python
# Enable full LaTeX rendering (requires LaTeX installation)
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

ax.set_title(r'\textbf{Bold Title}')
ax.set_xlabel(r'Time $t$ (s)')
```

## Spines and Grids

### Spine Customization

```python
# Hide specific spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Move spine position
ax.spines['left'].set_position(('outward', 10))
ax.spines['bottom'].set_position(('data', 0))

# Change spine color and width
ax.spines['left'].set_color('red')
ax.spines['bottom'].set_linewidth(2)
```

### Grid Customization

```python
# Basic grid
ax.grid(True)

# Customized grid
ax.grid(True, which='major', linestyle='--', linewidth=0.8, alpha=0.3)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.2)

# Grid for specific axis
ax.grid(True, axis='x')  # Only vertical lines
ax.grid(True, axis='y')  # Only horizontal lines

# Grid behind or in front of data
ax.set_axisbelow(True)  # Grid behind data
```

## Legend Customization

### Legend Positioning

```python
# Location strings
ax.legend(loc='best')  # Automatic best position
ax.legend(loc='upper right')
ax.legend(loc='upper left')
ax.legend(loc='lower right')
ax.legend(loc='lower left')
ax.legend(loc='center')
ax.legend(loc='upper center')
ax.legend(loc='lower center')
ax.legend(loc='center left')
ax.legend(loc='center right')

# Precise positioning (bbox_to_anchor)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Outside plot area
ax.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=3)  # Below plot
```

### Legend Styling

```python
ax.legend(
    fontsize=12,
    frameon=True,           # Show frame
    framealpha=0.9,         # Frame transparency
    fancybox=True,          # Rounded corners
    shadow=True,            # Shadow effect
    ncol=2,                 # Number of columns
    title='Legend Title',   # Legend title
    title_fontsize=14,      # Title font size
    edgecolor='black',      # Frame edge color
    facecolor='white'       # Frame background color
)
```

### Custom Legend Entries

```python
from matplotlib.lines import Line2D

# Create custom legend handles
custom_lines = [Line2D([0], [0], color='red', lw=2),
                Line2D([0], [0], color='blue', lw=2, linestyle='--'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10)]

ax.legend(custom_lines, ['Label 1', 'Label 2', 'Label 3'])
```

## Layout and Spacing

### Constrained Layout

```python
# Preferred method (automatic adjustment)
fig, axes = plt.subplots(2, 2, constrained_layout=True)
```

### Tight Layout

```python
# Alternative method
fig, axes = plt.subplots(2, 2)
plt.tight_layout(pad=1.5, h_pad=2.0, w_pad=2.0)
```

### Manual Adjustment

```python
# Fine-grained control
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1,
                    hspace=0.3, wspace=0.4)
```

## Professional Publication Style

Example configuration for publication-quality figures:

```python
# Publication style configuration
plt.rcParams.update({
    # Figure
    'figure.figsize': (8, 6),
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,

    # Font
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 11,

    # Axes
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'axes.linewidth': 1.5,
    'axes.grid': False,
    'axes.spines.top': False,
    'axes.spines.right': False,

    # Lines
    'lines.linewidth': 2,
    'lines.markersize': 8,

    # Ticks
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'xtick.major.size': 6,
    'ytick.major.size': 6,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5,
    'xtick.direction': 'in',
    'ytick.direction': 'in',

    # Legend
    'legend.fontsize': 10,
    'legend.frameon': True,
    'legend.framealpha': 1.0,
    'legend.edgecolor': 'black'
})
```

## Dark Theme

```python
# Dark background style
plt.style.use('dark_background')

# Or manual configuration
plt.rcParams.update({
    'figure.facecolor': '#1e1e1e',
    'axes.facecolor': '#1e1e1e',
    'axes.edgecolor': 'white',
    'axes.labelcolor': 'white',
    'text.color': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'grid.color': 'gray',
    'legend.facecolor': '#1e1e1e',
    'legend.edgecolor': 'white'
})
```

## Color Accessibility

### Colorblind-Friendly Palettes

```python
# Use colorblind-friendly colormaps
colorblind_friendly = ['viridis', 'plasma', 'cividis']

# Colorblind-friendly discrete colors
cb_colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC',
             '#CA9161', '#949494', '#ECE133', '#56B4E9']

# Test with simulation tools or use these validated palettes
```

### High Contrast

```python
# Ensure sufficient contrast
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.width'] = 2
```
-e 

---

# Matplotlib Common Issues and Solutions

Troubleshooting guide for frequently encountered matplotlib problems.

## Display and Backend Issues

### Issue: Plots Not Showing

**Problem:** `plt.show()` doesn't display anything

**Solutions:**
```python
# 1. Check if backend is properly set (for interactive use)
import matplotlib
print(matplotlib.get_backend())

# 2. Try different backends
matplotlib.use('TkAgg')  # or 'Qt5Agg', 'MacOSX'
import matplotlib.pyplot as plt

# 3. In Jupyter notebooks, use magic command
%matplotlib inline  # Static images
# or
%matplotlib widget  # Interactive plots

# 4. Ensure plt.show() is called
plt.plot([1, 2, 3])
plt.show()
```

### Issue: "RuntimeError: main thread is not in main loop"

**Problem:** Interactive mode issues with threading

**Solution:**
```python
# Switch to non-interactive backend
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Or turn off interactive mode
plt.ioff()
```

### Issue: Figures Not Updating Interactively

**Problem:** Changes not reflected in interactive windows

**Solution:**
```python
# Enable interactive mode
plt.ion()

# Draw after each change
plt.plot(x, y)
plt.draw()
plt.pause(0.001)  # Brief pause to update display
```

## Layout and Spacing Issues

### Issue: Overlapping Labels and Titles

**Problem:** Labels, titles, or tick labels overlap or get cut off

**Solutions:**
```python
# Solution 1: Constrained layout (RECOMMENDED)
fig, ax = plt.subplots(constrained_layout=True)

# Solution 2: Tight layout
fig, ax = plt.subplots()
plt.tight_layout()

# Solution 3: Adjust margins manually
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)

# Solution 4: Save with bbox_inches='tight'
plt.savefig('figure.png', bbox_inches='tight')

# Solution 5: Rotate long tick labels
ax.set_xticklabels(labels, rotation=45, ha='right')
```

### Issue: Colorbar Affects Subplot Size

**Problem:** Adding colorbar shrinks the plot

**Solution:**
```python
# Solution 1: Use constrained layout
fig, ax = plt.subplots(constrained_layout=True)
im = ax.imshow(data)
plt.colorbar(im, ax=ax)

# Solution 2: Manually specify colorbar dimensions
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(im, cax=cax)

# Solution 3: For multiple subplots, share colorbar
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax in axes:
    im = ax.imshow(data)
fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.95)
```

### Issue: Subplots Too Close Together

**Problem:** Multiple subplots overlapping

**Solution:**
```python
# Solution 1: Use constrained_layout
fig, axes = plt.subplots(2, 2, constrained_layout=True)

# Solution 2: Adjust spacing with subplots_adjust
fig, axes = plt.subplots(2, 2)
plt.subplots_adjust(hspace=0.4, wspace=0.4)

# Solution 3: Specify spacing in tight_layout
plt.tight_layout(h_pad=2.0, w_pad=2.0)
```

## Memory and Performance Issues

### Issue: Memory Leak with Multiple Figures

**Problem:** Memory usage grows when creating many figures

**Solution:**
```python
# Close figures explicitly
fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig('plot.png')
plt.close(fig)  # or plt.close('all')

# Clear current figure without closing
plt.clf()

# Clear current axes
plt.cla()
```

### Issue: Large File Sizes

**Problem:** Saved figures are too large

**Solutions:**
```python
# Solution 1: Reduce DPI
plt.savefig('figure.png', dpi=150)  # Instead of 300

# Solution 2: Use rasterization for complex plots
ax.plot(x, y, rasterized=True)

# Solution 3: Use vector format for simple plots
plt.savefig('figure.pdf')  # or .svg

# Solution 4: Compress PNG
plt.savefig('figure.png', dpi=300, optimize=True)
```

### Issue: Slow Plotting with Large Datasets

**Problem:** Plotting takes too long with many points

**Solutions:**
```python
# Solution 1: Downsample data
from scipy.signal import decimate
y_downsampled = decimate(y, 10)  # Keep every 10th point

# Solution 2: Use rasterization
ax.plot(x, y, rasterized=True)

# Solution 3: Use line simplification
ax.plot(x, y)
for line in ax.get_lines():
    line.set_rasterized(True)

# Solution 4: For scatter plots, consider hexbin or 2d histogram
ax.hexbin(x, y, gridsize=50, cmap='viridis')
```

## Font and Text Issues

### Issue: Font Warnings

**Problem:** "findfont: Font family [...] not found"

**Solutions:**
```python
# Solution 1: Use available fonts
from matplotlib.font_manager import findfont, FontProperties
print(findfont(FontProperties(family='sans-serif')))

# Solution 2: Rebuild font cache
import matplotlib.font_manager
matplotlib.font_manager._rebuild()

# Solution 3: Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Solution 4: Specify fallback fonts
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'sans-serif']
```

### Issue: LaTeX Rendering Errors

**Problem:** Math text not rendering correctly

**Solutions:**
```python
# Solution 1: Use raw strings with r prefix
ax.set_xlabel(r'$\alpha$')  # Not '\alpha'

# Solution 2: Escape backslashes in regular strings
ax.set_xlabel('$\\alpha$')

# Solution 3: Disable LaTeX if not installed
plt.rcParams['text.usetex'] = False

# Solution 4: Use mathtext instead of full LaTeX
# Mathtext is always available, no LaTeX installation needed
ax.text(x, y, r'$\int_0^\infty e^{-x} dx$')
```

### Issue: Text Cut Off or Outside Figure

**Problem:** Labels or annotations appear outside figure bounds

**Solutions:**
```python
# Solution 1: Use bbox_inches='tight'
plt.savefig('figure.png', bbox_inches='tight')

# Solution 2: Adjust figure bounds
plt.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.15)

# Solution 3: Clip text to axes
ax.text(x, y, 'text', clip_on=True)

# Solution 4: Use constrained_layout
fig, ax = plt.subplots(constrained_layout=True)
```

## Color and Colormap Issues

### Issue: Colorbar Not Matching Plot

**Problem:** Colorbar shows different range than data

**Solution:**
```python
# Explicitly set vmin and vmax
im = ax.imshow(data, vmin=0, vmax=1, cmap='viridis')
plt.colorbar(im, ax=ax)

# Or use the same norm for multiple plots
import matplotlib.colors as mcolors
norm = mcolors.Normalize(vmin=data.min(), vmax=data.max())
im1 = ax1.imshow(data1, norm=norm, cmap='viridis')
im2 = ax2.imshow(data2, norm=norm, cmap='viridis')
```

### Issue: Colors Look Wrong

**Problem:** Unexpected colors in plots

**Solutions:**
```python
# Solution 1: Check color specification format
ax.plot(x, y, color='blue')  # Correct
ax.plot(x, y, color=(0, 0, 1))  # Correct RGB
ax.plot(x, y, color='#0000FF')  # Correct hex

# Solution 2: Verify colormap exists
print(plt.colormaps())  # List available colormaps

# Solution 3: For scatter plots, ensure c shape matches
ax.scatter(x, y, c=colors)  # colors should have same length as x, y

# Solution 4: Check if alpha is set correctly
ax.plot(x, y, alpha=1.0)  # 0=transparent, 1=opaque
```

### Issue: Reversed Colormap

**Problem:** Colormap direction is backwards

**Solution:**
```python
# Add _r suffix to reverse any colormap
ax.imshow(data, cmap='viridis_r')
```

## Axis and Scale Issues

### Issue: Axis Limits Not Working

**Problem:** `set_xlim` or `set_ylim` not taking effect

**Solutions:**
```python
# Solution 1: Set after plotting
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Solution 2: Disable autoscaling
ax.autoscale(False)
ax.set_xlim(0, 10)

# Solution 3: Use axis method
ax.axis([xmin, xmax, ymin, ymax])
```

### Issue: Log Scale with Zero or Negative Values

**Problem:** ValueError when using log scale with data ≤ 0

**Solutions:**
```python
# Solution 1: Filter out non-positive values
mask = (data > 0)
ax.plot(x[mask], data[mask])
ax.set_yscale('log')

# Solution 2: Use symlog for data with positive and negative values
ax.set_yscale('symlog')

# Solution 3: Add small offset
ax.plot(x, data + 1e-10)
ax.set_yscale('log')
```

### Issue: Dates Not Displaying Correctly

**Problem:** Date axis shows numbers instead of dates

**Solution:**
```python
import matplotlib.dates as mdates
import pandas as pd

# Convert to datetime if needed
dates = pd.to_datetime(date_strings)

ax.plot(dates, values)

# Format date axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
plt.xticks(rotation=45)
```

## Legend Issues

### Issue: Legend Covers Data

**Problem:** Legend obscures important parts of plot

**Solutions:**
```python
# Solution 1: Use 'best' location
ax.legend(loc='best')

# Solution 2: Place outside plot area
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Solution 3: Make legend semi-transparent
ax.legend(framealpha=0.7)

# Solution 4: Put legend below plot
ax.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=3)
```

### Issue: Too Many Items in Legend

**Problem:** Legend is cluttered with many entries

**Solutions:**
```python
# Solution 1: Only label selected items
for i, (x, y) in enumerate(data):
    label = f'Data {i}' if i % 5 == 0 else None
    ax.plot(x, y, label=label)

# Solution 2: Use multiple columns
ax.legend(ncol=3)

# Solution 3: Create custom legend with fewer entries
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='r'),
                Line2D([0], [0], color='b')]
ax.legend(custom_lines, ['Category A', 'Category B'])

# Solution 4: Use separate legend figure
fig_leg = plt.figure(figsize=(3, 2))
ax_leg = fig_leg.add_subplot(111)
ax_leg.legend(*ax.get_legend_handles_labels(), loc='center')
ax_leg.axis('off')
```

## 3D Plot Issues

### Issue: 3D Plots Look Flat

**Problem:** Difficult to perceive depth in 3D plots

**Solutions:**
```python
# Solution 1: Adjust viewing angle
ax.view_init(elev=30, azim=45)

# Solution 2: Add gridlines
ax.grid(True)

# Solution 3: Use color for depth
scatter = ax.scatter(x, y, z, c=z, cmap='viridis')

# Solution 4: Rotate interactively (if using interactive backend)
# User can click and drag to rotate
```

### Issue: 3D Axis Labels Cut Off

**Problem:** 3D axis labels appear outside figure

**Solution:**
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

# Add padding
fig.tight_layout(pad=3.0)

# Or save with tight bounding box
plt.savefig('3d_plot.png', bbox_inches='tight', pad_inches=0.5)
```

## Image and Colorbar Issues

### Issue: Images Appear Flipped

**Problem:** Image orientation is wrong

**Solution:**
```python
# Set origin parameter
ax.imshow(img, origin='lower')  # or 'upper' (default)

# Or flip array
ax.imshow(np.flipud(img))
```

### Issue: Images Look Pixelated

**Problem:** Image appears blocky when zoomed

**Solutions:**
```python
# Solution 1: Use interpolation
ax.imshow(img, interpolation='bilinear')
# Options: 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', etc.

# Solution 2: Increase DPI when saving
plt.savefig('figure.png', dpi=300)

# Solution 3: Use vector format if appropriate
plt.savefig('figure.pdf')
```

## Common Errors and Fixes

### "TypeError: 'AxesSubplot' object is not subscriptable"

**Problem:** Trying to index single axes
```python
# Wrong
fig, ax = plt.subplots()
ax[0].plot(x, y)  # Error!

# Correct
fig, ax = plt.subplots()
ax.plot(x, y)
```

### "ValueError: x and y must have same first dimension"

**Problem:** Data arrays have mismatched lengths
```python
# Check shapes
print(f"x shape: {x.shape}, y shape: {y.shape}")

# Ensure they match
assert len(x) == len(y), "x and y must have same length"
```

### "AttributeError: 'numpy.ndarray' object has no attribute 'plot'"

**Problem:** Calling plot on array instead of axes
```python
# Wrong
data.plot(x, y)

# Correct
ax.plot(x, y)
# or for pandas
data.plot(ax=ax)
```

## Best Practices to Avoid Issues

1. **Always use the OO interface** - Avoid pyplot state machine
   ```python
   fig, ax = plt.subplots()  # Good
   ax.plot(x, y)
   ```

2. **Use constrained_layout** - Prevents overlap issues
   ```python
   fig, ax = plt.subplots(constrained_layout=True)
   ```

3. **Close figures explicitly** - Prevents memory leaks
   ```python
   plt.close(fig)
   ```

4. **Set figure size at creation** - Better than resizing later
   ```python
   fig, ax = plt.subplots(figsize=(10, 6))
   ```

5. **Use raw strings for math text** - Avoids escape issues
   ```python
   ax.set_xlabel(r'$\alpha$')
   ```

6. **Check data shapes before plotting** - Catch size mismatches early
   ```python
   assert len(x) == len(y)
   ```

7. **Use appropriate DPI** - 300 for print, 150 for web
   ```python
   plt.savefig('figure.png', dpi=300)
   ```

8. **Test with different backends** - If display issues occur
   ```python
   import matplotlib
   matplotlib.use('TkAgg')
   ```
