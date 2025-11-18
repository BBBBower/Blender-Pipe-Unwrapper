# Blender Pipe Unwrapper

A Blender addon that generates accurate flat pattern cutting templates for pipe wrapping materials. Create professional PDF templates for any pipe specification with a simple GUI interface.

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Blender](https://img.shields.io/badge/blender-3.0%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- 🎯 **Any Pipe Specification**: Works with any pipe diameter, bend radius, angle, and segment count
- 🖱️ **Easy GUI Interface**: Simple sidebar panel in Blender - no scripting required
- 📐 **Accurate UV Unwrapping**: Uses Blender's 3D geometry for precise flat patterns
- 📄 **Professional PDFs**: Generates print-ready templates with scale bars and dimensions
- ⚡ **Fast Generation**: Creates templates in seconds
- 🔄 **Two Templates Per Page**: Efficient printing with dual templates

## Use Cases

Perfect for:
- Exhaust system heat wrapping (fiberglass, ceramic, stainless steel)
- Pipe insulation fabrication
- Custom pipe covering materials
- Automotive and industrial applications
- Fabrication shops and motorsports

## Installation

### Prerequisites

1. **Blender 3.0 or higher** - [Download Blender](https://www.blender.org/download/)
2. **Python reportlab library** - Required for PDF generation

### Install reportlab

Open a terminal/command prompt and run:

**Windows:**
```bash
"C:\Program Files\Blender Foundation\Blender 4.1\4.1\python\bin\python.exe" -m pip install reportlab
```

**macOS/Linux:**
```bash
/path/to/blender/python/bin/python -m pip install reportlab
```

### Install the Addon

1. Download `pipe_template_generator.py` from this repository
2. Open Blender
3. Go to: **Edit > Preferences > Add-ons**
4. Click **Install...** button (top right)
5. Select the downloaded `pipe_template_generator.py` file
6. Enable the addon by checking the box next to **"Object: Pipe Flat Pattern Generator"**

## Quick Start

1. Open Blender and press **N** to open the sidebar
2. Click the **"Pipe Templates"** tab
3. Enter your pipe specifications:
   - Pipe OD: 76.2mm (for 3" pipe)
   - Bend Radius: 1.5 (for 1.5D radius)
   - Bend Angle: 90° (for 90-degree bend)
   - Number of Segments: 5
   - Wrap Thickness: 6.15mm (6mm fiberglass + 0.15mm stainless)
   - Overlap: 10mm
4. Click **"Generate Template"**
5. Open the generated PDF from the output folder
6. Print at **100% scale** (Actual Size)
7. Verify the 100mm scale bar measures exactly 100mm
8. Cut along the **RED outline**

## Template Output

The generated PDF includes:

- **Two identical templates per page** for efficient printing
- **Blue outline**: Base pipe shape (reference)
- **Red outline**: Cutting line for wrap materials
- **100mm scale bar**: For print verification
- **Dimensions**: Width and height annotations
- **Legend**: Clear identification of outlines
- **Title**: Shows pipe specs and degrees per segment

### Example Template

For a 3" OD pipe with 1.5D radius, 90° bend, 5 segments:
- Template dimensions: 288mm × 38mm
- Degrees per segment: 18°
- Two templates printed on A4 landscape

## Parameters Explained

### Pipe OD (mm)
Outer diameter of the pipe in millimeters
- Default: 76.2mm (3 inches)
- Range: 10mm to 500mm

### Bend Radius (×D)
Centerline radius as a multiple of the pipe diameter
- Default: 1.5 (means 1.5 × diameter)
- Range: 0.5 to 10.0
- Example: 1.5D for 3" pipe = 114.3mm centerline radius

### Bend Angle (°)
Total angle of the bend in degrees
- Default: 90°
- Range: 1° to 360°
- Enter the value directly (e.g., 90 for 90 degrees)

### Number of Segments
How many pieces to split the bend into
- Default: 5
- Range: 1 to 20
- More segments = easier fabrication, more joints

### Wrap Thickness (mm)
Thickness of the wrap material in millimeters
- Default: 6.15mm (6mm fiberglass + 0.15mm stainless)
- Range: 0.1mm to 50mm
- Automatically calculates wrap radius

### Overlap (mm)
Overlap for seams and segment joins
- Default: 10mm
- Range: 0mm to 50mm

## Example Configurations

### Example 1: 3" Exhaust with 90° Bend (Default)
```
Pipe OD: 76.2mm
Bend Radius: 1.5×D
Bend Angle: 90°
Segments: 5
Wrap Thickness: 6.15mm
Result: 5 pieces @ 18° each, 288mm × 38mm template
```

### Example 2: 2" Pipe with Tight 45° Bend
```
Pipe OD: 50.8mm
Bend Radius: 1.0×D
Bend Angle: 45°
Segments: 3
Wrap Thickness: 6.15mm
Result: 3 pieces @ 15° each
```

### Example 3: 4" Pipe with 180° U-Bend
```
Pipe OD: 101.6mm
Bend Radius: 2.0×D
Bend Angle: 180°
Segments: 6
Wrap Thickness: 6.15mm
Result: 6 pieces @ 30° each
```

## Printing Instructions

### Critical Settings

When printing the PDF template:

1. **Scale**: 100% (Actual Size / Do Not Scale)
2. **Orientation**: Landscape
3. **Paper**: A4 (297mm × 210mm)
4. **Margins**: None or Minimum

### Verification

**Always verify the scale before cutting:**
1. Measure the scale bar at the bottom of the page
2. It **must** measure exactly 100mm
3. If not 100mm, adjust printer settings and reprint

### Cutting

1. Cut along the **RED outline** (not the blue reference line)
2. Make the specified number of identical pieces
3. Example: For 5 segments, cut 5 pieces from fiberglass and 5 from stainless

## Assembly

For each segment:
1. Wrap fiberglass layer first
2. Position seam on inside of bend (concave side)
3. Ensure proper overlap
4. Wrap stainless steel layer second
5. Position seam on inside of bend
6. Ensure proper overlap

Connect all wrapped segments end-to-end to form the complete bend.

## Technical Details

### How It Works

1. **3D Geometry Creation**: Creates accurate curved pipe segment with proper cylindrical geometry
2. **Seam Marking**: Marks seam along ground plane at minimum radius (closest to origin)
3. **UV Unwrapping**: Uses Blender's UV unwrap to create flat pattern
4. **Boundary Extraction**: Finds outer edges of UV unwrap (88 boundary edges)
5. **PDF Generation**: Uses reportlab to create printable template with exact dimensions

### Calculations

- Base circumference: π × pipe_OD
- Base arc length: bend_centerline_radius × segment_angle_rad
- Wrap radius: pipe_radius + wrap_thickness
- Wrap width: (2π × wrap_radius) + overlap
- Wrap arc length: (bend_centerline_radius + wrap_thickness) × segment_angle_rad

### Quality Metrics

- Seam edges: 12 (clean longitudinal seam)
- UV boundary edges: 88 (accurate outline)
- PDF size: ~7.6KB (optimized)
- Template accuracy: Sub-millimeter precision

## Troubleshooting

### "reportlab not installed" Error
Install reportlab using the pip command from the Installation section above.

### Angle Input Not Working Correctly
Enter the angle value directly in degrees (e.g., 90 for 90 degrees). The field is labeled "Total Bend Angle (°)".

### Template Dimensions Seem Wrong
Verify that wrap thickness is correct. Should be the total thickness of all wrap layers combined.

### Scale Bar Doesn't Measure 100mm
When printing, ensure "Scale" is set to "100%" or "Actual Size" in your print dialog. Do not use "Fit to page".

### Addon Panel Not Visible
Press 'N' key in the 3D viewport to open the sidebar, then look for the "Pipe Templates" tab.

### Context Errors
The addon automatically handles context switching. If you encounter errors, try reloading the addon or restarting Blender.

## File Structure

```
Blender-Pipe-Unwrapper/
├── pipe_template_generator.py     # Main Blender addon
├── README.md                        # This file
├── ADDON_INSTALLATION_GUIDE.txt    # Detailed installation guide
├── UPDATE_LOG.txt                   # Recent fixes and improvements
├── exhaust_wrap_template.pdf       # Example generated template
├── generate_pdf.py                  # Legacy standalone script
├── pdf_data.json                    # Legacy data file
├── boundary_data.json               # Legacy data file
├── uv_data.json                     # Legacy data file
└── Documentation/
    ├── FINAL_PRINTING_GUIDE.txt
    ├── 3INCH_5SEGMENT_CUTTING_GUIDE.txt
    ├── SEGMENTED_BEND_CUTTING_GUIDE.md
    └── COMPLETE_SOLUTION_SUMMARY.md
```

## Version History

### v1.1.0 (2025-11-19)
- Fixed UV outline rendering (reduced from 320 to 88 boundary edges)
- Relocated degrees per segment to title header
- Removed yellow info box for cleaner layout
- Updated seam location to ground plane at minimum radius
- Changed wrap input from radius to thickness (more intuitive)
- Fixed angle input to use degrees directly (not radians)
- Resolved context errors - works from any Blender mode
- Comprehensive testing on multiple configurations

### v1.0.0 (2025-11-18)
- Initial release
- Complete Blender addon with GUI
- Generates 3D curved pipe segments
- UV unwrapping with automatic seam detection
- PDF export with actual UV outline shape
- Two templates per page
- Scale bar and dimension annotations

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - See LICENSE file for details

## Acknowledgments

- Project: Bower Motorsport
- Developed for exhaust wrap fabrication
- Built with Blender Python API and reportlab

## Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check the ADDON_INSTALLATION_GUIDE.txt for detailed documentation
- Review the UPDATE_LOG.txt for recent changes

## Screenshots

### Blender Interface
The addon appears in the sidebar (press N) under "Pipe Templates":

```
┌─────────────────────────┐
│ Pipe Specifications:    │
│  Pipe OD: 76.2 mm      │
│  Bend Radius: 1.5 ×D   │
│  Bend Angle: 90.0 °    │
│  Num Segments: 5        │
├─────────────────────────┤
│ Wrap Layer:             │
│  Wrap Thickness: 6.15mm │
│  Overlap: 10.0 mm       │
├─────────────────────────┤
│ Output:                 │
│  Output Folder: [path]  │
├─────────────────────────┤
│  [Generate Template]    │
└─────────────────────────┘
```

### Generated PDF Template
- Two identical templates per A4 page
- Blue outline shows base pipe shape
- Red outline shows cutting line
- 100mm scale bar for verification
- Clear dimensions and legend

---

**Made with ❤️ for fabricators and motorsports enthusiasts**
